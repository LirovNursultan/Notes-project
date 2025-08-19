import os
import openai
from dotenv import load_dotenv
import tensorflow as tf

# model = tf.keras.models.load_model('path/to/your_model.h5')
#
# def predict(input_data):
#     # input_data should be preprocessed to match the model's input shape
#     prediction = model.predict(input_data)
#     return prediction


load_dotenv()

import openai
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