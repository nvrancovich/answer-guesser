def check_score(score, passing_score, record):
    if score >= passing_score:
        print('Passing score reached!')
        for r in record:
            print(r)
        quit()
    else:
        pass

def set_distribution(answers, n_questions):
    distributions = []
    for answer in answers:
        distribution = int(round((int(input(f'Enter the percentage of correct answers, when all answers are \'{answer}\': '))/100)*n_questions,0))
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

def check_distribution(answer, answers, distribution):
    for i in answer:
        distribution[answers.index(i[0])] -= 1
    return distribution


def search_answer(initial_answer,passing_score,distribution,answers):

    position = 0
    answer = list([[i,'undefined'] for i in initial_answer])
    order = list(i[0] for i in answer)
    cycle = answers + answers
    record = []

    last_score = int(input(f'Enter the percentage of correct answers, using the following order \'{order}\': '))
    check_score(last_score, passing_score,record)
    record.append((str(answer), last_score))

    answer[position][0] = cycle[cycle.index(answer[position][0]) + 1]

    while last_score <= passing_score:

        order = list(i[0] for i in answer)
        new_score = int(input(f'Enter the percentage of correct answers, using the following order \'{order}\': '))

        if last_score < new_score:
            answer[position][1] = 'correct'
            position += 1
            answer[position][0] = cycle[cycle.index(answer[position][0]) + 1]
            last_score = new_score
            record.append((str(answer), last_score))
            check_score(new_score, passing_score, record)

        elif last_score > new_score:
            answer[position][1] = 'correct'
            answer[position][0] = cycle[cycle.index(answer[position][0]) - 1]
            position += 1
            record.append((str(answer), last_score))
            check_score(new_score, passing_score, record)

        elif last_score == new_score:
            answer[position][0] = cycle[cycle.index(answer[position][0]) + 1]
            last_score = new_score
            record.append((str(answer), last_score))
            check_score(new_score, passing_score, record)

        
        



        