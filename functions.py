def check_score(score, passing_score):
    if score >= passing_score:
        print('Passing score reached!')
        quit()
    pass

def check_distribution(answers, n_questions):
    distributions = []
    for answer in answers:
        distribution = round((int(input(f'Enter the precentage of correct answers, when all answers are \'{answer}\': '))/100)*n_questions,0)
        distributions.append(distribution)
    return distributions

def initial_answer(answers, distribution):
    test = []
    position = 0
    for n in distribution:
        for i in range(n):
            test.append(answers[position])
        position += 1
    return(test)