# azure_language_detection.py

import datetime
import json
import os
import requests
import sys
import uuid
from dotenv import load_dotenv

# Display Python version and current time
print("Python version:", sys.version)
print(f"Today is {datetime.datetime.today().strftime('%d-%b-%Y %H:%M:%S')}\n")

# Load Azure credentials from .env file
load_dotenv("azure.env")
azure_ai_translator_key = os.getenv("AZURE_AI_TRANSLATION_KEY")
azure_ai_translator_endpoint = os.getenv("AZURE_AI_TRANSLATION_ENDPOINT")
azure_ai_translator_region = os.getenv("AZURE_AI_TRANSLATION_REGION")

# Construct API URL
path = "/detect?api-version=3.0"
constructed_url = azure_ai_translator_endpoint + path

# Set headers for the request
headers = {
    "Ocp-Apim-Subscription-Key": azure_ai_translator_key,
    "Ocp-Apim-Subscription-Region": azure_ai_translator_region,
    "Content-type": "application/json",
    "X-ClientTraceId": str(uuid.uuid4()),
}

# Function to detect language from given text
def detect_language(text):
    body = [{"text": text}]
    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()

    print("\033[1;34m")  # ANSI color for blue
    print(
        json.dumps(
            response, sort_keys=True, indent=4, ensure_ascii=False, separators=(",", ": ")
        )
    )
    language = response[0]['language']
    score = response[0]['score']
    print(f"\033[0mDetected language: {language} with confidence = {score}\n")
    return language, score

# Sample inputs
texts = [
    "Bonjour, bienvenue à cette présentation Azure !",
    "こんにちは",
    "Salve. Benvenuti.",
    "مَسَاءُ الْخَيْرْ",
    "안녕하세요"
]

# Run detection for each sample
for text in texts:
    detect_language(text)