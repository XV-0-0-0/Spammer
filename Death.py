import aiohttp
import asyncio
import time

URL = "URL"

REQUESTS = 100 #all
CONCURRENCY = 100 #same time

information = {
    "name": "Test",
    "userName": "Vlad",
    "userLocation": "Poland"
}

async def worker(session, i, results):
    start = time.time()
    try:
        async with session.post(URL, json=information) as resp:
            latency = round((time.time() - start) * 1000)
            results.append(latency)
            print(f"{i}: Status {resp.status} | {latency} ms")
    except Exception as e:
        print(f"{i}: ERROR {e}")

async def run_test():
    results = []

    conn = aiohttp.TCPConnector(limit=CONCURRENCY)
    async with aiohttp.ClientSession(connector=conn) as session:
        tasks = [worker(session, i, results) for i in range(REQUESTS)]
        await asyncio.gather(*tasks)

    print("\n---- RESULTS ----")
    print(f"Total requests: {len(results)}")
    print(f"Average latency: {sum(results)/len(results):.2f} ms")
    print(f"Fastest: {min(results)} ms")
    print(f"Slowest: {max(results)} ms")

if __name__ == "__main__":
    asyncio.run(run_test())
