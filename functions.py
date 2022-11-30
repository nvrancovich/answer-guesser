def check_score(score, passing_score):
    if score >= passing_score:
        print('Passing score reached!')
        quit()
    else:
        pass

def check_distribution(answers, n_questions):
    distributions = []
    for answer in answers:
        distribution = round((int(input(f'Enter the percentage of correct answers, when all answers are \'{answer}\': '))/100)*n_questions,0)
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

def search_answer(initial_answer,passing_score,distribution,answers):

    position = 0
    answer = list([[i,'undefined'] for i in initial_answer])
    order = list(i[0] for i in answer)
    cycle = answers + answers

    last_score = int(input(f'Enter the percentage of correct answers, using the following order \'{order}\': '))
    check_score(last_score, passing_score)

    answer[position][0] = cycle[cycle.index(answer[position][0]) + 1]

    while last_score <= passing_score:
        order = list(i[0] for i in answer)
        new_score = int(input(f'Enter the percentage of correct answers, using the following order \'{order}\': '))
        if last_score < new_score:
            answer[position][1] = 'correct'
            position += 1
        elif last_score > new_score:
            pass

        
        



        