import telebot
import time
from datetime import datetime
import json

token = "1488309358:AAFbJOYMVn4UlB7urhORAIB1oUwgnaKL4XM"
bot = telebot.TeleBot(token=token)


def congratulations():
    with open("students.json", "r") as file:
        birthdays = json.load(file)
        for student in birthdays:
            if student['date'][5:] == str(datetime.now().date())[5:]:
                bot.send_message(chat_id=624385066, text=f"Tug'ilgan kuningiz muborak {student['name'].upper()}!")

    with open("holidays.json", "r") as file:
        holidays = json.load(file)
        for holiday in holidays:
            if holiday['date'] == str(datetime.now().date())[5:]:
                bot.send_message(chat_id=624385066, text=f"{holiday['name'].upper()} bayrami barchaga muborak bo'lsin!")


while True:
    if str(datetime.now().time())[:5] == "00:00":
        congratulations()
        time.sleep(86400)



if __name__ == '__main__':

    bot.polling(none_stop=True)
