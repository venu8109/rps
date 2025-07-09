import random
import sys
from enum import Enum

def RPS():
    class rps(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    game_count =0
    player_wins = 0
    python_wins = 0

    def play_rps():

        nonlocal player_wins
        nonlocal python_wins

        playerchoice = input('\nSelect One from Below\n1.Rock,\n2.Paper,\n3.Scissors\n\n')

        if playerchoice not in  ['1','2','3']:
            print('Please select one from the mentioned')
            return play_rps()
        
        player = int(playerchoice)

        computerchoice = random.choice('123')

        computer = int(computerchoice)

        print('\nYou Choose '+str(rps(player)).replace('rps.','').capitalize())
        print('Python Chooses '+str(rps(computer)).replace('rps.','').capitalize() + '\n')

        def decide_winner(player, computer):

            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return '🎉 You won the Game \n'
            elif player == 2 and computer == 1:
                player_wins += 1
                return '🎉 You won the Game \n'
            elif player == 3 and computer == 2:
                player_wins += 1
                return '🎉 You won the Game\n'
            elif player == computer:
                return '😲 Wow it\'s a tie game\n'
            else :
                python_wins += 1
                return '🐍 Python Won the Game'
        
        winner = decide_winner(player, computer)
        print(winner)

        nonlocal game_count
        game_count += 1
        print('Your Game Count is ' + str(game_count))
        print('your win Count is ' + str(player_wins))
        print('python\'s win Count is ' + str(python_wins))
        print('Play more to Increase your Game count')
        print('\nDo you want to play Again?\n')
        
        while True:
            playagain = input('PRESS\nY for yes\nQ to quit\n\n')
            if playagain.lower() not in ['y','q']:
                continue
            else:
                break
        
        if playagain.lower() == 'y':
            return play_rps()
        else :
            print('\nThanks for playing')
            print('you are welcomed all the time.')
            

    return play_rps

play = RPS()
play()