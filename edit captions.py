import csv
import json
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

client = OpenAI()

# Use the API key from the environment variables
client.api_key = os.getenv('OPENAI_API_KEY')

def shorten_caption(caption):
    # Call to OpenAI's API to edit the caption to a max length of 300 characters
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Shorten this to under 300 characters: {caption}"}
        ],
        max_tokens=300
    )
    return response.choices[0].message.content  # Response from GPT

def process_captions(file_path):
    # Read CSV and process captions
    captions_dict = {}
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            edited_caption = shorten_caption(row['caption'])
            captions_dict[row['filename']] = edited_caption
    
    # Write to JSON file
    with open('captions.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(captions_dict, jsonfile, ensure_ascii=False, indent=4)

# Provide the path to your CSV file here
process_captions('Your path here')
