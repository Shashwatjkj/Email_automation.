from telethon import events
from app.formatter import format_message


def register_group_listener(client, group_id):
    """
    Listen for NEW messages in a specific Telegram group
    and print them with preserved spacing.
    """

    @client.on(events.NewMessage(chats=group_id))
    async def handler(event):
        if not event.message or not event.message.text:
            return

        formatted_text = format_message(event.message.text)

        print("\n" + "=" * 60)
        print("NEW MESSAGE RECEIVED")
        print("=" * 60)
        print(formatted_text)
