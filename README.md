# Harley | Persian Therapy Chatbot for Telegram 🧠💬

**Harley** is a friendly, intelligent Telegram bot designed for conversational psychological support in Persian.  
Powered by GPT models via [OpenRouter.ai](https://openrouter.ai), Harley simulates a warm, empathetic therapy session.

---

## ✨ Features

- **Persian-only conversations** with a consistent character (“Harley”, an Iranian-origin clinical psychologist)  
- **Reflective listening**, empathy, motivational interviewing, CBT techniques  
- **Final analysis**: Identifies core issue, explores causes, and suggests actionable coping strategies at the end of each session  
- **Modular structure**: Easily extend with psychological quizzes and exercises  
- **Simple commands** to start and end AI chat

---

## ⚙️ Prerequisites

- Python 3.10 or higher  
- Install dependencies:

  ```bash
  pip install -r requirements.txt

Create a .env file in project root containing:

BOT_TOKEN=your_telegram_bot_token
OPENROUTER_API_KEY=your_openrouter_api_key



---

🚀 Running the Bot

python main.py

Start therapy session: /harley

End therapy session: /end



---

# 🗂️ Project Structure

```
harley_bot/
│
├── ai/
│   ├── ai_client.py      # OpenRouter API client
│   └── prompt.txt        # System prompt configuration
│
├── bot/
│   ├── commands.py       # Telegram bot commands
│   ├── handlers.py       # Message handlers
│   └── state.py         # User session management
│
├── main.py              # Application entry point
├── .env                 # Environment config
├── requirements.txt     # Dependencies
└── README.md           # Project docs
```

> Note: The core “Harley” prompt resides in ai/prompt.txt. Edit it to customize Harley’s personality and therapeutic style.




---

🗨️ Example Conversation

> User: “I feel like nothing motivates me anymore…”
Harley: “I hear you… It sounds like days have lost their color. Would you like to tell me when you first noticed this feeling?”
…
(At the end of the session, Harley summarizes the issue, explores possible roots, and provides practical suggestions.)




---

🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests to:

1. Add new psychological quizzes


2. Enhance conversational flows


3. Improve error handling and logging




---

📚 Resources

OpenRouter.ai Documentation

python-telegram-bot Library



---

Made with care to support Persian-speaking users on their journey to well-being.
Harley is always here to listen…


