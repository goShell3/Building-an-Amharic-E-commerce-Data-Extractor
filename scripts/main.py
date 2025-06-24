import asyncio, os, csv
from scrapper.fetch_telegram import fetch_channel_messages
from scrapper.preprocessor import clean_text, tokenize

CHANNELS = [
    "@ZemenExpress", "@nevacomputer", "@meneshayeofficial", "@ethio_brand_collection",
    "@Leyueqa", "@sinayelj", "@Shewabrand", "@helloomarketethiopia", "@modernshoppingcenter",
    "@qnashcom", "@Fashiontera", "@kuruwear", "@gebeyaadama", "@MerttEka", "@forfreemarket",
    "@classybrands", "@marakibrand", "@aradabrand2", "@marakisat2", "@belaclassic", "@AwasMart"
]


async def main():
    all_data = []
    for channel in CHANNELS:
        print(f"Fetching from {channel}")
        messages = await fetch_channel_messages(channel, limit=100)
        for msg in messages:
            if msg["text"]:
                msg["clean_text"] = clean_text(msg["text"])
                msg["tokens"] = tokenize(msg["clean_text"])
        all_data.extend(messages)

    # Ensure directory exists
    os.makedirs("../../data/processed", exist_ok=True)

    # Write to CSV
    with open("data/processed/cleaned_messages.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "channel", "message_id", "timestamp", "text", "clean_text", "tokens"
        ])
        writer.writeheader()
        for msg in all_data:
            writer.writerow({
                "channel": msg.get("channel"),
                "message_id": msg.get("message_id"),
                "timestamp": msg.get("timestamp"),
                "text": msg.get("text"),
                "clean_text": msg.get("clean_text", ""),
                "tokens": " ".join(msg.get("tokens", []))
            })


asyncio.run(main())
