import asyncio
import random

async def async_generator():
    for i in range(10):
        yield i
        await asyncio.sleep(random.random())


async def runtimes(a):
    await asyncio.gather(*(main(i) for i in range(1, a+1)))


async def main(a = 0):
        async for i in async_generator():
            print(f"{a} : {i}")



if __name__ == "__main__":
    
    # I want to launch the main function asynchronously three times, with different arguments 1, 2 and 3
    #gens = [lambda:main(i) for i in range(1, 4)]
    asyncio.run(runtimes(3))