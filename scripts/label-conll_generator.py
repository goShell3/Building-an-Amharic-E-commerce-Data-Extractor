import pandas as pd
import re

# Load CSV file
df = pd.read_csv("cleaned_messages.csv")

# Extract first 32 non-empty messages from the clean_text column
messages = df['clean_text'].dropna().head(32).tolist()

def label_message(text):
    tokens = text.split()
    labels = ['O'] * len(tokens)

    for i, token in enumerate(tokens):
        # Label Price (e.g., "ዋጋ 1000 ብር", or "1000 ብር")
        if token in ["ዋጋ", "በ"] and i + 2 < len(tokens):
            if re.match(r'^\d+$', tokens[i + 1]) and "ብር" in tokens[i + 2]:
                labels[i] = "B-PRICE"
                labels[i + 1] = "I-PRICE"
                labels[i + 2] = "I-PRICE"
        elif re.match(r'^\d+$', token) and i + 1 < len(tokens) and "ብር" in tokens[i + 1]:
            labels[i] = "B-PRICE"
            labels[i + 1] = "I-PRICE"

        # Label Product (keywords: tablet, LCD, etc.)
        elif any(x in token.lower() for x in ["tablet", "lcd", "ታብሌት", "writing", "TAB"]):
            labels[i] = "B-Product"
            if i + 1 < len(tokens):
                labels[i + 1] = "I-Product"

        # Label Location (common location/place names or keywords)
        elif any(x in token for x in ["አድራሻ", "ደፋር", "ቦሌ", "ሞል", "ፎቅ"]):
            labels[i] = "B-LOC"
            if i + 1 < len(tokens):
                labels[i + 1] = "I-LOC"

    return list(zip(tokens, labels))

# Generate CoNLL format data
conll_data = []
for message in messages:
    labeled = label_message(message)
    conll_data.append(labeled)

# Save to CoNLL .txt format
with open("labeled_conll.txt", "w", encoding="utf-8") as f:
    for sentence in conll_data:
        for token, label in sentence:
            f.write(f"{token} {label}\n")
        f.write("\n")

print("✅ CoNLL formatted file saved as 'labeled_conll.txt'")
