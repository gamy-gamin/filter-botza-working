
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1474138123:AAEMYvTM-DistFieVkAbvvbrfElL6D6C_38")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", 2834572))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "1aa8b2e8b291d916d2b9c0dbd0189dc2")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQCsZ-lMkKtGL2e5RKjCmORRzivRWbw0YhH7KhG2nPdwudBDCbSuEGNclG5dnMhqRfDVc8Z1bV5LvUirwACqnO2Id6D9np92MxqrLDLMVdm_et09igjXNK8VTxgO7Ww9eJyMkfbF7tsRyRhFdJzP5V-DxM-n6QmxIxPx_o3BwWUv05dUgjsw0T1cc2cltRXboZsJm5DmjElhubPjjzJHu8OsJCTBlFXHte2-BN720qoLU4fGJSPubk0t-U-W6VV-2iR5B1MIlWokHwZMyN9oqlVhrI-cBEpDuWH9ExcOzd39L2BUp0tpQpETanIakSoIJRNb29HxNkgdZ82lAr4gVus7ZS2DfgA")

# Database URL from https://cloud.mongodb.com/
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Gamy_Gamin:Gamy_Gamin@cluster0.wujnj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Your database name from mongoDB
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# ID of users that can use the bot commands
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1177233175").split())

#Small Admins
SM_ADMIN = set(int(x) for x in os.environ.get("SM_ADMIN", "1398980025").split())

# Should bot search for document files in channels
DOC_SEARCH = os.environ.get("DOC_SEARCH", "yes").lower()

#Should bot search for Images
PHO_SEARCH = os.environ.get("PHO_SEARCH", "yes").lower()

# Should bot search for video files in channels
VID_SEARCH = os.environ.get("VID_SEARCH", "yes").lower()

# Should bot search for music files in channels
MUSIC_SEARCH = os.environ.get("MUSIC_SEARCH", "no").lower()

#Link of the Channel
CHANNEL_LINK = os.environ.get("CHANNEL_LINK", "https://t.me/c/1404974777/")

#Web Site Link
WEB_SITE_URL = os.environ.get("WEB_SITE_URL", "https://www.irupc.net/p/bot.html?")

#text set when User Request Subtitle
SUB_TEXT = os.environ.get("SUB_TEXT", "𝕊𝕦𝕓𝕥𝕚𝕥𝕝𝕖 ❗️ ")

# Link to File bot url before Array
BOT_URL = os.environ.get("BOT_URL", "https://t.me/irupc_sever_bot?start=")

# Admin Support or Not
ADMIN_ALIVE = os.environ.get("ADMIN_ALIVE", "no")

TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
