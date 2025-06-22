from telethon.tl.functions.messages import GetHistoryRequest
from telethon.sync import TelegramClient

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
client = TelegramClient('ecom_data', api_id, api_hash)
client.start()


channel = 'https://t.me/ShegerMarket'  # repeat for each channel

async def fetch_messages(channel):
    async with client:
        entity = await client.get_entity(channel)
        messages = await client(GetHistoryRequest(
            peer=entity,
            limit=100,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0
        ))
        return messages.messages
