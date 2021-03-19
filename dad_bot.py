#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.


import logging
import re
import os
import json
import random
import sys

from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# PORT = int(os.environ.get('PORT', '443'))

def dad_reply(update, context):

    text = update.message.text
    text2 = re.sub('[^A-Za-z0-9]+', ' ', text.lower())
    words = text.lower().split()

    for i in range(len(words)):
        words[i] = re.sub('[^A-Za-z0-9]+', ' ', words[i])

    # function one: 'hi {}, im dad' 

    if "im dad" in text.lower().strip() or "i'm dad" in text.lower().strip():
        update.message.reply_text("No you're not, I'm Dad.")

    elif "im" in words:
        subindex = text2.index("im")
        identity = text[subindex + 2:]
        update.message.reply_text("Hi" + identity + ", I'm Dad!")

    elif "i m" in words:
        subindex = text2.index("i m")
        identity = text[subindex + 3:]
        update.message.reply_text("Hi" + identity + ", I'm Dad!")

    elif "i" in words and "am" in words:
        subindex = text.index("am")
        identity = text[subindex + 2:]
        update.message.reply_text("Hi" + identity + ", I'm Dad!")

    # function 2: dad responds to someone calling him/saying hi or bye

    dad_greetings = text.lower().strip()

    if dad_greetings == "dad":
        update.message.reply_text("Simi daiji? I busy you know.")

    elif dad_greetings == "hi dad" or dad_greetings == "hello dad":
        update.message.reply_text("Sorry ah, laopei busy, go entertain yourself first.")

    elif dad_greetings == "bye dad":
        update.message.reply_text("Ok come home by 10pm ah.")

    # function 3: dad responds to rude messages

    shut_up_text = ["shutup", "stfu", "shutthefuckup", "shaddup", "fucku", "fuckyou", "fuk", "fuku", "fukyou", "fuck", "fku", "fk", "fkyou", "fak", "fok", "wtf", "bij", "bitch", "stoopid", "stoopood", "dumbass", "fck"]

    text3 = re.sub('[^A-Za-z0-9]+', '', text.lower())

    for variation in shut_up_text:
        if variation in text3:
            update.message.reply_text("Listen here " + update.message.from_user['first_name'] + ", I will not tolerate any vulgarities being said in this chat, so take your own advice and close thine mouth in the name of the christian minecraft server owner.")

    # special for felice

    if update.message.from_user['username'].lower() == "feliceho":
        if "fork" in text3:
            update.message.reply_text("Listen here " + update.message.from_user['first_name'] + ", I will not tolerate any vulgarities being said in this chat, so take your own advice and close thine mouth in the name of the christian minecraft server owner.")

    # function 4: "u winnin son"

    playsub1 = "play"
    playsub3 = "playin"

    print(text3)
    
    if playsub3 in text3:
        update.message.reply_text("Are ya winnin' son?")
    
    elif playsub1 in text3:
        update.message.reply_text("I hope ya win, son!")

def dad_joke(update, context):
    print("dad joke triggered")

    try:
        joke_files = ["reddit_jokes", "stupidstuff", "wocka"]
        random_file = random.randint(0, len(joke_files))
        file_directory = os.path.join(sys.path[0], 'joke-dataset/' + joke_files[random_file] +'.json')
        print(file_directory)
        joke_file = open(file_directory, "r")

        jokes = json.load(joke_file)
        random_joke = random.randint(0, len(jokes))

        if random_file == 0:
            joke = jokes[random_joke]['title'] + "\n" + jokes[random_joke]['body']

        elif random_file == 1:
            joke = jokes[random_joke]['body']

        elif random_file == 2:
            joke = jokes[random_joke]['body']

        print(joke)
        
        context.bot.send_message(chat_id=update.effective_chat.id, text=joke)

        joke_file.close()

    except Exception as e:
        print(e)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """start the bot"""

    updater = Updater("1602009491:AAFoJFTDd3t5IL2KiRLr7S_Y0Ddn8nal65E", use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('dadjoke', dad_joke))
    dp.add_handler(MessageHandler(Filters.text, dad_reply))

    # log all errors
    dp.add_error_handler(error)

    print("Running...")
    # Start the Bot
    """ updater.start_webhook(listen="0.0.0.0", port=PORT, url_path="1602009491:AAFoJFTDd3t5IL2KiRLr7S_Y0Ddn8nal65E")

    # updater.bot.set_webhook(url=settings.WEBHOOK_URL)
    updater.bot.set_webhook("https://stupid-dad-bot.herokuapp.com/" + "1602009491:AAFoJFTDd3t5IL2KiRLr7S_Y0Ddn8nal65E") """

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
