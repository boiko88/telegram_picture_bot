from datetime import datetime
import telepot
import random
import api as key

bot = telepot.Bot(key.my_bot_api_key)

def response_function(input_text):
    user_message = str(input_text).lower()
    
    if user_message in ("hello", "hi", "how are you?"):
        return "Hey! How is it going?"
    
    if user_message in ("who are you?", "who are you"):
        return "I am an expense wallet bot"
    
    if user_message in ("add water"):
        return "How much water did you consume last month?"
            
    
    if user_message in ("time", "time?", "what is the time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S:")
        
        return str(date_time)
        
    if user_message in ("stoppy"):
        
        return "the bot stops working!"
        # x = 2 + "2"
        # print(x)
    if user_message in ("corgi", "dog"):
        
        
        
        random_number = random.randint(1,8)

        if random_number == 1:
            bot.sendPhoto(385140930, photo=open('images/corgi1.jpg', 'rb'))
        if random_number == 2:
            bot.sendPhoto(385140930, photo=open('images/corgi2.jpg', 'rb'))
        if random_number == 3:
            bot.sendPhoto(385140930, photo=open('images/corgi3.jpg', 'rb'))
        if random_number == 4:
            bot.sendPhoto(385140930, photo=open('images/corgi4.jpg', 'rb'))
        if random_number == 5:
            bot.sendPhoto(385140930, photo=open('images/corgi5.jpg', 'rb'))
        if random_number == 6:
            bot.sendPhoto(385140930, photo=open('images/corgi6.jpg', 'rb'))
        if random_number == 7:
            bot.sendPhoto(385140930, photo=open('images/corgi7.jpg', 'rb'))
        if random_number == 8:
            bot.sendPhoto(385140930, photo=open('images/corgi8.jpg', 'rb'))
        
        
    
        
    
