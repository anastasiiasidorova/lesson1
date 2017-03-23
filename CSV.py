#from answer_modified import answers
import csv


answers={"hello":"Hi", "how are you?":"I am fine", "bye":"Bye"}



with open('export.csv', 'w', encoding='utf-8') as f:
    new_dict1={'question':'hello', 'answer':'Hi'}
    new_dict2={'question':'how are you?', 'answer':'I am fine'}
    new_dict3={'question':'bye', 'answer':'Bye'}
    fields=['question','answer']
    print(new_dict1['question'])
    print(fields[0])

    
    writer = csv.DictWriter(f, fields, delimiter=';')

    writer.writeheader()


    
    writer.writerow(new_dict1)    
    
    writer.writerow(new_dict2)
    
    writer.writerow(new_dict3)


     