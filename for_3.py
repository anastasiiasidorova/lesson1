school = [
    {'school_class': '3A', 'scores': [5,5,4,5,4]},
    {'school_class': '5B', 'scores': [3,4,4,5,3]},
    {'school_class': '11G', 'scores': [5,3,4,5,5]},
]

summ = 0 #сумма всех оценок
count_of_scores = 0 #количество оценок

for score in school:
    score_list = score.get('scores')
    print('Списки оценок для каждого класса:  ', score_list)
    summ_class = 0
    for elem in score_list:
        summ_class += elem
    arithm_mean_class = summ_class / len(score_list)
    print('Сумма оценок по каждому классу:  ', summ_class)
    print('Среднее арифметическое по каждому классу:  ', arithm_mean_class)
    summ += summ_class
    for ind in score_list:
    	count_of_scores += 1

arithm_mean_school = int (summ / count_of_scores)
print('Общее количество оценок по трём классам:  ', count_of_scores)
print('Общая сумма оценок по школе:  ', summ)
print('Среднее арифметическое по школе:  ', arithm_mean_school)