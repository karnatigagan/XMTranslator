# azure_transliterate.py

import datetime
import json
import os
import requests
import sys
import uuid
from dotenv import load_dotenv

# Show Python version and current time
print("Python version:", sys.version)
print(f"Today is {datetime.datetime.today().strftime('%d-%b-%Y %H:%M:%S')}\n")

# Load Azure credentials from .env
load_dotenv("azure.env")

azure_ai_translator_key = os.getenv("AZURE_AI_TRANSLATION_KEY")
azure_ai_translator_endpoint = os.getenv("AZURE_AI_TRANSLATION_ENDPOINT")
azure_ai_translator_region = os.getenv("AZURE_AI_TRANSLATION_REGION")

# Transliterate endpoint with query params
path = "/transliterate?api-version=3.0"
params = "&language=ja&fromScript=jpan&toScript=latn"
constructed_url = azure_ai_translator_endpoint + path + params

# Request headers
headers = {
    "Ocp-Apim-Subscription-Key": azure_ai_translator_key,
    "Ocp-Apim-Subscription-Region": azure_ai_translator_region,
    "Content-type": "application/json",
    "X-ClientTraceId": str(uuid.uuid4()),
}

# Request body
body = [{"text": "こんにちは"}]

# POST request to transliterate
request = requests.post(constructed_url, headers=headers, json=body)
response = request.json()

# Display response
print("\033[1;34m")  # ANSI blue
print(json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(",", ": ")))

# Print transliteration result
print("\033[0m")  # Reset ANSI color
print(f"Result: {response[0]['text']} with script = {response[0]['script']}\n")