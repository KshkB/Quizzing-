import main
import os
import time
import random
import sys

def one_more_time(input1, correctly_answered = 0, questions_answered = 0):
    db = main.return_questions(random.randrange(0, 10), input1, 1)
    os.system('clear')
    for question in db[2]:
        print(question)
        for ans in db[2][question]:
            print(f'{ans}. {db[2][question][ans]}')
        print('Please choose your answer (enter: A, B, C or D)')
        ans = str(input().strip())
        questions_answered += 1
        try:
            if db[2][question][ans] in db[1]:
                print('Correct!')
                correctly_answered += 1
            else:
                print(f'Wrong. \nThe correct answer is: {db[1][0]}')
        except KeyError:
            print('That is not a valid entry.\nPlease try again:')
            ans = str(input().strip())
            try:
                if db[2][question][ans] in db[1]:
                    print('Correct!')
                    correctly_answered += 1
            except KeyError:
                print('Wrong entry again. Your game ends now!')
                return

    print('Would you like to play again? (Y or N)')
    rsp = str(input().strip())
    if rsp == 'Y':
        return one_more_time(input1, correctly_answered, questions_answered)

    score = 100*correctly_answered/questions_answered
    score = round(score, 2)
    os.system('clear')
    print(f'Transcript. \nIn this session you have answered {correctly_answered} out of {questions_answered} questions.')
    print(f'Your success rate for this session is {score}%. \nSee you next time!')
    time.sleep(4)
    return

if __name__ == '__main__':
    os.system('clear')
    print('In this game you will be bombarded with quiz qustions until you decide to stop.\nAre you ready to begin? (Y or N)')
    response = str(input().strip())

    if response != 'Y':
        sys.exit(0)
#        os.system("kill -9 %d"%(os.getppid()))

    print('Please choose the difficulty of the bombardment:')
    for diff in main.difficulty_inputs:
        print(f'{diff}. {main.difficulty_inputs[diff].upper()}')
    inp2 = int(input().strip())
    if inp2 not in range(3):
        print('That is an invalid choice.\nPlease choose again:')
        inp2 = int(input().strip())
    if inp2 not in range(3):
        print('Wrong entry again. Your game is ended!')
        os.system('clear')
        sys.exit(0)

    print('OK, lets begin!')
    time.sleep(3)
    os.system('clear')

    one_more_time(inp2)

    time.sleep(2)
    os.system('clear')