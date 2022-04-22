import main
import os
import time

if __name__ == '__main__':
    os.system('clear')
    print('Welcome to this quizzing game. The following categories are available for quizzing:')
    for category in main.category_inputs:
        print(f'{category}. {main.category_inputs[category].upper()}')
    print('Please choose a category')
    inp1 = int(input().strip())
    print(f'You have chosen: {main.category_inputs[inp1].upper()}. Now choose your difficulty:')
    for diff in main.difficulty_inputs:
        print(f'{diff}. {main.difficulty_inputs[diff].upper()}')
    inp2 = int(input().strip())
    print(f'You have chosen: {main.difficulty_inputs[inp2].upper()}. \nNow choose a number of questions to answer (less than 50):')
    num = int(input().strip())
    os.system('clear')
    print(f'You have chosen to quiz in: \nthe category, {main.category_inputs[inp1].upper()};\ndifficulty, {main.difficulty_inputs[inp2].upper()};\nfor {num} question(s).')
    print('Let the quizzing begin!\n')
    time.sleep(3)
    os.system('clear')
    database = main.return_questions(inp1, inp2, num)

    correct_questions = 0
    for question in database[2]:
        print(question)
        for ans in database[2][question]:
            print(f'{ans}. {database[2][question][ans]}')

        print('Please choose your answer (enter: A, B, C or D):')
        ans = str(input())
        if database[2][question][ans] in database[1]:
            print('Correct!')
            correct_questions += 1
        else:
            print('Wrong.')
        time.sleep(2)
        os.system('clear')

    score = float(correct_questions/num)
    score = round(score*100, 2)

    print(f'You have answered {correct_questions} out of {num} correctly, giving a success rate of {score}%.')
    print('The correct answers were:')
    for ind, ans in enumerate(database[1]):
        print(f'{ind+1}. {ans}')

