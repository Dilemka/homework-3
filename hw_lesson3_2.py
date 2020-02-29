from datetime import datetime, timedelta

# Задание
# Напечатайте в консоль даты: вчера, сегодня, месяц назад
# Превратите строку "01/01/17 12:10:03.234567" в объект datetime

def dates (dt_now, dt_yst, date_dt):
    from datetime import datetime, timedelta
    dt_now = datetime.now()
    delta = timedelta(days = 1)
    dt_yst = dt_now - delta
    delta_m = timedelta(days = 31)
    dt_mnth = dt_now - delta_m
    print('Вчера ', dt_yst.strftime('%d.%m.%Y'))
    print('Сегодня ', dt_now.strftime('%d.%m.%Y'))
    print('Месяц назад ', dt_mnth.strftime('%d.%m.%Y'))
    return dt_yst, dt_now, dt_mnth
dates('dt_now', 'dt_yst', 'date_dt')

def dates (date_str='01/01/17 12:10:03.234567'):
    # date_str '
    date_dt = datetime.strptime(date_str, '%d/%m/%y %I:%M:%S.%f')
    print(date_dt)
    return date_dt
dates()
