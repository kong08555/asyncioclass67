import asyncio
import time

class Coffee:
    pass

class Egg:
    pass

class Bacon:
    pass

class Toast:
    pass

class Juice:
    pass

async def PourCoffee():
    print(f"{time.ctime()} - Begin pour coffee...")
    await asyncio.sleep(2)  
    print(f"{time.ctime()} - Finish pour coffee...")
    print(f"{time.ctime()} - >>>>>>>>>> Coffee is ready\n")
    return Coffee()
    #return value to class  to indicate process this function complete

async def ApplyButter():
    print(f"{time.ctime()} - Begin apply butter...")
    await asyncio.sleep(1)  
    print(f"{time.ctime()} - Finish apply butter...")
    

async def FryEggs(eggs):
    print(f"{time.ctime()} - Begin fry eggs...")
    print(f"{time.ctime()} - Heat pan to fry eggs")
    await asyncio.sleep(1)
    for egg in range(eggs):
        print(f"{time.ctime()} - Frying", egg + 1, "eggs")
        await asyncio.sleep(1)  
    print(f"{time.ctime()} - >>>>>>>>>> Fry eggs are ready...")
    return Egg()

async def FryBacon():
    print(f"{time.ctime()} - Begin fry bacon...")
    await asyncio.sleep(2)  
    print(f"{time.ctime()} - Finish fry bacon...")
    print(f"{time.ctime()} - >>>>>>>>>>> Fry bacon is ready...")
    return Bacon()

async def ToastBread(slices): #slices in number of bread to want toast
    for slice in range(slices):
        print(f"{time.ctime()} - Toasting bread", slice + 1)
        await asyncio.sleep(1)  
        print(f"{time.ctime()} - Bread", slice + 1, "toasted")
        await ApplyButter() # insert ApplyButter func for wait this func finish
        print(f"{time.ctime()} - Toast", slice + 1, "ready")
    print(f"{time.ctime()} - >>>>>>>>>>> Toast are ready\n")
    return Toast()

async def PourJuice():
    print(f"{time.ctime()} - Begin pour juice...")
    await asyncio.sleep(1)  
    print(f"{time.ctime()} - Finish pour juice...")
    return Juice()

async def main():
    
    await PourCoffee()
    tasks = [asyncio.create_task(FryEggs(2)),
             asyncio.create_task(FryBacon()), 
             asyncio.create_task(ToastBread(2))]
             # asyncio.create_task for Create a task
    await asyncio.gather(*tasks) 
    #receive all task in array tasks to working together and wait until every task is finished.
    print(f"{time.ctime()} - >>>>>>>> Nearly to finished...")
    await PourJuice()

if __name__ == "__main__":
    start_cooking = time.perf_counter() #Record the current time in variable.
    asyncio.run(main())
    elapsed = time.perf_counter() - start_cooking
    print(f"{time.ctime()} - Breakfast cooked in" ,elapsed, "seconds.")
