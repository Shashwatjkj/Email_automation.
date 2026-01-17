from app.telegram.client import client
import asyncio
from app.listener import register_group_listener

async def main():
    await client.start()
    # async def read_group_messages(client, limit=5):
    #     entity = await client.get_entity(-1002947896517)

    #     messages = []
    #     async for msg in client.iter_messages(entity, limit=limit):
    #         if msg.text:
    #             messages.append(msg.text)

    #     return messages
    
    # print(await read_group_messages(client,2))
    register_group_listener(client,-1002947896517)

    print("NOW LISTENING — DO NOT CLOSE")
    await client.run_until_disconnected()
    print("DISCONNECTED")

   
    print("Telegram login successful")

if __name__ == "__main__":
    asyncio.run(main())
