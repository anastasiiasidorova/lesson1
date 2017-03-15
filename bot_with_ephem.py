from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import datetime

def greet_user(bot,update):
    print('Вызван /start')
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')
    bot.sendMessage(update.message.chat_id, text='Ну, пожалуйста!')
    bot.sendMessage(update.message.chat_id, 
        text='Звёздное небо таит в себе много тайн!')
    bot.sendMessage(update.message.chat_id, 'В каком созвездии сегодня Марс или Юпитер? Интересно?')
    bot.sendMessage(update.message.chat_id, 
        'Тогда введите /planet и название интересующей вас планеты Солнечной Сисемы на английском языке, и магия свершится! (Например, /planet Mars)')

def planet_query(bot,update):
    print('Вызван /planet')
    print(type(update.message.text))
    print(update.message.text)
    
def planet_search(bot,update):
    planets=['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    user_input_cap=update.message.text[8:].capitalize()
    print('поиск планеты')
    print('планета, которую ввел пользователь', user_input_cap)
    for index in planets:
        print(index)
        if user_input_cap==index:
            d=datetime.datetime.now().strftime('%Y')
            if user_input_cap=='Sun':
                planet_answer=ephem.constellation(ephem.Sun(datetime.datetime.now().strftime('%Y')))
                bot.sendMessage(update.message.chat_id,planet_answer)
                print(planet_answer)
            elif user_input_cap=='Moon':
                planet_answer=ephem.constellation(ephem.Moon(datetime.datetime.now().strftime('%Y')))
                bot.sendMessage(update.message.chat_id,planet_answer)  
                print(planet_answer)
            elif user_input_cap=='Mercury':
                planet_answer=ephem.constellation(ephem.Mercury(datetime.datetime.now().strftime('%Y')))
                bot.sendMessage(update.message.chat_id,planet_answer)
                print(planet_answer) 
            elif user_input_cap=='Venus':
                planet_answer=ephem.constellation(ephem.Venus(datetime.datetime.now().strftime('%Y')))
                bot.sendMessage(update.message.chat_id,planet_answer) 
                print(planet_answer)
            elif user_input_cap=='Mars':
                planet_answer=ephem.constellation(ephem.Mars(datetime.datetime.now().strftime('%Y')))
                bot.sendMessage(update.message.chat_id,planet_answer) 
                print(planet_answer) 
            elif user_input_cap=='Jupiter':
                planet_answer=ephem.constellation(ephem.Jupiter(datetime.datetime.now().strftime('%Y')))
                bot.sendMessage(update.message.chat_id,planet_answer) 
                print(planet_answer) 
            elif user_input_cap=='Saturn':
                planet_answer=ephem.constellation(ephem.Saturn(datetime.datetime.now().strftime('%Y')))
                bot.sendMessage(update.message.chat_id,planet_answer)  
                print(planet_answer)
            elif user_input_cap=='Uranus':
                planet_answer=ephem.constellation(ephem.Uranus(datetime.datetime.now().strftime('%Y')))
                bot.sendMessage(update.message.chat_id,planet_answer) 
                print(planet_answer) 
            elif user_input_cap=='Neptune':
                planet_answer=ephem.constellation(ephem.Neptune(datetime.datetime.now().strftime('%Y')))
                bot.sendMessage(update.message.chat_id,planet_answer) 
                print(planet_answer) 
            elif user_input_cap=='Pluto':
                planet_answer=ephem.constellation(ephem.Pluto(datetime.datetime.now().strftime('%Y')))
                bot.sendMessage(update.message.chat_id,planet_answer)
                print(planet_answer)

def show_error(bot,update,error):
    print(error)
 
def get_answer(question):
    answers={"привет": "и тебе привет!","как дела?": "Лучше всех!","что делаешь?": "сплю","пока": "и тебе пока"}
    print('поиск ответа')
    return answers.get(question,'Знаешь, порой мне кажется, что мы перестали понимать друг друга, печалька. Давай попробуем сначала?')

def talk_to_me(bot,update):
    print('блок отправки ботом сообщения')
    print(update.message.text)
    answer=get_answer(update.message.text)
    print(answer)
    bot.sendMessage(update.message.chat_id,answer)

def main():
    updater=Updater("291056924:AAHNPSrKjLEdN69AmIqTZH5n3As0wgNySJg")
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("planet", planet_search))
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()