import os
from dotenv import load_dotenv

load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
OWNER_ID = int(os.getenv('OWNER_ID', '0'))

# Database Configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite+aiosqlite:///data/bot.db') 
MONGO_URL = os.getenv("MONGO_URL", "link mongo")

# Subscription Settings
DEFAULT_SUBSCRIPTION_DAYS = 30
NOTIFICATION_DAYS_BEFORE_EXPIRY = 3

# Bot Settings
MAX_FILE_SIZE = 5000 * 1024 * 1024  # 5GB
MAX_FILES_PER_USER = 10000

# Button Configuration
DEFAULT_BUTTONS = [
    {'text': '📁 File Manager', 'callback': 'file_manager'},
    {'text': '👤 Profile', 'callback': 'profile'},
    {'text': '💳 Subscription', 'callback': 'subscription'},
    {'text': '📊 Statistics', 'callback': 'stats'}
]
