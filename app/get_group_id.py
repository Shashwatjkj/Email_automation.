from telethon import TelegramClient
from app.config import API_ID, API_HASH


async def main():
    client = TelegramClient("sessions/mysessions", API_ID, API_HASH)
    await client.start()

    async for dialog in client.iter_dialogs():
        print("=" * 10)
        print("Name :", dialog.name)
        print("ID   :", dialog.id)
        print("Type :", type(dialog.entity).__name__)

    await client.disconnect()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
