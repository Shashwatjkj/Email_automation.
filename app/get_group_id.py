from telethon import TelegramClient
from app.config import API_ID, API_HASH
from app.ai.extraction_agent import extract_technical_jobs
from app.formatter import format_message

async def get_group_text_messages(
    client,
    group_id: int,
    limit: int = 10
) -> list[str]:
    """
    Retrieve last `limit` TEXT messages from a group.
    """

    texts = []

    async for message in client.iter_messages(group_id, limit=limit):
        if message.text:
            texts.append(message.text)

    return texts



async def main():
    client = TelegramClient("sessions/mysessions", API_ID, API_HASH)
    await client.start()

    # async for dialog in client.iter_dialogs():
    #     print("=" * 10)
    #     print("Name :", dialog.name)
    #     print("ID   :", dialog.id)
    #     print("Type :", type(dialog.entity).__name__)

    data = await get_group_text_messages(client,-1002947896517)

    data1 = format_message(data) 
    # print(data1)
    
    # print(extract_technical_jobs(data1))

    await client.disconnect()




if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
