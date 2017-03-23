import datetime
dt=datetime.datetime.now()
print('datetime at this moment',dt)

print('date at this moment with the day of the week',dt.strftime('%A %d %B %Y'))


#class datetime.timedelta(days=0, seconds=0, microseconds=0, 
                          #milliseconds=0, minutes=0, hours=0, weeks=0)
from datetime import date, timedelta
delta = timedelta(days=1)
print('yesterday',dt-delta)

delta = timedelta(days=30)
print('one month ago',dt-delta)


#time.strptime(строка [, формат]) - разбор строки, представляющей время в соответствии с форматом. Возвращаемое значение struct_time. Формат по умолчанию: "%a %b %d %H:%M:%S %Y".
import datetime
date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string)
print('convert str to datetime object',date_dt)

print(datetime.strptime("01/01/17 12:10:03.234567", "%d/%m/%y %H:%M:%S.%f"))
