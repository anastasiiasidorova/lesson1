


#открыть два файла? 
#записать данные в файл из двух сделать один, по столбикам: метро, остановки, геотег.
#сделать выборку с одинаковым геотегом, ограничиться сотыми долями?
#из этой выборки выбрать наибольшее количество остановок
#

import csv




#УЛИЦЫ



streets_dict={}

streets=open('moscow_trans_stops.csv', 'r', encoding='utf-8')
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
reader = csv.DictReader(streets, fields, delimiter=';')
key_street=None
value_street=None
for row in reader:
    #print(row.get('Street'),row.get('geoData')) 
    key_street=row.get('geoData')
    value_street=row.get('Street')
    streets_dict={key_street:value_street}
    print(streets_dict)




stations_dict={}
#СТАНЦИИ МЕТРО
stations=open('data_m1.csv', 'r')
    
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
reader = csv.DictReader(stations, fields, delimiter=';')
key_station=None
value_station=None    
for row in reader:
    #print(row.get('Станция метрополитена'), row.get('Геоданные')) 
    key_station=row.get('geoData')
    value_station=row.get('Street')
    streets_dict={key_station:value_station}
    stations_dict={row.get('Станция метрополитена'):row.get('Геоданные')}
    print(stations_dict)


streets.close()    
stations.close()
    





