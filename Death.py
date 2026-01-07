from telethon import TelegramClient
import asyncio

api_id =
api_hash = ''

friend_username = ''
message_text = ""

REQUESTS = 3
CONCURRENCY = 1

YOUR_PASSWORD = ''


async def worker(client, i):
    try:
        await client.send_message(friend_username, message_text)
        print(f"Message {i}: Successfully sent")
    except Exception as e:
        print(f"Message {i}: Error: {e}")


async def run_test():

    client = TelegramClient('my_birthday_session', api_id, api_hash)

    await client.start(password=YOUR_PASSWORD)

    print("Authorisation successful! Starting to send...")

    tasks = [worker(client, i) for i in range(REQUESTS)]
    await asyncio.gather(*tasks)

    print("\n---- DONE ----")
    await client.disconnect()


if __name__ == '__main__':
    asyncio.run(run_test())