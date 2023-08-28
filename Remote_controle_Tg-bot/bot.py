import telebot
import time
from telebot import types
import os
import subprocess




bot=telebot.TeleBot('Your TOKEN')
@bot.message_handler(commands=['start'])
def start(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    brow=types.KeyboardButton('Open browser ')
    id = types.KeyboardButton('Id')
    time = types.KeyboardButton('Time')
    telegram = types.KeyboardButton('Open Telegram')
    steam = types.KeyboardButton('Steam')
    markup.add(brow,telegram,id,time,steam)
    bot.send_message(message.chat.id, 'Choose option', reply_markup=markup)


@bot.message_handler(content_types=[ "sticker", "pinned_message", "photo", "audio"])
def get_user_photo(message):
    bot.send_message(message.chat.id,'Not bad')

@bot.message_handler(content_types=['text'])
def all(message):
    if message.text == 'Close_Telegram':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        brow = types.KeyboardButton('Open browser')
        id = types.KeyboardButton('Id')
        timee = types.KeyboardButton('Time')
        telegram = types.KeyboardButton('Open Telegram')
        steam = types.KeyboardButton('Steam')

        markup.add(brow,telegram,id,timee,steam)



        try:
            program_to_close = "Telegram.exe"
            command = f"taskkill /f /im {program_to_close}"
            os.system(command)
            bot.reply_to(message, "Closing Telegram")
        except Exception as e:
            bot.reply_to(message, f"An error occurred: {e}")
        bot.send_message(message.chat.id, 'Choose option', reply_markup=markup)
    elif message.text=='Price':
        ...








    elif message.text=='Time':
        tm=time.time()
        tim=time.ctime(tm)
        bot.send_message(message.chat.id,f"Your time is: {tim}", parse_mode='html')
    elif message.text=="Id":
        bot.reply_to(message,f" Your id: {message.from_user.id}",parse_mode='html')
    elif message.text=='Youtube':
        chrome_path  = "Path to the brawser.exe"
        youtube_url = "https://www.youtube.com"
        subprocess.run([chrome_path, youtube_url])

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Youtube",url="https://www.youtube.com"))
        bot.send_message(message.chat.id, 'Go to youtube', reply_markup=markup)
    elif message.text=='Instagram':
        chrome_path = "Path to the brawser.exe"
        instagram_url = "https://www.instagram.com/"
        subprocess.run([chrome_path, instagram_url])


        merkup=types.InlineKeyboardMarkup()
        merkup.add((types.InlineKeyboardButton('Instagram',url='https://www.instagram.com')))
        bot.send_message(message.chat.id,'Go to Instagram',reply_markup=merkup)

    elif message.text=='DOTA_2': #Some game for example Dota 2
        try:
            program_path = "Path to your game"
            subprocess.Popen(program_path)
            bot.reply_to(message, "Opening Dota 2...") #Opening your game
        except Exception as e:
            bot.reply_to(message, f"An error occurred: {e}")
    elif message.text=='Open Telegram':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        close = types.KeyboardButton('Close_Telegram')
        markup.add(close)




        try:
            program_path = "Path to the telegram.exe"
            subprocess.Popen(program_path)
            bot.reply_to(message, "Opening Telegram...")
        except Exception as e:
            bot.reply_to(message, f"An error occurred: {e}")
        bot.send_message(message.chat.id, 'Choose option', reply_markup=markup)


    elif message.text=='Steam':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        dota=types.KeyboardButton('DOTA_2')
        close=types.KeyboardButton('Close Steam')
        markup.add(dota,close)





        try:
            program_path = "Path to the steam.exe"
            subprocess.Popen(program_path)
            bot.reply_to(message, "Opening Steam...")
        except Exception as e:
            bot.reply_to(message, f"An error occurred: {e}")
        bot.send_message(message.chat.id, 'Choose option', reply_markup=markup)

    elif message.text=='Close Steam':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        brow = types.KeyboardButton('Open browser')
        id = types.KeyboardButton('Id')
        timee = types.KeyboardButton('Time')


        telegram = types.KeyboardButton('Open Telegram')
        steam = types.KeyboardButton('Steam')

        markup.add(brow,telegram,id,timee,steam)






        try:
            program_to_close ="steam.exe"
            command = f"taskkill /f /im {program_to_close}"
            os.system(command)
            bot.reply_to(message,"Closing browser")
        except Exception as e:
            bot.reply_to(message, f"An error occurred: {e}")
        bot.send_message(message.chat.id, 'Choose option', reply_markup=markup)



    elif message.text=='Open browser':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        website = types.KeyboardButton('Youtube')
        inst = types.KeyboardButton('Instagram')
        close=types.KeyboardButton('Close browser')
        markup.add(website,inst,close)





        try:
            program_path="Path to the brawser.exe"
            subprocess.Popen(program_path)
            bot.reply_to(message,"Opening browser")
        except Exception as e:
            bot.reply_to(message, f"An error occurred: {e}")
        bot.send_message(message.chat.id, 'Choose option', reply_markup=markup)


    elif message.text=='Close browser':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        brow = types.KeyboardButton('Open browser')
        id = types.KeyboardButton('Id')
        timee = types.KeyboardButton('Time')

        telegram = types.KeyboardButton('Open Telegram')
        steam = types.KeyboardButton('Steam')

        markup.add(brow,telegram,id,timee,steam)





        try:
            program_to_close ="chrome.exe"
            command = f"taskkill /f /im {program_to_close}"
            os.system(command)
            bot.reply_to(message,"Closing browser")
        except Exception as e:
            bot.reply_to(message, f"An error occurred: {e}")
        bot.send_message(message.chat.id, 'Choose option', reply_markup=markup)





    elif message.text=='food':
        photo=open('ph.jpeg','rb')
        bot.send_photo(message.chat.id, photo ,parse_mode='html')
    else:
        bot.send_message(message.chat.id,"Sorry i can understand what you mean:",parse_mode='html')


bot.polling(none_stop=True)




