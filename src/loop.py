import asyncio
import aiohttp

import io_bound

URL = 'https://k7hf6ipvq8.execute-api.us-west-2.amazonaws.com/sleep_lambda'


async def main():
    async with aiohttp.ClientSession() as session:
        result_text = await io_bound.aio_call(session)

    print(result_text)

asyncio.run(main())



