name_list = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
ind = 0
while ind < len(name_list):
    if name_list.pop(ind) == 'Валера':
        print('Валера нашелся')
ind += 1