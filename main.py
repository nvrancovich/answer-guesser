import os
from functions import *

os.system('clear')

# n_questions = int(input('Enter the number of questions (int): '))
# n_answers = int(input('Enter the number of possible answers per question (int): '))
# passing_score = int(input('Enter the percentage of correct answers needed to pass (int): '))

n_questions = 10
n_answers = 4
passing_score = 70

answers = ['a','b','c','d','e']
answers = answers[:n_answers]

distribution = check_distribution(answers, n_questions)

print(distribution)

initial_answer = initial_answer(answers, distribution)

search_answer(initial_answer,passing_score,distribution,answers)