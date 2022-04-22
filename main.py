import requests
import random
from generate_token import token


quiz_api_url = requests.get(f'https://opentdb.com/api.php?amount=10&{token}')
quiz_data = quiz_api_url.json()

categories = {
    'General knowledge': 9,
    'Science & Nature': 17,
    'Science: Computers': 18,
    'Science: Mathematics': 19,
    'Mythology': 20,
    'Geography': 22,
    'History': 23,
    'Politics': 24,
    'Art': 25,
    'Animals': 27
}

category_inputs = {
    0: 'General knowledge',
    1: 'Science & Nature',
    2: 'Science: Computers',
    3: 'Science: Mathematics',
    4: 'Mythology',
    5: 'Geography',
    6: 'History',
    7: 'Politics',
    8: 'Art',
    9: 'Animals'
}

difficulty_inputs = {
    0: 'easy',
    1: 'medium',
    2: 'hard'
}

def shuffle(arr):
    random.shuffle(arr)
    return arr

def return_questions(inp, inp2, num):
    question_dict = {}
    questions = []
    correct_answers = []
    options = ['A', 'B', 'C', 'D']
    
    api_url = f'https://opentdb.com/api.php?amount={num}&category={categories[category_inputs[inp]]}&difficulty={difficulty_inputs[inp2]}&type=multiple&{token}'
    api_data = requests.get(api_url).json()
    
    for result in api_data['results']:
        questions.append(result['question'])
        correct_answers.append(result['correct_answer'])
        
        all_ans = [ans for ans in result['incorrect_answers']]
        all_ans.append(result['correct_answer'])
        shuffle(all_ans)
        
        question_dict[result['question']] = {
            options[i]:all_ans[i] for i in range(4)
        }  
        
    return questions, correct_answers, question_dict

