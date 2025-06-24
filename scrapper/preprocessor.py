import re

def clean_text(text):
    text = re.sub(r'[^\w\s።፣]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def tokenize(text):
    return text.split()  # simple split — replace with Amharic-specific tokenizer if needed
