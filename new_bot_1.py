from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def greet_user(bot,update):
    print('Вызван /start')
    print(update)
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')
    bot.sendMessage(update.message.chat_id, text='Ну, пожалуйста')

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
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_error_handler(show_error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()