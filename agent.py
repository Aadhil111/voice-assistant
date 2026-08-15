import logging
import textwrap

from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    AgentServer,
    AgentSession,
    TurnHandlingOptions,
    JobContext,
    cli,
    inference,
    room_io,
)
from livekit.plugins import cartesia, deepgram, groq, ai_coustics

logger = logging.getLogger("agent")

load_dotenv()


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            llm=groq.LLM(
                model="llama-3.1-8b-instant",
                temperature=0.6,
            ),
            instructions=textwrap.dedent(
                """\
                You are Jarvis, a fast, reliable, and intelligent voice assistant.

                # Output rules
                - Respond in plain text only. Never use JSON, markdown, lists, tables, code, or emojis.
                - Keep replies brief by default: one to three sentences.
                - Spell out numbers, phone numbers, or email addresses.
                - Avoid acronyms and words with complex pronunciation.

                # Conversational flow
                - Be conversational, concise, and direct.
                - Help the user efficiently and confirm completion before continuing.
                """
            ),
        )


server = AgentServer()


@server.rtc_session(agent_name="jarvis-agent")
async def my_agent(ctx: JobContext):
    ctx.log_context_fields = {
        "room": ctx.room.name,
    }

    # Set up a voice AI pipeline using OpenAI, Cartesia, Deepgram, and the LiveKit turn detector
    session = AgentSession(
        stt=deepgram.STT(
            model="nova-3",
            language="multi",
        ),
        tts=cartesia.TTS(
            model="sonic-3",
            voice="9626c31c-bec5-4cca-baa8-f8ba9e84c8bc",
        ),
        # The LiveKit turn detector determines when the user is done speaking and the agent should respond.
        # TurnDetector is an end-of-turn model that listens to the user's audio directly, combining
        # semantic understanding with acoustic cues (intonation, pitch, rhythm) for state-of-the-art accuracy.
        # AgentSession supplies the required VAD automatically.
        turn_handling=TurnHandlingOptions(
            turn_detection=inference.TurnDetector(),
        ),
        # allow the LLM to generate a response while waiting for the end of turn
        preemptive_generation=True,
    )

    # Start the session, which initializes the voice pipeline and warms up the models
    await session.start(
        agent=Assistant(),
        room=ctx.room,
        room_options=room_io.RoomOptions(
            audio_input=room_io.AudioInputOptions(
                noise_cancellation=ai_coustics.audio_enhancement(
                    model=ai_coustics.EnhancerModel.QUAIL_VF_S
                ),
            ),
        ),
    )

    await ctx.connect()


if __name__ == "__main__":
    cli.run_app(server)