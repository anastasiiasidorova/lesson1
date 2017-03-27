import csv
with open('moscow_trans_stops.csv', 'r', encoding='utf-8') as f:
    #fields = ['position', 'station', 'street', 'route', 'direction', 'pavilion']
    fields = ['Name', 
    'Street', 
    'AdmArea', 
    'District', 
    'RouteNumbers', 
    'StationName', 
    'Direction', 
    'Pavilion', 
    'OperatingOrgName', 
    'geoData', 
    'global_id'
    ]
    reader = csv.DictReader(f, fields, delimiter=';')
    
    
    street_dict={}

    for row in reader:
        if row.get('Street') in street_dict:
            street_dict[row.get('Street')]+=1
        else:
            street_dict[row.get('Street')]=1

    #print(street_dict)
        #print(street_dict[row.get('Street')])
    

    #print(max(street_dict.values()))


    max_key_value = None
    

    for k, v in street_dict.items():
        if max_key_value is None or max_key_value[1] < v:
            max_key_value = (k, v)
    
    print(max_key_value)



    #print(len(street_dict))
  





   
            

            

         

  
        
        #street_max
        #print('Улица с максимальным количество остановок', street_max)













        #print(max(street_dict.values()))
        #var=street_dict.values()
        #list_l=list(var)
        #print(list_l)







        #print(row)
        #only_streets=row['Street']
        #print(only_streets)
        #only_streets=row.get('Street')
        #print(only_streets)
        #count+=1
        #print(count) #общее количество
        #dictionary={row.get('Street'):count}
        #print(dictionary)
