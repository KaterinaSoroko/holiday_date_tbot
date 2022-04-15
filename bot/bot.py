from datetime import date
from bot.birthday import list_birthday
from bot.constans import month


def get_data():
    today = date.today()
    day_today = int(today.strftime("%d"))
    month_today = int(today.strftime("%m"))
    year_today = int(today.strftime("%y")) + 2000
    return day_today, month_today, year_today


def prepare_message(date_today):
    answer_message = ""
    for string in list_birthday:
        if date_today[0] == string[0] and date_today[1] == string[1]:
            answer_message += f"Сегодня День Рождения у {string[4]}!\n"
            answer_message += f"""Поздравляем {string[3]} с {date_today[2] - string[2]}-летием!
Желаем здоровья, счастья и много приятных интересностей!\n\n"""

    if answer_message == "":
        answer_message = "Поздравляю всех с {} {}!".format(date_today[0], month[date_today[1]])
    return answer_message
