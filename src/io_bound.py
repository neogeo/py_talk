import aiohttp
import requests

URL = 'https://k7hf6ipvq8.execute-api.us-west-2.amazonaws.com/sleep_lambda'


'''
Old School
'''
def io_call():
    res = requests.get(URL)
    res.raise_for_status()

    print('io finished')
    return res.json()


'''
New Hotness
'''
async def aio_call(aiohttp_session):
    async with aiohttp_session.get(URL) as result:
        result.raise_for_status()
        json = await result.text()

        print('io finished')

    return json