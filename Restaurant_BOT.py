import telebot

# Replace 'YOUR_API_KEY' with your actual Telegram Bot API key
bot = telebot.TeleBot('7343138212:AAGS-vgfTu3cDgxIX_G2L25cpg7oTVgSYYY')

# Dictionary to store reservations and feedback
reservations = {}
feedbacks = {}

# Sample Menu with prices in INR
menu = """
Welcome to Our Chinnari Restaurant!!!

Starters:
1. Caesar Salad - ₹738
   Fresh romaine lettuce, parmesan cheese, croutons, and Caesar dressing.

2. Tomato Soup - ₹573
   Creamy tomato soup with a hint of basil.

3. Garlic Bread - ₹409
   Warm, crispy garlic bread with a buttery finish.

4. Paneer Tikka - ₹140
   Grilled marinated paneer cubes served with bell peppers and onions.

5. Aloo Tikki - ₹80
   Crispy potato patties served with mint chutney.

6. Hara Bhara Kabab - ₹100
   Spinach and green pea patties, served with a tangy dip.

Main Courses:
1. Grilled Salmon - ₹1557
   Fresh salmon fillet grilled to perfection, served with steamed vegetables and rice.

2. Ribeye Steak - ₹1885
   Juicy ribeye steak cooked to your preference, served with mashed potatoes and asparagus.

3. Vegetarian Pasta - ₹1229
   Penne pasta with a medley of fresh vegetables, tossed in a rich marinara sauce.

4. Grilled Chicken Breast - ₹500
   Tender chicken breast marinated in herbs and spices, grilled to perfection, and served with a side of steamed vegetables and mashed potatoes.

5. Vegetable Biryani - ₹400
   Fragrant basmati rice cooked with assorted vegetables, spices, and herbs, served with raita (yogurt sauce) and salad.

6. Paneer Butter Masala - ₹350
   Soft paneer cubes cooked in a rich and creamy tomato-based gravy with butter and aromatic spices, served with naan or rice.

Desserts:
1. Chocolate Lava Cake - ₹655
   Warm chocolate cake with a gooey molten center, served with vanilla ice cream.

2. Cheesecake - ₹573
   Classic New York-style cheesecake with a graham cracker crust.

3. Fruit Salad - ₹491
   Fresh seasonal fruits served with a light honey dressing.

4. Cupcakes - ₹80
   Fluffy cupcakes with your choice of vanilla or chocolate flavor, topped with simple icing.

5. Ice Cream - ₹60 per scoop
   Creamy ice cream available in vanilla, chocolate, and strawberry flavors.

6. Brownies - ₹90
   Rich and fudgy brownies, freshly baked and cut into generous squares.

Beverages:
1. Coffee - ₹246
   Freshly brewed coffee, regular or decaf.

2. Tea - ₹204
   A selection of herbal, black, and green teas.

3. Soft Drinks - ₹164
   Choose from a variety of sodas and juices.

4. Lemonade - ₹50 - ₹100
   Refreshing and tangy, our classic lemonade is made with freshly squeezed lemons and a hint of sweetness.

5. Iced Tea - ₹60 - ₹120
   Cool off with our iced tea, brewed to perfection and served over ice. Choose from black, green, or herbal varieties.

6. Mojito - ₹80 - ₹180
   Experience a taste of the tropics with our mojito, a refreshing mix of muddled mint, lime, sugar, and soda water.
"""

# Information about the restaurant
about_restaurant = """
Welcome to Our Chinnari Restaurant!

Chinnari restaurant is a haven for food enthusiasts, offering a diverse menu that caters to all tastes. From delicious starters to sumptuous main courses and delightful desserts, we ensure that each dish is crafted with the freshest ingredients and utmost care.

Chinnari Hotel is a modern establishment known for its excellent hospitality and comfortable accommodations. It began operations in 2010, quickly becoming a preferred choice for both business and leisure travelers due to its convenient location and high-quality services.
"""

# Special Dishes
special_dishes = {
    'veg': "Our special vegetarian dish is the 'Vegetarian Pasta' - Penne pasta with a medley of fresh vegetables, tossed in a rich marinara sauce.",
    'non': "Our special non-vegetarian dish is the 'Grilled Salmon' - Fresh salmon fillet grilled to perfection, served with steamed vegetables and rice."
}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to our Chinnari Restaurant Bot! How can I assist you today? Type 'menu' to see our menu, 'contact' for contact info, 'reserve' to make a reservation, 'about' to learn more about us, or ask about our special dishes in 'veg' or 'nonveg'.")

@bot.message_handler(commands=['reserve'])
def reserve_table(message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name
    reservations[chat_id] = {'step': 1, 'user_name': user_name}
    bot.send_message(chat_id, "Please provide the following information:\n1. Date (MM/DD/YYYY)")

@bot.message_handler(commands=['feedback'])
def feedback(message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name
    feedbacks[chat_id] = {'step': 1, 'user_name': user_name}
    bot.send_message(chat_id, "We'd love to hear your feedback! Please rate your experience from 1 to 5 stars.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    if chat_id in reservations:
        process_reservation_step(message)
    elif chat_id in feedbacks:
        process_feedback_step(message)
    else:
        text = message.text.lower()
        if text == 'menu':
            bot.send_message(chat_id, menu)
        elif text == 'contact':
            bot.send_message(chat_id, "For inquiries, please contact us at 9854302310 or Chinnari1234@gmail.com.")
        elif text == 'feedback':
            feedback(message)
        elif text == 'reserve':
            reserve_table(message)
        elif text == 'about':
            bot.send_message(chat_id, about_restaurant)
        elif 'special' in text and 'veg' in text:
            bot.send_message(chat_id, special_dishes['veg'])
        elif 'special' in text and 'non' in text:
            bot.send_message(chat_id, special_dishes['non'])
        elif 'opening hours' in text:
            bot.send_message(chat_id, "Our restaurant is open from 9 AM to 11 PM every day.")
        elif 'location' in text:
            bot.send_message(chat_id, "We are located at Rajahmundry.")
        else:
            bot.send_message(chat_id, "I'm sorry, I didn't understand that. Type 'menu' to see our menu, 'contact' for contact info, 'reserve' to make a reservation, 'about' to learn more about us, or ask about our special dishes in 'veg' or 'nonveg'.")

def process_reservation_step(message):
    chat_id = message.chat.id
    user_name = reservations[chat_id]['user_name']
    step = reservations[chat_id]['step']
    
    if step == 1:
        reservations[chat_id]['date'] = message.text.strip()
        bot.send_message(chat_id, "Got it! Now, please provide the time (HH:MM AM/PM).")
        reservations[chat_id]['step'] = 2
    elif step == 2:
        reservations[chat_id]['time'] = message.text.strip()
        bot.send_message(chat_id, "Great! Finally, how many people will be joining?")
        reservations[chat_id]['step'] = 3
    elif step == 3:
        reservations[chat_id]['people'] = message.text.strip()
        bot.send_message(chat_id, "Your reservation has been confirmed for {} at {} for {} people.".format(
            reservations[chat_id]['date'], reservations[chat_id]['time'], reservations[chat_id]['people']
        ))
        print("Reservation received from {}: Date: {}, Time: {}, People: {}".format(
            user_name, reservations[chat_id]['date'], reservations[chat_id]['time'], reservations[chat_id]['people']
        ))
        del reservations[chat_id]

def process_feedback_step(message):
    chat_id = message.chat.id
    user_name = feedbacks[chat_id]['user_name']
    step = feedbacks[chat_id]['step']
    
    if step == 1:
        feedbacks[chat_id]['rating'] = message.text.strip()
        bot.send_message(chat_id, "Thank you! Please describe your experience in a few words.")
        feedbacks[chat_id]['step'] = 2
    elif step == 2:
        feedbacks[chat_id]['comments'] = message.text.strip()
        bot.send_message(chat_id, "Thank you for your feedback! We appreciate your time.")
        print("Feedback received from {}: {} stars, Comments: {}".format(
            user_name, feedbacks[chat_id]['rating'], feedbacks[chat_id]['comments']
        ))
        del feedbacks[chat_id]

bot.polling()
