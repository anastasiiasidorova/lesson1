string1=input('Введите первую строку: ')
print(string1)
string2=input('Введите вторую строку: ')
print(string2)

def string_compare (string1,string2):
    if string1==string2:
        return 1
    elif string1!=string2 and string2=='learn':
        return 3
    elif string1!=string2 and len(string1)>len(string2):
        return 2
    else:
        return "There is no such variant. Sorry :-("
result=string_compare(string1,string2)
print(result)