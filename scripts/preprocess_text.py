import re

def clean_amharic_text(text):
    text = re.sub(r'[\u200b-\u200d\u2060]', '', text)  # Remove invisible chars
    text = re.sub(r'[^\w\s፡።፤፥፦፧]', '', text)  # Allow Amharic punctuation
    text = re.sub(r'\s+', ' ', text).strip()
    return text
