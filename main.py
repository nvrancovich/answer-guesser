from functions import *

# n_questions = int(input('Enter the number of questions (int): '))
# n_answers = int(input('Enter the number of possible answers per question (int): '))
# passing_score = int(input('Enter the percentage of correct answers needed to pass (int): '))

n_questions = 10
n_answers = 4
passing_score = 40

answers = ['a','b','c','d','e']
answers = answers[:n_answers]

distribution = [2,1,0,1]

initial_answer = initial_answer(answers, distribution)


print(search_answer(initial_answer,passing_score,distribution,answers))