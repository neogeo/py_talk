import aiohttp
import asyncio
import requests

import io_bound
import cpu_bound
from quart import Quart

app = Quart(__name__)


@app.route('/async')
async def async_endpoint():
    concurrent_io_tasks = []

    for i in range(0,3):
        task = io_bound.aio_call(app.aiohttp_session)
        concurrent_io_tasks.append(task)

    results = await asyncio.gather(*concurrent_io_tasks)

    # await cpu_bound.aio_cpu()
    return results[0]


@app.route('/sync')
def sync():
    for i in range(0,3):
        res = io_bound.io_call()
    
    return res 


@app.before_serving
async def create_session_connections():
    app.aiohttp_session = aiohttp.ClientSession()


@app.after_serving
async def close_session_connections():
    await app.aiohttp_session.close()
