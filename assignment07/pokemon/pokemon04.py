import aiofiles
import asyncio
import json
from pathlib import Path

pokemonapi_directory = './assignment07/pokemon/pokemonapi'
pokemonmove_directory = './assignment07/pokemon/pokemonmove'

async def process_all_file(path_files): #'path_file' is parameter path of JSON file to func
    async with aiofiles.open(path_files, mode='r') as f:
        contents = await f.read()
    
    # Load it into a dictionary and create a list of moves.
    pokemon = json.loads(contents)
    name = pokemon['name']
    moves = [move['move']['name'] for move in pokemon['moves']]
    
    # Open a new file to write the list of moves into.
    async with aiofiles.open(f'{pokemonmove_directory}/{name}_moves.txt', mode='w') as f:
        await f.write('\n'.join(moves))

async def main():
    pathlist = Path(pokemonapi_directory).glob('*.json')

    # Iterate through all json files in the directory.
    #for path in pathlist:
    #    print(path)
    
    tasks = [process_all_file(path) for path in pathlist]
    # func 'process_all_file' recieve 'pathlist'
    await asyncio.gather(*tasks)
    #wait all tasks complete (use for Process multiple JSON files)

asyncio.run(main())
