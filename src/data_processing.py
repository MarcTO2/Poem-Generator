import re

def clean_text(text):
    """
    Cleans the input text by removing unwanted characters and lowercasing it
    """
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text

def load_and_clean_data(filepath):
    """
    Loads text data from a file and cleans it
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    return clean_text(text)
