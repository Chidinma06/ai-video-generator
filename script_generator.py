import os
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_available_models():
    SKIP = [
        "whisper", "guard", "safeguard", "orpheus", "allam"
    ]
    try:
        models = client.models.list()
        available = [
            m.id for m in models.data
            if not any(skip in m.id.lower() for skip in SKIP)
        ]
        return available if available else [
            "openai/gpt-oss-20b",
            "openai/gpt-oss-120b",
            "qwen/qwen3.8-27b",
        ]
    except Exception:
        return [
            "openai/gpt-oss-20b",
            "openai/gpt-oss-120b",
            "qwen/qwen3.8-27b",
        ]

def generate_script(business_name, description, target_audience, tone):
    prompt = f"""
    You are a professional marketing scriptwriter.
    Write a 30-second promotional video script for a small business.

    Business name: {business_name}
    Description: {description}
    Target audience: {target_audience}
    Tone: {tone}

    Write only the spoken words. No stage directions, no camera directions, no text in brackets or parentheses, no scene descriptions. Only the words that will be spoken out loud.
    """

    models = get_available_models()

    for model in models:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            result = response.choices[0].message.content
            result = re.sub(r'<think>.*?</think>', '', result, flags=re.DOTALL)
            return result.strip()
        except Exception:
            continue

    return "Sorry, no models are currently available. Please try again shortly."