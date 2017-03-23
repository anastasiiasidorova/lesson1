import re
with open('referat.txt', 'r', encoding='utf-8') as f:
    #content = f.read()
    #print(content)
    count=0
    for line in f:
        line = line.replace('\n','')

        line_split=line.split(' ')
        print(line_split)


        list_filter=list(filter(None, line_split))
        print(list_filter)

        for ind in list_filter:
            if ind!=' ':
                count+=1
        print(count)





        

