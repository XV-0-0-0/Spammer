from telethon import TelegramClient, errors
import asyncio

api_id =

api_hash = ''

friend_username = ''
message_text = ""

REQUESTS = 500

YOUR_PASSWORD = '1234567890qwe@#*'

async def run_test():
    client = TelegramClient('my_birthday_session', api_id, api_hash)
    await client.start(password=YOUR_PASSWORD)

    print(f" I am starting a marathon on {REQUESTS} Message")

    sent_count = 0

    while sent_count < REQUESTS:
        try:

            text = message_text.format(sent_count + 1)

            await client.send_message(friend_username, text)
            sent_count += 1

            print(f"[{sent_count}/{REQUESTS}] successful")

            await asyncio.sleep(0.3)

        except errors.FloodWaitError as e:
            print(f"\n Telegram FloodWait: one must wait {e.seconds} seconds.")
            print("Waiting")
            await asyncio.sleep(e.seconds + 5)
            print("continue\n")

        except Exception as e:
            print(f" Another mistake: {e}")
            await asyncio.sleep(2)

    print("\nAll messages sent.")
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(run_test())