

def _cpu():
    count = 0
    for i in range(1000000):
        count += i


async def aio_cpu():
    count = 0
    for i in range(1000000):
        count += i

