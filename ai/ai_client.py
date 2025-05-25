import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("OPENROUTER_MODEL")

with open('prompt.txt', 'r', encoding='utf-8') as file:
    system_prompt = file.read().strip()

user_histories: dict[int, list] = {}

def chat_with_harley(user_id: int, message: str) -> str:
    history = user_histories.get(user_id, [])

    history.append({"role": "user", "content": message})

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [{"role": "system", "content": system_prompt}] + history,
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        reply = response.json()["choices"][0]["message"]["content"]
        history.append({"role": "assistant", "content": reply})
        user_histories[user_id] = history[-10:]
        return reply

    except requests.RequestException as e:
        return "در ارتباط مشکلی پیش آمده. لطفاً بعداً تلاش کن."

