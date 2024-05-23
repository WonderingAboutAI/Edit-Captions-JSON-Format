# Edit-Captions-JSON-Format
This Python script reads image captions from a CSV file, shortens them using OpenAI's API, and then saves them in a JSON file. This could be particularly useful if you need image captions equal to or less than a certain character count for accessibility, social media, or training an image model.

## Features

### Environment Variable Management
Securely loads API keys and other sensitive settings from a .env file.

### OpenAI API Integration
Uses OpenAI’s GPT-3.5-turbo model to shorten captions effectively.

### CSV Input
Reads captions from a CSV file, which allows for batch processing of multiple captions.

### JSON Output
Outputs the processed captions in a JSON format, making it easy to integrate with web applications or other media.
Setup and Usage

## Prerequisites

* Python installed on your system.
* An OpenAI API key.
* A CSV file with at least two columns: filename and caption.

## Installation

1. Set up a Python environment (recommended):

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

1. Install required packages:

```
pip install openai python-dotenv

```

1. Prepare your environment:

Create a .env file in the same directory as the script and add your OpenAI API key:

```
OPENAI_API_KEY='your_api_key_here'
```

## Usage

### Prepare your CSV file
Ensure your CSV file is formatted correctly with filename and caption headers.

### Set your path
Modify the script to include the correct path to your CSV file in the process_captions('Your path here') call.

### Run the script
Output will be in `captions.json`.


