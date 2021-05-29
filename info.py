import re
from os import environ

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = 1733305
API_HASH = 'f423cffca6b5b7247b31b5b0df61f48d'
BOT_TOKEN = '1838208004:AAFckP950IP9aoaIjYG66JnEfHRMtjkW_hw'

# Bot settings
MAX_RESULTS = 10
CACHE_TIME = 300
USE_CAPTION_FILTER =  False

# Admins, Channels & Users
ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if re.search('^.\d+$', ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if re.search('^\d+$', user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# MongoDB information
DATABASE_URI = 'mongodb+srv://kaj:kaj@cluster0.xyylh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
DATABASE_NAME = 'kaj'
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
START_MSG = """
**Hi, I'm Media Search bot**

Here you can search files in inline mode. Just press following buttons and start searching.
"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
