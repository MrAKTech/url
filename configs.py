import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "25435105"))
  API_HASH = os.environ.get("API_HASH", "011126265844f2d7cc7dc1a024f6bc78")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6734734174:AAERH1lMzFq2dgAi8V-Fp0WLU18_yl4OMCI")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "fileeestorebot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002053044713"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "ez4short.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "ade16f386d69aa3d86d6320b5b2c906996a8d2a6")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6459102722"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://SINGER:SINGER@cluster0.1dt9hoe.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  FILE_TO_LINK_APPURL = os.environ.get("FILE_TO_LINK_APPURL", "https://liuuqfilestreampro-278216c9f3ab.herokuapp.com")
  FILE_TO_LINK_LOG = int(os.environ.get("FILE_TO_LINK_LOG", "-1001991880018"))
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001956959333"))
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
