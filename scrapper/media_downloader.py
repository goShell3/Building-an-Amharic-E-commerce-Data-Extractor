import os
from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto

async def download_media(client, message, save_dir):
    if message.media and isinstance(message.media, MessageMediaPhoto):
        file_path = os.path.join(save_dir, f"{message.id}.jpg")
        await client.download_media(message, file_path)
        return file_path
    return None