import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    ball_number = 1
    while (True):
        await asyncio.sleep(power ** (-1))
        print(f'Силач {name} поднял {ball_number}')
        if ball_number == 5:
            print(f'Силач {name} закончил соревнования')
            break
        else:
            ball_number += 1

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Petr', 2))
    task2 = asyncio.create_task(start_strongman('Arcadiy', 15))
    task3 = asyncio.create_task(start_strongman('Ivan', 34))

    await task1
    await task2
    await task3

asyncio.run(start_tournament())