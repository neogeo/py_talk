def fun(n):
    nums = []
    for i in range(0, n):
        nums.append(i)
    return nums


def gen(n):
    nums = []
    for i in range(0, n):
        yield i
    print('done')


def print_to_5(generator):
    for i in generator:
        if i > 5:
            break
        print(i)








#
#
# queue = []
# def my_loop():
#     queue.put(gen())
#     while not queue.emtpy():
#         # pop queue
#         # run until yeild
#










import asyncio


async def aio_func():
    print('starting')
    await asyncio.sleep(1)
    print('finished')


def run_async():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(aio_func())
    finally:
        loop.close()



