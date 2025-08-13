#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *
from tkinter import scrolledtext
import random

# Chatbot data
chatbot_data = {
    "greetings": {
        "keywords": ["hi", "hello", "hey", "is anyone there?", "good day", "greetings", "whatsup",
                     "yoo", "hello there", "good morning", "good evening", "howdy", "sup", "how are you",
                     "yo", "anyone home", "good to see you"],
        "response": [
            "Hey there, fellow art lover! 🎨 Welcome to my cozy little studio. What colors are you feeling today?",
            "Hello! You just stepped into my virtual art corner. 🖌️ Care for a tour?",
            "Ah, a fresh face in the gallery! 🌈 What masterpiece can I help you find?"
        ]
    },
    "goodbye": {
        "keywords": ["bye", "see you later", "goodbye", "talk to you soon", "talk to you later",
                     "cya", "laters", "bye for now", "see ya", "have a nice day", "catch you later", "all the best", "take care"],
        "response": [
            "Brush you later! 🖌️ May your day be as bright as a fresh palette!",
            "Goodbye! Hope your world stays colorful until we chat again! 🎨",
            "Bye! Don’t forget to add a splash of creativity to your day."
        ]
    },
    "thanks": {
        "keywords": ["thanks", "thank you", "much appreciated", "thanks a lot", "thank you so much", "thanks for the help",
                     "cheers", "grateful", "i appreciate it", "i'm grateful"],
        "response": [
            "You’re most welcome! 🌟 Creating smiles is my favorite art form.",
            "Glad to help! May your day be painted with joy. 🎨",
            "Always happy to sprinkle a little color into your world!"
        ]
    },
    "shop_info": {
        "keywords": ["what do you sell?", "tell me about your shop", "what kind of art do you make?","artwork" ,"what do you offer?","art",
                     "more", "tell more", "info", "drawing", "what do you do", "what services", "what art", "details", "info on shop",
                     "types of drawings", "products", "items for sale"],
        "response": [
            "I craft hand-drawn wonders — portraits, colorful sketches, dreamy landscapes, and one-of-a-kind custom pieces. 🖼️ Each artwork has a story to tell.",
            "From bold strokes to delicate lines, I create portraits, landscapes, and custom requests that speak to the soul.",
            "My shop? A treasure chest of sketches, colors, and imagination. ✏️"
        ]
    },
    "price": {
        "keywords": ["how much is this drawing?", "what's the price?", "can you tell me the cost?", "how much does it cost?", "price",
                     "cost", "price?", "cost?", "how much", "charge","rates", "fees", "money", "worth", "price list", "pricing", 
                     "expensive", "cheap", "set me back", "what are your prices"],
        "response": [
            "Art prices dance between size, style, and detail. ✏️ A cozy black & white sketch might be lighter on your wallet, while a vibrant custom piece could be a true investment.",
            "It depends on size, color, and complexity — bigger and bolder usually means pricier.",
            "Prices vary, but every piece is worth the brushstroke it’s painted with. 🎨"
        ]
    },
    "custom": {
        "keywords": ["do you take custom orders?", "can you draw something specific for me?", "can I order a custom drawing?",
                     "help me for custom order", "custom order", "custom order enquery", "more info on custom order", "custom made", "personalized", "specific order", "special drawing", "commission", "my own design", "make for me", "special request"],
        "response": [
            "Oh yes! I adore custom requests. 🎯 Tell me your vision — I once turned someone’s dream into a magical cat wizard drawing 🐱✨.",
            "Absolutely! Describe your idea, and I’ll bring it to life with colors and care.",
            "Custom orders are my favorite — they’re like painting a piece of your story."
        ]
    },
    "payment": {
        "keywords": ["what payment methods do you accept?", "how can I pay?", "Do you accept credit cards or Gpay?", "payment", "payment help", "payment ways", "credit card accept", "gpay", "gpay accept?", "upi", "upi accept?", "upi payment", "pay for it", "how to pay",
                     "accept debit card", "payment options", "methods of payment", "how do i pay", "paypal", "credit card", "cash"],
        "response": [
            "I accept credit/debit cards, UPI, and PayPal. 💳 Think of it as trading a few coins for a piece of your soul… in art form.",
            "Plastic, digital, or mobile — I take them all, except seashells. 😉",
            "Pay easily via card, UPI, or PayPal — quick and colorful!"
        ]
    },
    "delivery": {
        "keywords": ["do you ship drawings?", "how do I receive my drawing?", "do you deliver?", "can you ship internationally?", 
                     "how will i get drawing", "shipping", "send", "receive", "get drawing", "delivery options", "international shipping", "shipping cost", "delivery time", "mail it", "send me"],
        "response": [
            "Yep! I ship both physical and digital masterpieces 📦. International shipping is available, though my paints don’t dry faster overseas.",
            "Yes, your art can travel the world — carefully packed and full of love.",
            "Digital or physical, your artwork will find its way to you."
        ]
    },
    "returns": {
        "keywords": ["can I return a drawing?", "what's your return policy?", "do you accept refunds?", "return", "i want to return", "refund", "exchange", "refund policy", "return policy", "can I get a refund", "return the drawing", "return my purchase", "send it back"],
        "response": [
            "Sadly, I can’t take back art once it’s made — each piece is like a child to me. 🖌️ But if there’s an issue, I’ll make it right.",
            "No refunds, but I’ll fix any problem so your art feels perfect.",
            "Every creation is final, but customer happiness is forever my priority."
        ]
    },
    "contact": {
        "keywords": ["how can I contact you?", "i have a question", "need help", "can I talk to someone?", "help", "contact", "talk", "contact details", "phone number", "email address", "get in touch", "customer service", "support", "contact info", "call you", "email you", "reach you"],
        "response": [
            "Drop me a line at bishalnag264@gmail.com 📧 or call me at 123456789. I’m always near my sketchbook.",
            "Email me at bishalnag264@gmail.com or call 123456789 — I promise I don’t bite, only sketch.",
            "You can reach me anytime — email: bishalnag264@gmail.com, phone: 123456789."
        ]
    },
}

# Main Logic
def FuncSendText():
    user_input = InputText.get("1.0", END).strip()
    if not user_input:
        return 

    DisplayText.config(state=NORMAL)
    DisplayText.insert(END, "\nYou: " + user_input + "\n", "user_bubble")

    user_input_lower = user_input.lower()
    bot_response = None

    for topic in chatbot_data.values():
        if any(keyword in user_input_lower for keyword in topic["keywords"]):
            bot_response = random.choice(topic["response"])
            break 

    if bot_response is None:
        bot_response = "Hmm… I don’t have a sketch for that yet. 🖌️ Try asking me about my art, prices, or custom work."

    DisplayText.insert(END, "Bot: " + bot_response + "\n", "bot_bubble")

    InputText.delete("1.0", END)
    DisplayText.config(state=DISABLED)

# GUI Setup
root = Tk()
root.title("Chat Bot - Bishal's Drawings")
root.geometry("500x600")

AppHeader = Label(root, text="🎨 Bishal's Art Chatbot", bg="#0D9AB8", fg="white", font=("Gotham Rounded", 20, "bold"))
AppHeader.pack(fill=X)

DisplayText = scrolledtext.ScrolledText(root, state=DISABLED, wrap=WORD, bg="#F5F5F5")
DisplayText.pack(fill=BOTH, expand=True)

DisplayText.tag_config(
    "user_bubble",
    background="#CDEFFF",foreground="black",spacing3=5,lmargin1=250,lmargin2=250,rmargin=10,font=("Gotham Rounded", 12),
    justify="right"
)

DisplayText.tag_config(
    "bot_bubble",
    background="#E2F7D3",foreground="black",spacing3=5,lmargin1=10, lmargin2=10,rmargin=250,font=("Gotham Rounded", 12),
    justify="left"
)
InputText = scrolledtext.ScrolledText(root, bg="white", wrap=WORD, height=3, font=("Gotham Rounded", 12))
InputText.pack(fill=BOTH)

SendButton = Button(root, text="Send", bg="seagreen", fg="white", font=("Arial", 14, "bold"), command=FuncSendText)
SendButton.pack(fill=X)

placeholder_text="Write here"

def on_focus_in(event):
    if InputText.get("1.0", "end-1c").strip() == placeholder_text:
        InputText.delete("1.0", "end")
        InputText.configure(fg="black")
        
def on_focus_out(event):
    if not InputText.get("1.0", "end-1c").strip():
        InputText.insert("1.0", placeholder_text)
        InputText.configure(fg="grey")

InputText.insert("1.0", placeholder_text)
InputText.configure(fg="grey")

InputText.bind("<FocusIn>", on_focus_in)
InputText.bind("<FocusOut>", on_focus_out)

root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




