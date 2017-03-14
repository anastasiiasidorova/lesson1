question=input('Введите возраст, пожалуйста: ')
print(question)
ask_user=int(question)

def age_comparator(ask_user):
    if ask_user>=3 and ask_user<=6:
        return "Малыш ходит в садик"
    elif ask_user>=7 and ask_user<=18:
        return "Это не малыш, это школьник"
    elif ask_user>=0 and ask_user<=3:
        return "Такие маленькие ничего не делают, если только учатся ходить"
    elif ask_user>=19 and ask_user<=23:
        return "Товарищ-студент. Наверняка лекции прогуливает"   
    else:
        return "Товарищ либо работает, либо на пенсии"
result=age_comparator(ask_user)
print(result)