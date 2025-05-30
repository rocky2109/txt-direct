#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29028535"))
API_HASH = environ.get("API_HASH", "9e501cebfbd5da42d6b74d48a1bf2536")
BOT_TOKEN = environ.get("BOT_TOKEN", "7692540490:AAGOnamVpEAT8QT7dA0SjF4Y-nsxmXgwImU")
OWNER = int(environ.get("OWNER", "5913865424"))
CREDIT = "𝄟⃝‌🐬🇳‌ɪᴋʜɪʟ𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
