import random

def printboard(player1pos, player2pos):
    for row in range(10, 0, -1):
        for col in range(1, 11):
            newno = (row) * 10 - col
            if newno == player1pos:
                print("[P1]", end=' ')
            elif newno == player2pos:
                print("[P2]", end=' ')
            elif newno in sandl:
                print("[S]", end=' ')
            elif newno in sandl.values():
                print("[L]", end=' ')
            else:
                print("[-]", end=' ')
        print()

# Snakes and ladders
sandl = {24: 15, 38: 12, 47: 23, 70: 36, 80: 55, 98: 58}

def movedice(playerpos, dice):
    newpos = playerpos + dice
    print("Before position is:", newpos)
    if newpos in sandl:
        newpos = sandl[newpos]
        print("You are bitten by a snake!")
        return newpos
    elif newpos in sandl.values():
        for i in sandl:
            if sandl[i] == newpos:
                newpos = i
        print("You found a ladder!")
        return newpos
    else:
        return newpos

def diceroll():
    return random.randint(1, 6)

print("Welcome to Snakes and Ladders game")
print("-" * 50)

player1pos = 0
player2pos = 0
current_player = 1

while player1pos < 100 and player2pos < 100:
    if current_player == 1:
        print("Player 1 position is at", player1pos)
        input("Player 1, press Enter to roll the dice")
        dice = diceroll()
        print("Your lucky number is", dice)
        move = movedice(player1pos, dice)
        print("Your new position is", move)
        player1pos = move
        current_player = 2
    else:
        print("Player 2 position is at", player2pos)
        input("Player 2, press Enter to roll the dice")
        dice = diceroll()
        print("Your lucky number is", dice)
        move = movedice(player2pos, dice)
        print("Your new position is", move)
        player2pos = move
        current_player = 1
    
    print()
    printboard(player1pos, player2pos)
    print()
    print('*' * 50)

if player1pos >= 100:
    print("Game over! Player 1 won!!!")
else:
    print("Game over! Player 2 won!!!")
