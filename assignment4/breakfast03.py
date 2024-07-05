# Asynchronous breakfast
import asyncio
from time import sleep, time


async def make_coffee(): #1
    print("coffee: prepare ingridients")
    sleep(1)
    print("coffee: waiting...")
    await asyncio.sleep(5) # 2: pause, another tasks can be run
    print("coffee: ready")
    
async def fry_egg(): #1
    print("eggs: prepare ingridients")
    sleep(1)
    print("eggs: frying...")
    await asyncio.sleep(3) #2: pause, another tasks can be run
    print("eggs: ready")    

    
async def main():
    start = time()
    tasks = [make_coffee(), fry_egg()] # make task for insert function make_coffee & fry_egg
    await asyncio.gather(*tasks) 
    # run both task
    # await : wait function finish(wait result of asyncio.gather)
    # asyncio.gather : function for receive asyn function for run together
    # *task : * for unpack function in tasks
    print(f"breakfast is ready in {time()-start} min")
    
asyncio.run(main()) # run top-level function concurrently
    