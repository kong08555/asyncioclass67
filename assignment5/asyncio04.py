# example of waiting for all tasks to be completed with a timeout
from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(arg):
    # generate a random value between 0 and 10
    value = random() * 10
    #block for a moment
    await asyncio.sleep(value)
    #report the value
    print(f'>task {arg} done with {value}')
     
# main coroutine
async def main():
    #create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for the first task to fall, or all tasks to complete
    done,pending = await asyncio.wait(tasks, timeout=5)
    #report results
    print(f'Done, {len(done)} tasks complete in time')
    
#start the asyncio program
asyncio.run(main())