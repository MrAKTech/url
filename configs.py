import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "22225617"))
  API_HASH = os.environ.get("API_HASH", "ef16f7597376f1689663304c954e4493")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7381849410:AAEdcGfp1W41Q5SYAPIavcZ3HHMc7SYk8l8")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "MrAKFileShareBot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001602208028"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "publicearn.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "5f14184b5d330486d0ebcb32127fdca5b03c8b42")
  IS_SHORTLINK = bool(os.environ.get('IS_SHORTLINK', True))
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6072149828"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://akmonsterprogrammer:S.Aruna1155182089@store.sscpbr1.mongodb.net/?retryWrites=true&w=majority&appName=store")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002145921498")
  FILE_TO_LINK_APPURL = os.environ.get("FILE_TO_LINK_APPURL", "https://mraklinkzz-c342d83c238c.herokuapp.com")
  FILE_TO_LINK_LOG = int(os.environ.get("FILE_TO_LINK_LOG", "-1002026821864"))
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001602208028"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))

  
  ABOUT_BOT_TEXT = f"""
 ʜᴇʀᴇ ᴡᴇ ɢᴏ ᴄʜᴇᴄᴋᴏᴜᴛ ᴍʏ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ✔
  
 🚩 ʟᴏᴏᴋ ʙᴇʟᴏᴡ ᴍʏ ꜰʀɪᴇɴᴅ 🚩

▶ ᴍʏ ɴᴀᴍᴇ : ꜰɪʟᴇ ꜱᴛᴏʀᴇ
▶ ꜱᴇʀᴠᴇʀ : ʜᴇʀᴏᴋᴜ

🌿 ɴᴇᴠᴇʀꜰᴏʟᴅ ɴᴇᴠᴇʀ ʙᴀᴄᴋᴅᴏᴡɴ 🌿
"""
  ABOUT_DEV_TEXT = f"""
ᴍʏ ᴅᴇᴠ: [➡](https://telegram.me/badal6667rai)
 
 I am Super noob Please Support My Hard Work. 🐸
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **File Store Bot**.

📢 ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ & ɪᴛ ᴡɪʟʟʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ & ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴛʜᴇ (ꜱʜᴏʀᴛᴇɴᴇᴅ) ꜰɪʟᴇ ʟɪɴᴋ.
"""
