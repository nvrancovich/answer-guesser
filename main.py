from functions import *

# n_questions = int(input('Enter the number of questions (int): '))
# n_answers = int(input('Enter the number of possible answers per question (int): '))
# passing_score = int(input('Enter the percentage of correct answers needed to pass (int): '))

n_questions = 10
n_answers = 3
passing_score = 40

answers = ['a','b','c','d','e']
answers = answers[:n_answers]

distribution = [1,2,3]

print(initial_answer(answers, distribution))