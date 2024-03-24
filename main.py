import asyncio
import random
import os

# Initial money
INITIAL_MONEY = 302123.32
PLAYER_EDGE = 0.49
total_money = INITIAL_MONEY
bets_placed = 0

async def coin_flip_bet():
    global total_money
    global bets_placed
    global PLAYER_EDGE
    while True:
        bet_amount = 5  # Starting bet

        while total_money >= bet_amount:
            bets_placed += 1
            # Simulate coin flip, win if result < 0.48
            coin_flip_result = random.random() < PLAYER_EDGE

            if not coin_flip_result:  # Loss
                total_money -= bet_amount
                bet_amount *= 1.85  # Double the bet for the next round
            else:  # Win
                total_money += bet_amount
                break  # Exit the loop after a win

            

            await asyncio.sleep(0.01)  # Allow other tasks to run
        

async def print_total_money():
    global INITIAL_MONEY
    global total_money
    global bets_placed
    while True:
        await asyncio.sleep(0.1)  # Update interval
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Total Money: {round(total_money, 2)}")
        net_money = total_money - INITIAL_MONEY

        if net_money >= 0:
            print(f"Net Money:  +{round(net_money, 2)}")
        else:
            print(f"Net Money:  {round(net_money, 2)}")        
        print(f"Bets Placed: {bets_placed}")
        

async def main():
    bet_tasks = [asyncio.create_task(coin_flip_bet()) for _ in range(1)]
    print_task = asyncio.create_task(print_total_money())
    await asyncio.gather(*bet_tasks, print_task)

if __name__ == '__main__':
    asyncio.run(main())
