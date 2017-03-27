


#открыть два файла? 
#записать данные в файл из двух сделать один, по столбикам: метро, остановки, геотег.
#сделать выборку с одинаковым геотегом, ограничиться сотыми долями?
#из этой выборки выбрать наибольшее количество остановок
#

import csv




#УЛИЦЫ

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
    for row in reader:
        print(row.get('Street'),row.get('geoData')) 


#СТАНЦИИ МЕТРО
with open('data_m1.csv', 'r') as f:
    
    fields = ['Локальный идентификатор', 
     'Наименование',
     'Долгота в WGS-84',
     'Широта в WGS-84',
     'Станция метрополитена', 
     'Линия', 
     'Режим работы по чётным дням', 
     'Режим работы по нечётным дням', 
     'Количество полнофункциональных БПА (все типы билетов)', 
     'Количество малофункциональных БПА (билеты на 1 и 2 поездки)', 
     'Общее количество БПА', 
     'Ремонт эскалаторов', 
     'global_id', 
     'Геоданные'
     ]

    reader = csv.DictReader(f, fields, delimiter=';')
    
    for row in reader:
        print(row.get('Станция метрополитена'), row.get('Геоданные')) 

    





