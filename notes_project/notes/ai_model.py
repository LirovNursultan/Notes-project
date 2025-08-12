import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def predict_ai(note_text: str) -> str:
    """Отправка текста заметки в OpenAI для получения совета."""
    prompt = f"{note_text}\n\nДай совет, что почитать или посмотреть, чтобы лучше понять материал."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты полезный советчик по обучению."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Ошибка при работе с ИИ: {e}"