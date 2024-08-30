from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue):
    start_time = time.time()  
    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = i
        # block to simulate work
        sleeptime = 0.6
        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
        print(f"Queue size after put: {queue.qsize()}")  
    # send an all done signal
    await queue.put(None)
    print('Producer: Done')
    end_time = time.time()
    print("---------------------Producer time---------------------")
    print(f"Producer execution time: {end_time - start_time:.2f} seconds")
    print("-------------------------------------------------------")

# coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
            print(f"Queue size before get: {queue.qsize()}")  
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.1)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    # all done
    print('Consumer: Done')

# entry point coroutine
async def main():
    start_time = time.time()
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))
    end_time = time.time()
    print("---------------------Total time-------------------------")
    print(f"Program execution time: {end_time - start_time:.2f} seconds")
    print("--------------------------------------------------------")

# start the asyncio program
asyncio.run(main())
