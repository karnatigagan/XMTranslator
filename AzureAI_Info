# azure_translator_info.py

import datetime
import pandas as pd
import sys
import os
from azure.ai.translation.text import TextTranslationClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.text.models import InputTextItem
from azure.core.exceptions import HttpResponseError
from dotenv import load_dotenv

# Print Python version
print("Python version:", sys.version)
print(f"Today is {datetime.datetime.today().strftime('%d-%b-%Y %H:%M:%S')}\n")

# Load Azure credentials
load_dotenv("azure.env")

azure_ai_translator_key = os.getenv("AZURE_AI_TRANSLATION_KEY")
azure_ai_translator_region = os.getenv("AZURE_AI_TRANSLATION_REGION")

credential = AzureKeyCredential(azure_ai_translator_key)
text_translator = TextTranslationClient(
    credential=credential,
    region=azure_ai_translator_region
)

# Get supported languages (default)
print("=== Supported Languages (Default) ===\n")
try:
    response = text_translator.get_supported_languages()

    print(f"Translate: {len(response.translation or {})}")
    print(f"Transliterate: {len(response.transliteration or {})}")
    print(f"Dictionary: {len(response.dictionary or {})}\n")

    if response.translation:
        print("Translation Languages:")
        for i, (key, value) in enumerate(response.translation.items(), 1):
            print(f"{i}. {key} -- {value.name} ({value.native_name})")
    print()

    if response.transliteration:
        print("Transliteration Languages:")
        for i, (key, value) in enumerate(response.transliteration.items(), 1):
            print(f"{i}. {key} -- {value.name}, scripts: {len(value.scripts)}")
    print()

    if response.dictionary:
        print("Dictionary Languages:")
        for i, (key, value) in enumerate(response.dictionary.items(), 1):
            print(f"{i}. {key} -- {value.name}, targets: {len(value.translations)}")

except HttpResponseError as e:
    print("Error fetching language data")
    if e.error:
        print(f"Error Code: {e.error.code}\nMessage: {e.error.message}")
    raise

# Get supported languages (localized, French)
print("\n=== Supported Languages (Localized - French) ===\n")
try:
    accept_language = "fr"
    response = text_translator.get_supported_languages(accept_language=accept_language)

    print(f"Translate: {len(response.translation or {})}")
    print(f"Transliterate: {len(response.transliteration or {})}")
    print(f"Dictionary: {len(response.dictionary or {})}\n")

    if response.translation:
        print("Translation Languages:")
        for i, (key, value) in enumerate(response.translation.items(), 1):
            print(f"{i}. {key} -- {value.name} ({value.native_name})")

    if response.transliteration:
        print("\nTransliteration Languages:")
        for i, (key, value) in enumerate(response.transliteration.items(), 1):
            print(f"{i}. {key} -- {value.name}, scripts: {len(value.scripts)}")

    if response.dictionary:
        print("\nDictionary Languages:")
        for i, (key, value) in enumerate(response.dictionary.items(), 1):
            print(f"{i}. {key} -- {value.name}, targets: {len(value.translations)}")

except HttpResponseError as e:
    print("Error fetching localized language data")
    if e.error:
        print(f"Error Code: {e.error.code}\nMessage: {e.error.message}")
    raise

# Create DataFrame
data = []
if response.translation:
    for key, value in response.translation.items():
        data.append({
            'Language_Code': key,
            'Language_Name': value.name,
            'Native_Name': value.native_name
        })

df = pd.DataFrame(data)
print("\nDataFrame Created:")
print(df.head())

print("\nShape:", df.shape)

# Save to Excel
df.to_excel("languages.xlsx", index=False)
print("Saved to 'languages.xlsx'")

# Functions
def get_language_name(langcode):
    langname = df.loc[df['Language_Code'] == langcode, 'Language_Name'].values[0]
    print(langcode, "=>", langname)
    return langname

def get_language_code(langname):
    langcode = df.loc[df['Language_Name'] == langname, 'Language_Code'].values[0]
    print(langname, "=>", langcode)
    return langcode

# Example usage
get_language_name("fr")
get_language_code("Français")

# Save another output
df.to_excel("output.xlsx", index=False)
print("Also saved to 'output.xlsx'")