#restaurant lunch
import asyncio
import random

#cooking rice
async def cook_rice():
    cook_time = 1 + random.random() # random more 1 second
    print(f'Microwave (rice):, cooking {cook_time:.4f} seconds..')
    await asyncio.sleep(cook_time)
    print('Microwave (rice) is finish!')
    return f'Rice is completed in {cook_time:.4f}'

#cooking noodle
async def cook_noodle():
    cook_time = 1 + random.random()
    print(f'Microwave (noodle): cooking {cook_time:.4f} seconds..')
    await asyncio.sleep(cook_time)
    print('Microwave (noodle) is finish!')
    return f'noodle is completed in {cook_time:.4f}'

#cooking curry 
async def cook_curry():
    cook_time = 1 + random.random()
    print(f'Microwave (curry): cooking {cook_time:.4f} seconds..')
    await asyncio.sleep(cook_time)
    print('Microwave (curry) is finish!')
    return f'curry is completed in {cook_time:.4f}'

async def main():
    tasks = [cook_rice(), cook_noodle(),cook_curry()]
    
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    #FIRST_COMPLETE is Returned when a one of task in group is completed.
    
    for task in done:
        print(f'Complete task: {len(done)}')
        print(f' - {task.result()} ')
        
    print(f'uncomplete task: {len(pending)}')

# Run the asyncio program
asyncio.run(main())
