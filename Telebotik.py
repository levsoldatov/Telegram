import Settings
import telebot
import random
from telebot import types
from LogicGame import LogicGame
from Magasin import Magazin
from present import KolesoFortuni
from mybase import mybase
#Использование класса логики игры
base = mybase()

# Активация телеграмм бота
bot = telebot.TeleBot(Settings.ip)
dict_user = {}
my_magazin = Magazin()

# нажатие на кнопку старт
@bot.message_handler(commands = ['start'])
def start(message):
    base.write_base(message.from_user.id)
    markdown = """*_bold and italic_*"""
    bot.send_message(message.chat.id,"Привет {0} \U0001F44B\! Вы играете в игру поле чудес\. По ходу игры вы зарабатываете очки\,которые можете потратить на разные вещи\. А сейчас вращайте барабан\! ".format(message.from_user.first_name),parse_mode='MarkdownV2')
    #if dict_user and message.from_user.id in dict_user:
    #    pass
    #else:
    dict_user[message.from_user.id] = LogicGame()
    print(dict_user)
# появление кнопок управления игрой
@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Вращать барабан \U0001F579")
    #item2 = types.KeyboardButton("Взять награду")
    item3 = types.KeyboardButton("Мои очки \U0001F4B0")
    item4 = types.KeyboardButton("Магазин \U0001F3EA")
    item5 = types.KeyboardButton("Колесо фортуны! \U0001F381")
    item6 = types.KeyboardButton("Мой статус")
    markup.add(item1)
    #markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    markup.add(item5)
    markup.add(item6)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)

#Слушатель событий
@bot.message_handler(content_types=['text'])
def my_answer(message):
    if message.from_user in dict_user:
        print('ok')
    if message.text == "Вращать барабан \U0001F579":
        if base.read_base(message.from_user.id) != 'no':
            dict_user[message.from_user.id] = LogicGame()
            bot.send_message(message.chat.id, dict_user[message.from_user.id].action(str(random.randint(1,9))))
            print(dict)
            
    #elif message.text == "Взять награду":
    elif message.text == "Мои очки \U0001F4B0":
        if base.read_base(message.from_user.id) != 'no':
            bot.send_message(message.chat.id,dict_user[message.from_user.id].get_points())
    elif message.text == "Магазин \U0001F3EA":
        if base.read_base(message.from_user.id) != 'no':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            list_item = []
            for i in range(my_magazin.count_tovars()):
                list_item.append(types.KeyboardButton(my_magazin.dict_tovars[i+1]['name'] + '-' + str(my_magazin.dict_tovars[i+1]['price'])))

            for item in list_item:
                markup.add(item)

            item6 = types.KeyboardButton('Назад \U0001F519')
            markup.add(item6)

            bot.send_message(message.chat.id,str(my_magazin.count_tovars()),reply_markup=markup)

    elif '-' in message.text:
        if base.read_base(message.from_user.id) != 'no':
            list_product = message.text.split('-')
            print(list_product)

            text_tovar = my_magazin.buy_tovar(dict_user[message.from_user.id].get_points(),list_product[0])
            dict_user[message.from_user.id].set_points(my_magazin.get_newmycount())
            dict_user[message.from_user.id].set_stat(my_magazin.get_new_stat())
            my_magazin.set_new_stat()
            print(dict_user[message.from_user.id].get_points())
            bot.send_message(message.chat.id,text_tovar)

    elif message.text == 'Колесо фортуны! \U0001F381':
        if base.read_base(message.from_user.id) != 'no':
            chance = 0
            kf = KolesoFortuni()
            if len(chance) > 1:
                print(chance[0])
                print(chance[1])
                status = chance[1]['stat']
                dict_user[12345].set_stat(status)
                print(dict_user[12345].get_stat())
                new_chance = kf.get_chanse()
                dict_user[12345].set_chanse(new_chance)
                print(dict_user[12345].getchance())
            else:
                new_message = kf.popitka(chance)
                print(new_message)
                print(kf.get_random_predmet())

                print('Колесо фортуны')

                bot.send_message(message.chat.id,'Вы выиграли предмет '+ kf.get_random_predmet()['think']+ ' '+str(kf.get_stat()))

    elif message.text == 'Назад \U0001F519':
        if base.read_base(message.from_user.id) != 'no':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Вращать барабан \U0001F579")
            # item2 = types.KeyboardButton("Взять награду")
            item3 = types.KeyboardButton("Мои очки \U0001F4B0")
            item4 = types.KeyboardButton("Магазин \U0001F3EA")
            item5 = types.KeyboardButton("Колесо фортуны! \U0001F381")
            item6 =types.KeyboardButton("Мой статус")

            markup.add(item1)
            # markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            markup.add(item5)
            markup.add(item6)
            bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)
    elif message.text == "Мой статус":
        if base.read_base(message.from_user.id) != 'no':
            bot.send_message(message.chat.id,dict_user[message.from_user.id].get_stat())

bot.polling(none_stop = True)
