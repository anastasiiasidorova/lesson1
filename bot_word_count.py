from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
import ephem
import datetime
import random

import telegram
from telegram import ReplyKeyboardMarkup, KeyboardButton

from telebot import types
import telebot

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
    bot.sendMessage(update.message.chat_id, 'Теперь bot умеет считать слова во фразе. Например, введите: /wordcount "Как дела"')
    bot.sendMessage(update.message.chat_id, 
        'Также bot умеет производить простейшие арифметические операции: + - / *, введите, например: /calculator 2+3=')
    bot.sendMessage(update.message.chat_id, 
        'Также bot умеет производить простейшие арифметические операции: плюс, минус, умножить, разделить, если цифры (от одного до десяти) заданы словами, введите, например: /wordcalculator сколько будет один плюс два')
    bot.sendMessage(update.message.chat_id, 
        'Также bot умеет производить простейшие арифметические операции: сложить с, вычесть из, умножить на, разделить на, с вещественными числами (от одного до десяти), если они заданы словами, введите, например: /floatwordcalculator четыре и шесть умножить на шесть и два')    
    bot.sendMessage(update.message.chat_id,
        'Чтобы узнать дату ближайшего полнолуния в октябре, введите: /fullmoonoctober Когда ближайшее полнолуние после 2016-10-01?')
    bot.sendMessage(update.message.chat_id,
        'Чтобы узнать дату ближайшего полнолуния в принципе, введите: /fullmoon Когда ближайшее полнолуние?')    
    bot.sendMessage(update.message.chat_id,
        'Поиграем в города? Вводи: /goroda Москва') 
  

 
def goroda_query(bot,update):
    print('Вызван /goroda')
    print(type(update.message.text))
    print(update.message.text)

def goroda_search(bot,update):
    cities = [
        'Абаза',
        'Абакан',
        'Абдулино',
        'Абинск',
        'Агидель',
        'Агрыз',
        'Адыгейск',
        'Азнакаево',
        'Азов',
        'Ак-Довурак',
        'Аксай',
        'Алагир',
        'Алапаевск',
        'Алатырь',
        'Алдан',
        'Алейск',
        'Александров',
        'Александровск',
        'Александровск-Сахалинский',
        'Алексеевка',
        'Алексин',
        'Алзамай',
        'Алупка',
        'Алушта',
        'Альметьевск',
        'Амурск',
        'Анадырь',
        'Анапа',
        'Ангарск',
        'Андреаполь',
        'Анжеро-Судженск',
        'Анива',
        'Апатиты',
        'Апрелевка',
        'Апшеронск',
        'Арамиль',
        'Аргун',
        'Ардатов',
        'Ардон',
        'Арзамас',
        'Аркадак',
        'Армавир',
        'Армянск',
        'Арсеньев',
        'Арск',
        'Артём',
        'Артёмовск',
        'Артёмовский',
        'Архангельск',
        'Асбест',
        'Асино',
        'Астрахань',
        'Аткарск',
        'Ахтубинск',
        'Ачинск',
        'Аша',
        'Бабаево',
        'Бабушкин',
        'Бавлы',
        'Багратионовск',
        'Байкальск',
        'Баймак',
        'Бакал',
        'Баксан',
        'Балабаново',
        'Балаково',
        'Балахна',
        'Балашиха',
        'Балашов',
        'Балей',
        'Балтийск',
        'Барабинск',
        'Барнаул',
        'Барыш',
        'Батайск',
        'Бахчисарай',
        'Бежецк',
        'Белая Калитва',
        'Белая Холуница',
        'Белгород',
        'Белебей',
        'Белёв',
        'Белинский',
        'Белово',
        'Белогорск',
        'Белогорск',
        'Белозерск',
        'Белокуриха',
        'Беломорск',
        'Белорецк',
        'Белореченск',
        'Белоусово',
        'Белоярский',
        'Белый',
        'Бердск',
        'Березники',
        'Берёзовский',
        'Берёзовский',
        'Беслан',
        'Бийск',
        'Бикин',
        'Билибино',
        'Биробиджан',
        'Бирск',
        'Бирюсинск',
        'Бирюч',
        'Благовещенск',
        'Благовещенск',
        'Благодарный',
        'Бобров',
        'Богданович',
        'Богородицк',
        'Богородск',
        'Боготол',
        'Богучар',
        'Бодайбо',
        'Бокситогорск',
        'Болгар',
        'Бологое',
        'Болотное',
        'Болохово',
        'Болхов',
        'Большой Камень',
        'Бор',
        'Борзя',
        'Борисоглебск',
        'Боровичи',
        'Боровск',
        'Бородино',
        'Братск',
        'Бронницы',
        'Брянск',
        'Бугульма',
        'Бугуруслан',
        'Будённовск',
        'Бузулук',
        'Буинск',
        'Буй',
        'Буйнакск',
        'Бутурлиновка',
        'Валдай',
        'Валуйки',
        'Велиж',
        'Великие Луки',
        'Великий Новгород',
        'Великий Устюг',
        'Вельск',
        'Венёв',
        'Верещагино',
        'Верея',
        'Верхнеуральск',
        'Верхний Тагил',
        'Верхний Уфалей',
        'Верхняя Пышма',
        'Верхняя Салда',
        'Верхняя Тура',
        'Верхотурье',
        'Верхоянск',
        'Весьегонск',
        'Ветлуга',
        'Видное',
        'Вилюйск',
        'Вилючинск',
        'Вихоревка',
        'Вичуга',
        'Владивосток',
        'Владикавказ',
        'Владимир',
        'Волгоград',
        'Волгодонск',
        'Волгореченск',
        'Волжск',
        'Волжский',
        'Вологда',
        'Володарск',
        'Волоколамск',
        'Волосово',
        'Волхов',
        'Волчанск',
        'Вольск',
        'Воркута',
        'Воронеж',
        'Ворсма',
        'Воскресенск',
        'Воткинск',
        'Всеволожск',
        'Вуктыл',
        'Выборг',
        'Выкса',
        'Высоковск',
        'Высоцк',
        'Вытегра',
        'Вышний Волочёк',
        'Вяземский',
        'Вязники',
        'Вязьма',
        'Вятские Поляны',
        'Гаврилов Посад',
        'Гаврилов-Ям',
        'Гагарин',
        'Гаджиево',
        'Гай',
        'Галич',
        'Гатчина',
        'Гвардейск',
        'Гдов',
        'Геленджик',
        'Георгиевск',
        'Глазов',
        'Голицыно',
        'Горбатов',
        'Горно-Алтайск',
        'Горнозаводск',
        'Горняк',
        'Городец',
        'Городище',
        'Городовиковск',
        'Гороховец',
        'Горячий Ключ',
        'Грайворон',
        'Гремячинск',
        'Грозный',
        'Грязи',
        'Грязовец',
        'Губаха',
        'Губкин',
        'Губкинский',
        'Гудермес',
        'Гуково',
        'Гулькевичи',
        'Гурьевск',
        'Гурьевск',
        'Гусев',
        'Гусиноозёрск',
        'Гусь-Хрустальный',
        'Давлеканово',
        'Дагестанские Огни',
        'Далматово',
        'Дальнегорск',
        'Дальнереченск',
        'Данилов',
        'Данков',
        'Дегтярск',
        'Дедовск',
        'Демидов',
        'Дербент',
        'Десногорск',
        'Джанкой',
        'Дзержинск',
        'Дзержинский',
        'Дивногорск',
        'Дигора',
        'Димитровград',
        'Дмитриев',
        'Дмитров',
        'Дмитровск',
        'Дно',
        'Добрянка',
        'Долгопрудный',
        'Долинск',
        'Домодедово',
        'Донецк',
        'Донской',
        'Дорогобуж',
        'Дрезна',
        'Дубна',
        'Дубовка',
        'Дудинка',
        'Духовщина',
        'Дюртюли',
        'Дятьково',
        'Евпатория',
        'Егорьевск',
        'Ейск',
        'Екатеринбург',
        'Елабуга',
        'Елец',
        'Елизово',
        'Ельня',
        'Еманжелинск',
        'Емва',
        'Енисейск',
        'Ермолино',
        'Ершов',
        'Ессентуки',
        'Ефремов',
        'Железноводск',
        'Железногорск',
        'Железногорск',
        'Железногорск-Илимский',
        'Жердевка',
        'Жигулёвск',
        'Жиздра',
        'Жирновск',
        'Жуков',
        'Жуковка',
        'Жуковский',
        'Завитинск',
        'Заводоуковск',
        'Заволжск',
        'Заволжье',
        'Задонск',
        'Заинск',
        'Закаменск',
        'Заозёрный',
        'Заозёрск',
        'Западная Двина',
        'Заполярный',
        'Зарайск',
        'Заречный',
        'Заречный',
        'Заринск',
        'Звенигово',
        'Звенигород',
        'Зверево',
        'Зеленогорск',
        'Зеленоградск',
        'Зеленодольск',
        'Зеленокумск',
        'Зерноград',
        'Зея',
        'Зима',
        'Златоуст',
        'Злынка',
        'Змеиногорск',
        'Знаменск',
        'Зубцов',
        'Зуевка',
        'Ивангород',
        'Иваново',
        'Ивантеевка',
        'Ивдель',
        'Игарка',
        'Ижевск',
        'Избербаш',
        'Изобильный',
        'Иланский',
        'Инза',
        'Инкерман',
        'Иннополис',
        'Инсар',
        'Инта',
        'Ипатово',
        'Ирбит',
        'Иркутск',
        'Исилькуль',
        'Искитим',
        'Истра',
        'Ишим',
        'Ишимбай',
        'Йошкар-Ола',
        'Кадников',
        'Казань',
        'Калач',
        'Калач-на-Дону',
        'Калачинск',
        'Калининград',
        'Калининск',
        'Калтан',
        'Калуга',
        'Калязин',
        'Камбарка',
        'Каменка',
        'Каменногорск',
        'Каменск-Уральский',
        'Каменск-Шахтинский',
        'Камень-на-Оби',
        'Камешково',
        'Камызяк',
        'Камышин',
        'Камышлов',
        'Канаш',
        'Кандалакша',
        'Канск',
        'Карабаново',
        'Карабаш',
        'Карабулак',
        'Карасук',
        'Карачаевск',
        'Карачев',
        'Каргат',
        'Каргополь',
        'Карпинск',
        'Карталы',
        'Касимов',
        'Касли',
        'Каспийск',
        'Катав-Ивановск',
        'Катайск',
        'Качканар',
        'Кашин',
        'Кашира',
        'Кедровый',
        'Кемерово',
        'Кемь',
        'Керчь',
        'Кизел',
        'Кизилюрт',
        'Кизляр',
        'Кимовск',
        'Кимры',
        'Кингисепп',
        'Кинель',
        'Кинешма',
        'Киреевск',
        'Киренск',
        'Киржач',
        'Кириллов',
        'Кириши',
        'Киров',
        'Киров',
        'Кировград',
        'Кирово-Чепецк',
        'Кировск',
        'Кировск',
        'Кирс',
        'Кирсанов',
        'Киселёвск',
        'Кисловодск',
        'Клин',
        'Клинцы',
        'Княгинино',
        'Ковдор',
        'Ковров',
        'Ковылкино',
        'Когалым',
        'Кодинск',
        'Козельск',
        'Козловка',
        'Козьмодемьянск',
        'Кола',
        'Кологрив',
        'Коломна',
        'Колпашево',
        'Кольчугино',
        'Коммунар',
        'Комсомольск',
        'Комсомольск-на-Амуре',
        'Конаково',
        'Кондопога',
        'Кондрово',
        'Константиновск',
        'Копейск',
        'Кораблино',
        'Кореновск',
        'Коркино',
        'Королёв',
        'Короча',
        'Корсаков',
        'Коряжма',
        'Костерёво',
        'Костомукша',
        'Кострома',
        'Котельники',
        'Котельниково',
        'Котельнич',
        'Котлас',
        'Котово',
        'Котовск',
        'Кохма',
        'Красавино',
        'Красноармейск',
        'Красноармейск',
        'Красновишерск',
        'Красногорск',
        'Краснодар',
        'Краснозаводск',
        'Краснознаменск',
        'Краснознаменск',
        'Краснокаменск',
        'Краснокамск',
        'Красноперекопск',
        'Краснослободск',
        'Краснослободск',
        'Краснотурьинск',
        'Красноуральск',
        'Красноуфимск',
        'Красноярск',
        'Красный Кут',
        'Красный Сулин',
        'Красный Холм',
        'Кремёнки',
        'Кропоткин',
        'Крымск',
        'Кстово',
        'Кубинка',
        'Кувандык',
        'Кувшиново',
        'Кудымкар',
        'Кузнецк',
        'Куйбышев',
        'Кулебаки',
        'Кумертау',
        'Кунгур',
        'Купино',
        'Курган',
        'Курганинск',
        'Курильск',
        'Курлово',
        'Куровское',
        'Курск',
        'Куртамыш',
        'Курчатов',
        'Куса',
        'Кушва',
        'Кызыл',
        'Кыштым',
        'Кяхта',
        'Лабинск',
        'Лабытнанги',
        'Лагань',
        'Ладушкин',
        'Лаишево',
        'Лакинск',
        'Лангепас',
        'Лахденпохья',
        'Лебедянь',
        'Лениногорск',
        'Ленинск',
        'Ленинск-Кузнецкий',
        'Ленск',
        'Лермонтов',
        'Лесной',
        'Лесозаводск',
        'Лесосибирск',
        'Ливны',
        'Ликино-Дулёво',
        'Липецк',
        'Липки',
        'Лиски',
        'Лихославль',
        'Лобня',
        'Лодейное Поле',
        'Лосино-Петровский',
        'Луга',
        'Луза',
        'Лукоянов',
        'Луховицы',
        'Лысково',
        'Лысьва',
        'Лыткарино',
        'Льгов',
        'Любань',
        'Люберцы',
        'Любим',
        'Людиново',
        'Лянтор',
        'Магадан',
        'Магас',
        'Магнитогорск',
        'Майкоп',
        'Майский',
        'Макаров',
        'Макарьев',
        'Макушино',
        'Малая Вишера',
        'Малгобек',
        'Малмыж',
        'Малоархангельск',
        'Малоярославец',
        'Мамадыш',
        'Мамоново',
        'Мантурово',
        'Мариинск',
        'Мариинский Посад',
        'Маркс',
        'Махачкала',
        'Мглин',
        'Мегион',
        'Медвежьегорск',
        'Медногорск',
        'Медынь',
        'Межгорье',
        'Междуреченск',
        'Мезень',
        'Меленки',
        'Мелеуз',
        'Менделеевск',
        'Мензелинск',
        'Мещовск',
        'Миасс',
        'Микунь',
        'Миллерово',
        'Минеральные Воды',
        'Минусинск',
        'Миньяр',
        'Мирный',
        'Мирный',
        'Михайлов',
        'Михайловка',
        'Михайловск',
        'Михайловск',
        'Мичуринск',
        'Могоча',
        'Можайск',
        'Можга',
        'Моздок',
        'Мончегорск',
        'Морозовск',
        'Моршанск',
        'Мосальск',
        'Москва',
        'Муравленко',
        'Мураши',
        'Мурманск',
        'Муром',
        'Мценск',
        'Мыски',
        'Мытищи',
        'Мышкин',
        'Набережные Челны',
        'Навашино',
        'Наволоки',
        'Надым',
        'Назарово',
        'Назрань',
        'Называевск',
        'Нальчик',
        'Нариманов',
        'Наро-Фоминск',
        'Нарткала',
        'Нарьян-Мар',
        'Находка',
        'Невель',
        'Невельск',
        'Невинномысск',
        'Невьянск',
        'Нелидово',
        'Неман',
        'Нерехта',
        'Нерчинск',
        'Нерюнгри',
        'Нестеров',
        'Нефтегорск',
        'Нефтекамск',
        'Нефтекумск',
        'Нефтеюганск',
        'Нея',
        'Нижневартовск',
        'Нижнекамск',
        'Нижнеудинск',
        'Нижние Серги',
        'Нижний Ломов',
        'Нижний Новгород',
        'Нижний Тагил',
        'Нижняя Салда',
        'Нижняя Тура',
        'Николаевск',
        'Николаевск-на-Амуре',
        'Никольск',
        'Никольск',
        'Никольское',
        'Новая Ладога',
        'Новая Ляля',
        'Новоалександровск',
        'Новоалтайск',
        'Новоаннинский',
        'Нововоронеж',
        'Новодвинск',
        'Новозыбков',
        'Новокубанск',
        'Новокузнецк',
        'Новокуйбышевск',
        'Новомичуринск',
        'Новомосковск',
        'Новопавловск',
        'Новоржев',
        'Новороссийск',
        'Новосибирск',
        'Новосиль',
        'Новосокольники',
        'Новотроицк',
        'Новоузенск',
        'Новоульяновск',
        'Новоуральск',
        'Новохопёрск',
        'Новочебоксарск',
        'Новочеркасск',
        'Новошахтинск',
        'Новый Оскол',
        'Новый Уренгой',
        'Ногинск',
        'Нолинск',
        'Норильск',
        'Ноябрьск',
        'Нурлат',
        'Нытва',
        'Нюрба',
        'Нягань',
        'Нязепетровск',
        'Няндома',
        'Облучье',
        'Обнинск',
        'Обоянь',
        'Обь',
        'Одинцово',
        'Озёрск',
        'Озёрск',
        'Озёры',
        'Октябрьск',
        'Октябрьский',
        'Окуловка',
        'Олёкминск',
        'Оленегорск',
        'Олонец',
        'Омск',
        'Омутнинск',
        'Онега',
        'Опочка',
        'Орёл',
        'Оренбург',
        'Орехово-Зуево',
        'Орлов',
        'Орск',
        'Оса',
        'Осинники',
        'Осташков',
        'Остров',
        'Островной',
        'Острогожск',
        'Отрадное',
        'Отрадный',
        'Оха',
        'Оханск',
        'Очёр',
        'Павлово',
        'Павловск',
        'Павловский Посад',
        'Палласовка',
        'Партизанск',
        'Певек',
        'Пенза',
        'Первомайск',
        'Первоуральск',
        'Перевоз',
        'Пересвет',
        'Переславль-Залесский',
        'Пермь',
        'Пестово',
        'Петров Вал',
        'Петровск',
        'Петровск-Забайкальский',
        'Петрозаводск',
        'Петропавловск-Камчатский',
        'Петухово',
        'Петушки',
        'Печора',
        'Печоры',
        'Пикалёво',
        'Пионерский',
        'Питкяранта',
        'Плавск',
        'Пласт',
        'Плёс',
        'Поворино',
        'Подольск',
        'Подпорожье',
        'Покачи',
        'Покров',
        'Покровск',
        'Полевской',
        'Полесск',
        'Полысаево',
        'Полярные Зори',
        'Полярный',
        'Поронайск',
        'Порхов',
        'Похвистнево',
        'Почеп',
        'Починок',
        'Пошехонье',
        'Правдинск',
        'Приволжск',
        'Приморск',
        'Приморск',
        'Приморско-Ахтарск',
        'Приозерск',
        'Прокопьевск',
        'Пролетарск',
        'Протвино',
        'Прохладный',
        'Псков',
        'Пугачёв',
        'Пудож',
        'Пустошка',
        'Пучеж',
        'Пушкино',
        'Пущино',
        'Пыталово',
        'Пыть-Ях',
        'Пятигорск',
        'Радужный',
        'Радужный',
        'Райчихинск',
        'Раменское',
        'Рассказово',
        'Ревда',
        'Реж',
        'Реутов',
        'Ржев',
        'Родники',
        'Рославль',
        'Россошь',
        'Ростов-на-Дону',
        'Ростов',
        'Рошаль',
        'Ртищево',
        'Рубцовск',
        'Рудня',
        'Руза',
        'Рузаевка',
        'Рыбинск',
        'Рыбное',
        'Рыльск',
        'Ряжск',
        'Рязань',
        'Саки',
        'Салават',
        'Салаир',
        'Салехард',
        'Сальск',
        'Самара',
        'Санкт-Петербург',
        'Саранск',
        'Сарапул',
        'Саратов',
        'Саров',
        'Сасово',
        'Сатка',
        'Сафоново',
        'Саяногорск',
        'Саянск',
        'Светлогорск',
        'Светлоград',
        'Светлый',
        'Светогорск',
        'Свирск',
        'Свободный',
        'Себеж',
        'Севастополь',
        'Северо-Курильск',
        'Северобайкальск',
        'Северодвинск',
        'Североморск',
        'Североуральск',
        'Северск',
        'Севск',
        'Сегежа',
        'Сельцо',
        'Семёнов',
        'Семикаракорск',
        'Семилуки',
        'Сенгилей',
        'Серафимович',
        'Сергач',
        'Сергиев Посад',
        'Сердобск',
        'Серов',
        'Серпухов',
        'Сертолово',
        'Сибай',
        'Сим',
        'Симферополь',
        'Сковородино',
        'Скопин',
        'Славгород',
        'Славск',
        'Славянск-на-Кубани',
        'Сланцы',
        'Слободской',
        'Слюдянка',
        'Смоленск',
        'Снежинск',
        'Снежногорск',
        'Собинка',
        'Советск',
        'Советск',
        'Советск',
        'Советская Гавань',
        'Советский',
        'Сокол',
        'Солигалич',
        'Соликамск',
        'Солнечногорск',
        'Соль-Илецк',
        'Сольвычегодск',
        'Сольцы',
        'Сорочинск',
        'Сорск',
        'Сортавала',
        'Сосенский',
        'Сосновка',
        'Сосновоборск',
        'Сосновый Бор',
        'Сосногорск',
        'Сочи',
        'Спас-Деменск',
        'Спас-Клепики',
        'Спасск',
        'Спасск-Дальний',
        'Спасск-Рязанский',
        'Среднеколымск',
        'Среднеуральск',
        'Сретенск',
        'Ставрополь',
        'Старая Купавна',
        'Старая Русса',
        'Старица',
        'Стародуб',
        'Старый КрымОспаривается',
        'Старый Оскол',
        'Стерлитамак',
        'Стрежевой',
        'Строитель',
        'Струнино',
        'Ступино',
        'Суворов',
        'СудакОспаривается',
        'Суджа',
        'Судогда',
        'Суздаль',
        'Суоярви',
        'Сураж',
        'Сургут',
        'Суровикино',
        'Сурск',
        'Сусуман',
        'Сухиничи',
        'Сухой Лог',
        'Сызрань',
        'Сыктывкар',
        'Сысерть',
        'Сычёвка',
        'Сясьстрой',
        'Тавда',
        'Таганрог',
        'Тайга',
        'Тайшет',
        'Талдом',
        'Талица',
        'Тамбов',
        'Тара',
        'Тарко-Сале',
        'Таруса',
        'Татарск',
        'Таштагол',
        'Тверь',
        'Теберда',
        'Тейково',
        'Темников',
        'Темрюк',
        'Терек',
        'Тетюши',
        'Тимашёвск',
        'Тихвин',
        'Тихорецк',
        'Тобольск',
        'Тогучин',
        'Тольятти',
        'Томари',
        'Томмот',
        'Томск',
        'Топки',
        'Торжок',
        'Торопец',
        'Тосно',
        'Тотьма',
        'Трёхгорный',
        'Троицк',
        'Трубчевск',
        'Туапсе',
        'Туймазы',
        'Тула',
        'Тулун',
        'Туран',
        'Туринск',
        'Тутаев',
        'Тында',
        'Тырныауз',
        'Тюкалинск',
        'Тюмень',
        'Уварово',
        'Углегорск',
        'Углич',
        'Удачный',
        'Удомля',
        'Ужур',
        'Узловая',
        'Улан-Удэ',
        'Ульяновск',
        'Унеча',
        'Урай',
        'Урень',
        'Уржум',
        'Урус-Мартан',
        'Урюпинск',
        'Усинск',
        'Усмань',
        'Усолье-Сибирское',
        'Усолье',
        'Уссурийск',
        'Усть-Джегута',
        'Усть-Илимск',
        'Усть-Катав',
        'Усть-Кут',
        'Усть-Лабинск',
        'Устюжна',
        'Уфа',
        'Ухта',
        'Учалы',
        'Уяр',
        'Фатеж',
        'Феодосия',
        'Фокино',
        'Фокино',
        'Фролово',
        'Фрязино',
        'Фурманов',
        'Хабаровск',
        'Хадыженск',
        'Ханты-Мансийск',
        'Харабали',
        'Харовск',
        'Хасавюрт',
        'Хвалынск',
        'Хилок',
        'Химки',
        'Холм',
        'Холмск',
        'Хотьково',
        'Цивильск',
        'Цимлянск',
        'Циолковский',
        'Чадан',
        'Чайковский',
        'Чапаевск',
        'Чаплыгин',
        'Чебаркуль',
        'Чебоксары',
        'Чегем',
        'Чекалин',
        'Челябинск',
        'Чердынь',
        'Черемхово',
        'Черепаново',
        'Череповец',
        'Черкесск',
        'Чёрмоз',
        'Черноголовка',
        'Черногорск',
        'Чернушка',
        'Черняховск',
        'Чехов',
        'Чистополь',
        'Чита',
        'Чкаловск',
        'Чудово',
        'Чулым',
        'Чусовой',
        'Чухлома',
        'Шагонар',
        'Шадринск',
        'Шали',
        'Шарыпово',
        'Шарья',
        'Шатура',
        'Шахтёрск',
        'Шахты',
        'Шахунья',
        'Шацк',
        'Шебекино',
        'Шелехов',
        'Шенкурск',
        'Шилка',
        'Шимановск',
        'Шиханы',
        'Шлиссельбург',
        'Шумерля',
        'Шумиха',
        'Шуя',
        'Щёкино',
        'Щёлкино',
        'Щёлково',
        'Щигры',
        'Щучье',
        'Электрогорск',
        'Электросталь',
        'Электроугли',
        'Элиста',
        'Энгельс',
        'Эртиль',
        'Югорск',
        'Южа',
        'Южно-Сахалинск',
        'Южно-Сухокумск',
        'Южноуральск',
        'Юрга',
        'Юрьев-Польский',
        'Юрьевец',
        'Юрюзань',
        'Юхнов',
        'Ядрин',
        'Якутск',
        'Ялта',
        'Ялуторовск',
        'Янаул',
        'Яранск',
        'Яровое',
        'Ярославль',
        'Ярцево',
        'Ясногорск',
        'Ясный',
        'Яхрома',
    ]

    #print('А',cities[0:56])
    #print('Б',cities[56:140])
    #print('В',cities[140:197])
    #print('Г',cities[197:235])
    #print('Д',cities[235:271])
    #print('Е',cities[271:286])
    #print('Ж',cities[286:297])
    #print('З',cities[297:328])
    #print('И',cities[328:350])
    #print('Й',cities[350])
    #print('К',cities[351:508])
    #print('Л',cities[508:547])
    #print('М',cities[547:610])
    #print('Н',cities[610:691])
    #print('О',cities[691:725])
    #print('П',cities[725:791])
    #print('Р',cities[791:816])
    #print('С',cities[816:934])
    #print('Т',cities[934:981])
    #print('У',cities[981:1011])
    #print('Ф',cities[1011:1018])
    #print('Х',cities[1018:1030])
    #print('Ц',cities[1030:1033])
    #print('Ч',cities[1033:1060])
    #print('Ш',cities[1060:1080])
    #print('Щ',cities[1080:1085])
    #print('Э',cities[1085:1091])
    #print('Ю',cities[1091:1101])
    #print('Я',cities[1101:1113])

    user_input_whole_phrase=update.message.text.capitalize()
    user_input_city=user_input_whole_phrase.replace('/goroda','')
    print('user_input_city',user_input_city)


    length_of_city=len(user_input_city)
    print('length_of_city',length_of_city)

    the_last_letter= user_input_city[length_of_city-1]
    print('the_last_letter',the_last_letter)

    print(len(cities))
    
    if the_last_letter=='а':
        city=cities.pop(random.randint(0,56))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
        print(len(cities))
    elif the_last_letter=='б':
        city=cities.pop(random.randint(56,140))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='в':
        city=cities.pop(random.randint(140,197))
        print(city)
        bot.sendMessage(update.message.chat_id, city)        
    elif the_last_letter=='г':
        city=cities.pop(random.randint(197,235))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='д':
        city=cities.pop(random.randint(235,271))
        print(city)
        bot.sendMessage(update.message.chat_id, city)        
    elif the_last_letter=='е':
        city=cities.pop(random.randint(271,286))
        print(city)
        bot.sendMessage(update.message.chat_id, city)        
    elif the_last_letter=='ж':
        city=cities.pop(random.randint(286,297))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='з':
        city=cities.pop(random.randint(297,328))
        print(city)
        bot.sendMessage(update.message.chat_id, city)        
    elif the_last_letter=='и':
        city=cities.pop(random.randint(328,350))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='й':
        city=cities(350)
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='к':
        city=cities.pop(random.randint(351,508))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='л':
        city=cities.pop(random.randint(508,547))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='м':
        city=cities.pop(random.randint(547,610))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='н':
        city=cities.pop(random.randint(610,691))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='о':
        city=cities.pop(random.randint(691,725))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='п':
        city=cities.pop(random.randint(725,791))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='р':
        city=cities.pop(random.randint(791,816))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='с':
        city=cities.pop(random.randint(816,934))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='т':
        city=cities.pop(random.randint(934,981))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='у':
        city=cities.pop(random.randint(981,1011))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='ф':
        city=cities.pop(random.randint(1011,1018))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='х':
        city=cities.pop(random.randint(1018,1030))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='ц':
        city=cities.pop(random.randint(1030,1033))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='ч':
        city=cities.pop(random.randint(1033,1060))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='ш':
        city=cities.pop(random.randint(1060,1080))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='щ':
        city=cities.pop(random.randint(1080,1085))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='э':
        city=cities.pop(random.randint(1085,1091))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='ю':
        city=cities.pop(random.randint(1091,1101))
        print(city)
        bot.sendMessage(update.message.chat_id, city)
    elif the_last_letter=='я':
        city=cities.pop(random.randint(1101,1113))
        print(city)
        bot.sendMessage(update.message.chat_id, city)        
    else:
        print('Городов на Ы, Ь, Ё итд я не знаю, хорошо,  на этот раз ты победил!')
        bot.sendMessage(update.message.chat_id,text='Городов на Ы, Ь, Ё итд я не знаю, хорошо,  на этот раз ты победил!')
    
def fullmoonoctober_query(bot,update):
    print('Вызван /fullmoonoctober')
    print(type(update.message.text))
    print(update.message.text)

def fullmoonoctober_search(bot,update):
    user_query_fm_oct=update.message.text.lower()
    print('user_query_fm_oct',user_query_fm_oct)
    nearest_fm_oct=ephem.next_full_moon('2016/10/01')
    print('nearest_fm_oct',nearest_fm_oct)
    answer_output_for_bot_format='Полнолуние состоится: {}'.format(nearest_fm_oct)+' '+'Не опаздывайте!'
    bot.sendMessage(update.message.chat_id,answer_output_for_bot_format)

def fullmoon_query(bot,update):
    print('Вызван /fullmoon')
    print(type(update.message.text))
    print(update.message.text)

def fullmoon_search(bot,update):
    user_query_fm=update.message.text.lower()
    print('user_query_fm',user_query_fm)
    nearest_fm_from_today=ephem.next_full_moon(datetime.datetime.now().strftime('%Y/%m/%d'))
    print('nearest_fm_from_today',nearest_fm_from_today)
    answer_output_for_bot_format='Ответ равен: {}'.format(nearest_fm_from_today)+' '+'Не опаздывайте!'
    bot.sendMessage(update.message.chat_id,answer_output_for_bot_format)
    
def copy_get_digit_from_dict(question):
    float_word_digit_dict={
    'один':1,
    'два':2,
    'три':3,
    'четыре':4,
    'пять':5,
    'шесть':6,
    'семь':7,
    'восемь':8,
    'девять':9,
    'десять':10
    }

    print('Поиск цифры в словаре')
    return float_word_digit_dict.get(question,'Странное число, однако')

def float_word_calculator_query(bot,update):
    print('Вызван /floatwordcalculator')
    print(type(update.message.text))
    print(update.message.text)

def float_word_calculator_output(bot,update):
    user_input=update.message.text.lower()
    user_input_only_words=user_input.replace('/floatwordcalculator','')
    print('user_input_only_words',user_input_only_words)
    user_input_split=user_input_only_words.split(' ')
    print('user_input_split',user_input_split)

    first_part1=user_input_split[1]
    second_part1=user_input_split[3]
    print('first_part1',first_part1)
    print('second_part1',second_part1)
    first_part_digit1=get_digit_from_dict(first_part1)
    second_part_digit1=copy_get_digit_from_dict(second_part1)
    print('first_part_digit1',first_part_digit1)
    print('second_part_digit1',second_part_digit1)
    first_part_digit_str1=str(first_part_digit1)
    second_part_digit_str1=str(second_part_digit1)
    result1=first_part_digit_str1+'.'+second_part_digit_str1
    print('result1',result1)


    first_part2=user_input_split[6]
    second_part2=user_input_split[8]
    print('first_part2',first_part2)
    print('second_part2',second_part2)
    first_part_digit2=get_digit_from_dict(first_part2)
    second_part_digit2=copy_get_digit_from_dict(second_part2)
    print('first_part_digit2',first_part_digit2)
    print('second_part_digit2',second_part_digit2)
    first_part_digit_str2=str(first_part_digit2)
    second_part_digit_str2=str(second_part_digit2)
    result2=first_part_digit_str2+'.'+second_part_digit_str2
    print('result2',result2)

    

    if user_input_split[4]=='умножить':
        send_to_user=float(result1)*float(result2)
        print('send_to_user',send_to_user)
        send_to_user_for_bot_format='Ответ равен: {}'.format(send_to_user)
        bot.sendMessage(update.message.chat_id,send_to_user_for_bot_format)       

    elif user_input_split[4]=='разделить':
        send_to_user=float(result1)/float(result2)
        print('send_to_user',send_to_user)
        send_to_user_for_bot_format='Ответ равен: {}'.format(send_to_user)
        bot.sendMessage(update.message.chat_id,send_to_user_for_bot_format)

    elif user_input_split[4]=='сложить':
        send_to_user=float(result1)+float(result2)
        print('send_to_user',send_to_user)
        send_to_user_for_bot_format='Ответ равен: {}'.format(send_to_user)
        bot.sendMessage(update.message.chat_id,send_to_user_for_bot_format)       

    elif user_input_split[4]=='вычесть':
        send_to_user=float(result1)-float(result2)
        print('send_to_user',send_to_user)
        send_to_user_for_bot_format='Ответ равен: {}'.format(send_to_user)
        bot.sendMessage(update.message.chat_id,send_to_user_for_bot_format)

    else:
        bot.sendMessage(update.message.chat_id,text='Неподдерживаемый формат операции')

def word_calculator_query(bot,update):
    print('Вызван /wordcalculator')
    print(type(update.message.text))
    print(update.message.text)

def get_digit_from_dict(question):
    word_digit_dict={
    'один':1,
    'два':2,
    'три':3,
    'четыре':4,
    'пять':5,
    'шесть':6,
    'семь':7,
    'восемь':8,
    'девять':9,
    'десять':10
    }

    print('Поиск цифры в словаре')
    return word_digit_dict.get(question,'Странная цифра')

def word_calculator_output(bot,update):

    user_input_word_example=update.message.text.lower()
    user_input_only_words=user_input_word_example.replace('/wordcalculator','')
    print('Пользователь ввёл такой примерчик: ', user_input_only_words) 

    user_input_word_example_split=user_input_only_words.split(' ')
    print('Пользователь ввёл: ', user_input_word_example_split)


    the_first_word=user_input_word_example_split[3]
    print('Первая цифра словом ',the_first_word)
 
    the_first_word_digit=get_digit_from_dict(the_first_word)
    print('Первая цифра числом ', the_first_word_digit)
   

    the_second_word=user_input_word_example_split[5]
    print('Вторая цифра словом ',the_second_word)
 
    the_second_word_digit=get_digit_from_dict(the_second_word)
    print('Вторая цифра числом ', the_second_word_digit)


    
    for indd in user_input_word_example_split:
        if indd=='плюс':
            answer_output=the_first_word_digit+the_second_word_digit
            answer_output_for_bot_format='Ответ равен: {}'.format(answer_output)
            bot.sendMessage(update.message.chat_id,answer_output_for_bot_format)
        if indd=='минус':
            answer_output=the_first_word_digit-the_second_word_digit
            answer_output_for_bot_format='Ответ равен: {}'.format(answer_output)
            bot.sendMessage(update.message.chat_id,answer_output_for_bot_format)
        if indd=='разделить':
            answer_output=the_first_word_digit/the_second_word_digit
            answer_output_for_bot_format='Ответ равен: {}'.format(answer_output)
            bot.sendMessage(update.message.chat_id,answer_output_for_bot_format)
        if indd=='умножить':
            answer_output=the_first_word_digit*the_second_word_digit
            answer_output_for_bot_format='Ответ равен: {}'.format(answer_output)
            bot.sendMessage(update.message.chat_id,answer_output_for_bot_format)
            
def wordcount_query(bot,update):
    print('Вызван /wordcount')
    print(type(update.message.text))
    print(update.message.text)

def word_count(bot,update):
    user_input_phrase=update.message.text
    count_of_words=len(user_input_phrase.split(' '))-1
    print('Пользователь ввёл: ', user_input_phrase.split(' '))
    print('Количество слов в вашей фразе: ', count_of_words)
    answer_to_user='Количество слов в вашей фразе: {}'.format(count_of_words)
    the_last_element_in_user_input=len(user_input_phrase)-1
    if count_of_words==0:
        bot.sendMessage(update.message.chat_id, text='Вы ввели пустую строку, ай-яй-яй!" ", пожалуйста!')
    elif user_input_phrase[11]!='"' and  user_input_phrase[the_last_element_in_user_input]!='"':
        bot.sendMessage(update.message.chat_id, text='Введите фразу в кавычках: " ", пожалуйста!')
    else:
        bot.sendMessage(update.message.chat_id, answer_to_user)


    



def calculator_query(bot,update):
    print('Вызван /calculator')
    print(type(update.message.text))
    print(update.message.text)

def calculator_output(bot,update):

    user_input_calculator=update.message.text
    user_input_only_digits=user_input_calculator.replace('/calculator','')
    print('user_input', user_input_only_digits)
    
    find_eq=user_input_only_digits.find('=')
    print('find_eq', find_eq)

    find_plus=user_input_only_digits.find('+')
    print('find_plus', find_plus)
    find_minus=user_input_only_digits.find('-')
    print('find_minus', find_minus)
    find_multiplier=user_input_only_digits.find('*')
    print('find_multiplier', find_multiplier)
    find_divider=user_input_only_digits.find('/')
    print('find_divider', find_divider)   
    

    if find_plus>0:
        the_first_digit=user_input_only_digits[1:find_plus]
        the_second_digit=user_input_only_digits[(find_plus+1):find_eq]
        print('the_first_digit', the_first_digit)
        print('the_second_digit', the_second_digit)
        if the_first_digit=='' or the_second_digit=='':
            bot.sendMessage(update.message.chat_id,text='Почему только одно число?')
        else:
            answer_example=int(the_first_digit)+int(the_second_digit)
            answer_example_for_bot_format='Ответ равен: {}'.format(answer_example)
            bot.sendMessage(update.message.chat_id,answer_example_for_bot_format)
    elif find_minus>0:
        the_first_digit=user_input_only_digits[1:find_minus]
        the_second_digit=user_input_only_digits[(find_minus+1):find_eq]
        print('the_first_digit', the_first_digit)
        print('the_second_digit', the_second_digit)
        if the_first_digit=='' or the_second_digit=='':
            bot.sendMessage(update.message.chat_id,text='Почему только одно число?')
        else:
            answer_example=int(the_first_digit)-int(the_second_digit)
            answer_example_for_bot_format='Ответ равен: {}'.format(answer_example)
            bot.sendMessage(update.message.chat_id,answer_example_for_bot_format)
    elif find_multiplier>0:
        the_first_digit=user_input_only_digits[1:find_multiplier]
        the_second_digit=user_input_only_digits[(find_multiplier+1):find_eq]
        print('the_first_digit', the_first_digit)
        print('the_second_digit', the_second_digit)
        if the_first_digit=='' or the_second_digit=='':
            bot.sendMessage(update.message.chat_id,text='Почему только одно число?')
        else:
            answer_example=int(the_first_digit)*int(the_second_digit)
            answer_example_for_bot_format='Ответ равен: {}'.format(answer_example)
            bot.sendMessage(update.message.chat_id,answer_example_for_bot_format)
    elif find_divider>0:
        the_first_digit=user_input_only_digits[1:find_divider]
        the_second_digit=user_input_only_digits[(find_divider+1):find_eq]
        print('the_first_digit', the_first_digit)
        print('the_second_digit', the_second_digit)
        if the_first_digit=='' or the_second_digit=='':
            bot.sendMessage(update.message.chat_id,text='Почему только одно число?')
        elif int(the_second_digit)==0:
            bot.sendMessage(update.message.chat_id,text='Увы и Ах! Делить на ноль нельзя! Пересмотрите свой запрос!')
        else:
            answer_example=int(the_first_digit)/int(the_second_digit)
            answer_example_for_bot_format='Ответ равен: {}'.format(answer_example)
            bot.sendMessage(update.message.chat_id,answer_example_for_bot_format)
    else:
        bot.sendMessage(update.message.chat_id,text='Что же вы ничего не ввели? Попробуйте еще раз!')
    
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
    dp.add_handler(CommandHandler("goroda", goroda_search))
    dp.add_handler(CommandHandler("fullmoonoctober", fullmoonoctober_search))
    dp.add_handler(CommandHandler("fullmoon", fullmoon_search))
    dp.add_handler(CommandHandler("floatwordcalculator", float_word_calculator_output))
    dp.add_handler(CommandHandler("wordcalculator", word_calculator_output))
    dp.add_handler(CommandHandler("calculator", calculator_output))
    dp.add_handler(CommandHandler("wordcount", word_count))
    dp.add_handler(CommandHandler("planet", planet_search))
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()