from datetime import date
from bot.birthday_example import list_birthday


answer_message = ""
date_today = date.today()

for string in list_birthday:
    delta_y = int(date_today.strftime("%y")) - int(string[2]) + 2000
    delta_m = int(date_today.strftime("%m")) - int(string[1])
    delta_d = int(date_today.strftime("%d")) - int(string[0])
    if delta_m == 0 and delta_d == 0:
        answer_message += f"Сегодня День Рождения у {string[4]}!\n"
        if delta_y <= 25:
            answer_message += f"""Поздравляем {string[3]} с {delta_y}-летием!
Желаем здоровья, счастья и много приятных интересностей!\n\n"""
        else:
            answer_message += f"""Поздравляем {string[3]} с Днем Рождения!
Желаем здоровья, счастья и много любви!\n\n"""

if answer_message == "":
    answer_message = "Поздравляю всех с {}.{}!".format(date_today.strftime('%d'), date_today.strftime('%m'))
