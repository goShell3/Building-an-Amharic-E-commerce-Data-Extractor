import asyncio
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import json, os

API_ID: int = 25736723
API_HASH = 'f5978e7341470b96d02b676d1987bfb3'
SESSION = 'ecom_session'

client = TelegramClient(SESSION, API_ID, API_HASH)

async def fetch_channel_messages(channel_username, limit=100):
    await client.start()
    entity = await client.get_entity(channel_username)
    messages = await client(GetHistoryRequest(
        peer=entity,
        limit=limit,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0
    ))
    data = []
    for msg in messages.messages:
        if msg.message:
            data.append({
                "channel": channel_username,
                "message_id": msg.id,
                "sender_id": msg.from_id.user_id if msg.from_id else None,
                "timestamp": str(msg.date),
                "text": msg.message,
                "media": msg.media
            })
    return data
