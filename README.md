# Jarvis AI Voice Assistant

A real-time AI voice assistant built with **Python and LiveKit Agents**, designed for fast and natural voice conversations.

> 🚧 **Status:** In Development — the current version implements the real-time voice pipeline. Java Spring Boot token generation and cloud deployment are planned next.

## ✨ Features

- 🎙️ Real-time voice conversations
- 🧠 Groq LLM with **Llama 3.1 8B Instant**
- 🗣️ Multilingual speech-to-text using **Deepgram Nova-3**
- 🔊 Text-to-speech using **Cartesia Sonic-3**
- ⚡ Preemptive generation for faster responses
- 🎯 LiveKit turn detection
- 🎧 Audio enhancement using **ai-coustics**
- 🔐 API credentials managed using environment variables
- 🐍 Built with Python and Object-Oriented Programming

## 🏗️ Architecture

```text
                    User
                      │
                  Voice Input
                      │
                      ▼
              ┌───────────────┐
              │    LiveKit    │
              │ Voice Session │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │   Deepgram    │
              │    Nova-3     │
              │     STT       │
              └───────┬───────┘
                      │
                    Text
                      │
                      ▼
              ┌───────────────┐
              │     Groq      │
              │ Llama 3.1 8B  │
              │    Instant    │
              └───────┬───────┘
                      │
                AI Response
                      │
                      ▼
              ┌───────────────┐
              │    Cartesia   │
              │    Sonic-3    │
              │     TTS       │
              └───────┬───────┘
                      │
                Voice Output
                      │
                      ▼
                    User
```

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| LiveKit Agents | Real-time voice agent framework |
| Groq | LLM inference |
| Llama 3.1 8B Instant | Language model |
| Deepgram Nova-3 | Speech-to-text |
| Cartesia Sonic-3 | Text-to-speech |
| ai-coustics | Audio enhancement |
| python-dotenv | Environment variable management |

## 📁 Project Structure

```text
jarvis-ai-assistant/
│
├── agent.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Prerequisites

Before running the project, make sure you have:

- Python 3.10+
- A LiveKit account/project
- LiveKit API credentials
- Groq API key
- Deepgram API key
- Cartesia API key

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
LIVEKIT_URL=
LIVEKIT_API_KEY=
LIVEKIT_API_SECRET=

DEEPGRAM_API_KEY=
GROQ_API_KEY=
CARTESIA_API_KEY=
```

Add your actual API credentials to the `.env` file.

**Never commit `.env` to GitHub.**

The repository includes `.env.example` as a template.

## ▶️ Running the Project

Run the LiveKit agent:

```powershell
python agent.py console
```

Once the agent starts, connect to the LiveKit session and begin a voice conversation.

> The exact command may vary depending on the installed LiveKit Agents version.

## 🧠 How It Works

The assistant uses a real-time voice pipeline:

```text
User speaks
     ↓
LiveKit receives audio
     ↓
Deepgram Nova-3
Speech → Text
     ↓
Groq / Llama 3.1 8B Instant
Text → AI Response
     ↓
Cartesia Sonic-3
Text → Speech
     ↓
LiveKit streams audio
     ↓
User hears response
```

### Turn Detection

LiveKit's turn detector determines when the user has finished speaking.

The project also uses **preemptive generation**, allowing the LLM to begin preparing a response while the system is waiting for the final end-of-turn signal.

This helps reduce perceived response latency.

### Audio Enhancement

The project uses **ai-coustics audio enhancement** to improve incoming audio quality before processing.

## 🔐 Security

API credentials are loaded from environment variables using `python-dotenv`.

```python
from dotenv import load_dotenv

load_dotenv()
```

Secrets are not hard-coded in the source code.

The `.env` file is excluded from Git using `.gitignore`.

## 🚧 Future Development

The project is currently being extended with:

- [ ] Java Spring Boot backend
- [ ] Secure LiveKit token generation
- [ ] Backend authentication
- [ ] Cloud deployment
- [ ] Integration between Java backend and Python voice agent
- [ ] Additional AI assistant tools
- [ ] External service integrations
- [ ] More JARVIS-like capabilities

## 🎯 Project Goal

The long-term goal is to build a personal AI assistant inspired by **JARVIS**, capable of understanding natural voice commands, responding conversationally, and interacting with external services to perform useful tasks.

## 👨‍💻 Author

**Mohammed Aadil N**

Computer Science & Engineering  
Java Backend Developer | AI & Voice Assistant Development
