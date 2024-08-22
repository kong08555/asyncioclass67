import asyncio
import httpx
import time

async def get_pokemon_details(client, url):
    start_time = time.perf_counter()
    print(f"{time.ctime()} - get {url}")
    response = await client.get(url)
    data = response.json()
    end_time = time.perf_counter()
    
    pokemon_names = [pokemon['pokemon']['name'] for pokemon in data['pokemon']]
    time_taken = end_time - start_time
    return pokemon_names, time_taken

async def main():
    start_time = time.perf_counter()  
    async with httpx.AsyncClient() as client:
        urls = {
            "battle-armor": "https://pokeapi.co/api/v2/ability/battle-armor",
            "speed-boost": "https://pokeapi.co/api/v2/ability/speed-boost"
        }
        
        tasks = [asyncio.create_task(get_pokemon_details(client, url)) for url in urls.values()]
        results = await asyncio.gather(*tasks)
        
        
        for ability, (pokemon_names, time_taken) in zip(urls.keys(), results):
            print(f"{time.ctime()} - {pokemon_names}")
            print(f"{time.ctime()} - Asynchronous get ability={ability}:{len(pokemon_names)} pokemons. Time taken: {time_taken} seconds\n")
            

    end_time = time.perf_counter()  
    overall_time = end_time - start_time  
    print(f"{time.ctime()} - Asynchronous finished. Time taken: {overall_time} seconds")

if __name__ == '__main__':
    asyncio.run(main())


