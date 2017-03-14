
name_list = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
def find_person(name):
    ind = 0
    while ind < len(name_list):
        if name_list.pop(ind) == str(name):
            print('Человек по имени' + ' ' + str(name) + ' '  + 'нашелся')
    ind += 1
find_person('Вася')