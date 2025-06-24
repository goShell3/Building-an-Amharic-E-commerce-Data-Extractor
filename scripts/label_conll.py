import pandas as pd
import os

# Load cleaned CSV
df = pd.read_csv("data/processed/cleaned_messages.csv", encoding="utf-8")

# How many messages to label
NUM_MESSAGES = 50

# Output CSV path
output_csv = "data/processed/conll_labeled.csv"

def get_label(token):
    valid = {"O", "B-Product", "I-Product", "B-LOC", "I-LOC", "B-PRICE", "I-PRICE", ""}
    prompt = f"Label for '{token}': "
    while True:
        lbl = input(prompt).strip()
        if lbl == "":
            return "O"
        if lbl in valid:
            return lbl
        print("Invalid label! Use one of: O, B-Product, I-Product, B-LOC, I-LOC, B-PRICE, I-PRICE or press Enter for O.")

def main():
    labeled_data = []

    # Use first N rows/messages
    for idx, row in df.head(NUM_MESSAGES).iterrows():
        print(f"\n--- Message {idx+1}/{NUM_MESSAGES} ---")
        print("Original Text:", row["text"])
        tokens = row["tokens"].split()
        msg_id = row["message_id"]

        for token in tokens:
            label = get_label(token)
            labeled_data.append({
                "message_id": msg_id,
                "token": token,
                "label": label
            })

    # Save to CSV
    os.makedirs("data/processed", exist_ok=True)
    labeled_df = pd.DataFrame(labeled_data)
    labeled_df.to_csv(output_csv, index=False, encoding="utf-8")
    print(f"\n✅ Labeled data saved to: {output_csv}")

if __name__ == "__main__":
    main()
