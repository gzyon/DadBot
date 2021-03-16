#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.


import logging
import re
import os

from telegram.ext import Updater, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# PORT = int(os.environ.get('PORT', '443'))

def dad_reply(update, context):

    # function one: 'hi {}, im dad' 

    text = update.message.text
    text2 = re.sub('[^A-Za-z0-9]+', ' ', text.lower())
    print(text2)
    words = text.lower().split()

    for word in words:
        word = re.sub('[^A-Za-z0-9]+', ' ', word)

    print(words)

    if "im" in words:
        subindex = text2.index("im")
        identity = text[subindex + 2:]
        print(identity)
        update.message.reply_text("Hi" + identity + ", I'm Dad!")
    elif "i m" in words:
        print("detected")
        subindex = text2.index("i m")
        identity = text[subindex + 3:]
        print(identity)
        update.message.reply_text("Hi" + identity + ", I'm Dad!")

    if "i" in words and "am" in words:
        subindex = text.index("am")
        identity = text[subindex + 2:]
        print(identity)
        update.message.reply_text("Hi" + identity + ", I'm Dad!")

    # message = update.message.text.lower()
    # message = re.sub('[^A-Za-z0-9]+', ' ', message)
    # print(message)
    # imsub1 = "im "
    # imsub4 = " im"
    # imsub2 = "i am"
    # imsub3 = "i m "
    # imsub5 = " i m"
    # dad = "dad"

    # if imsub1 in message or imsub4 in message:
    #     subindex = message.index(imsub1)
    #     identity = message[subindex + 2:]
    #     print(identity)
    #     update.message.reply_text("Hi" + identity + ", I'm Dad!")

    # elif imsub2 in message:
    #     subindex = message.index(imsub2)
    #     identity = message[subindex + 4:]
    #     print(identity)
    #     update.message.reply_text("Hi" + identity + ", I'm Dad!")
    
    # elif imsub3 in message or imsub5 in message:
    #     subindex = message.index(imsub3)
    #     identity = message[subindex + 3:]
    #     print(identity)
    #     update.message.reply_text("Hi" + identity + ", I'm Dad!")
    
    # elif dad in message:
    #     update.message.reply_text("Ya?")

    # message2 = update.message.text.lower()
    # message2 = re.sub('[^A-Za-z0-9]+', '', message2)
    # shutupsub1 = "shutup"
    # shutupsub2 = "stfu"
    # shutupsub3 = "shaddup"
    # shutupsub4 = "shutthefuckup"
    # dad = "imdad"
    # hidad1 = "hidad"
    # hidad2 = "hellodad"
    # byedad = "byedad"
    # if shutupsub1 in message2 or shutupsub2 in message2 or shutupsub3 in message or shutupsub4 in message:
    #     update.message.reply_text("Listen here " + update.message.from_user['first_name'] + ", I will not tolerate you saying the words that consist any variation of the letters 's h u t  u p' being said in this server, so take your own advice and close thine mouth in the name of the christian minecraft server owner.")
    
    # if dad in message2:
    #     update.message.reply_text("No you're not, I'm Dad.")

    # if hidad1 in message2 or hidad2 in message2:
    #     update.message.reply_text("Sorry ah, laopei busy, go entertain yourself first.")
    
    # if byedad in message2:
    #     update.message.reply_text("Ok come home by 10pm ah.")

    # message3 = update.message.text.lower()
    # message3 = re.sub('[^A-Za-z0-9]+', '', message3)
    # playsub1 = "play"
    # playsub2 = "playing"
    # playsub3 = "playin"
    
    # if playsub2 in message3 or playsub3 in message3:
    #     update.message.reply_text("Are ya winnin' son?")
    
    # elif playsub1 in message3:
    #     update.message.reply_text("I hope ya win, son!")

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """start the bot"""

    updater = Updater("1602009491:AAFoJFTDd3t5IL2KiRLr7S_Y0Ddn8nal65E", use_context=True)

    dp = updater.dispatcher

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
