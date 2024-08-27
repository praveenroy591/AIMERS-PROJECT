import telebot
import google.generativeai as genai
from datetime import datetime

# Configure Google Generative AI API
genai.configure(api_key="AIzaSyCk24LgF1T9VW4fqltn8rubr2wYFFmJpEk")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])

# Initialize Telegram Bot
bot = telebot.TeleBot("7489829095:AAF9Xr3ZCQSgF2peoc1_iumqKPe3r8IfiEk")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! The MOST POWERFUL AI BOT from IndianServers")

@bot.message_handler(func=lambda message: message.text.lower() == 'today time')
def get_current_time(message):
    current_time = datetime.now().strftime("%H:%M:%S")
    bot.reply_to(message, f"Current time: {current_time}")

@bot.message_handler(func=lambda message: message.text.lower() == 'today date')
def get_current_date(message):
    current_date = datetime.now().strftime("%Y-%m-%d")
    bot.reply_to(message, f"Current date: {current_date}")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        print(message)
        response = convo.send_message(message.text)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        bot.reply_to(message, f"{current_time}\n{response.text}")  # Include current time and date in the response
    except Exception as e:
        print(f"An error occurred: {e}")
        bot.reply_to(message, "Sorry, I couldn't process your request.")

bot.polling()
