import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Kennedy Music")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/18d25616d9883400af112.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/8008bce98aa5c60f9b37a.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/8008bce98aa5c60f9b37a.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/8008bce98aa5c60f9b37a.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "rio1robot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "riohelper")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "riogroupsupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "riobotsupport")
OWNER_NAME = getenv("OWNER_NAME", "riio00") # isi dengan username kamu tanpa simbol @
DEV_NAME = getenv("DEV_NAME", "riio00")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
