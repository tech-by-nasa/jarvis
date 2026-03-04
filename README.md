⚡ JARVIS: Project Stark (2026 Edition)

A high-performance personal AI assistant built with Gemini 3 Flash and RealtimeSTT.

🚀 Quick Start

Clone the Hub: git clone https://github.com/tech-by-nasa/jarvis
Install Core: pip install RealtimeSTT google-generativeai pinggy
Environment: Set your GEMINI_API_KEY in a .env file.
🌐 External Access (For Outsiders)

To allow a friend or "outsider" to interact with your local Jarvis HUD, we use Pinggy. It provides a secure, temporary URL without port forwarding.

Start the Jarvis Web UI: python app.py --mode web (Starts local server on port 8000)

use

ssh -p 443 -R0:localhost:8000 a.pinggy.io

Generate the Outsider Link: Run this in a new terminal:

ssh -p 443 -R0:localhost:8000 a.pinggy.io

standard dependenices

pip install google-genai edge-tts RealtimeSTT customtkinter python-dotenv gitpython
