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
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/923e40935bd93d3e807dc.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/2844a65699ff40af67451.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/2844a65699ff40af67451.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/2844a65699ff40af67451.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "KennedyXRobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "assistantmusicken")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "kenbotsupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "KennedyProject")
OWNER_NAME = getenv("OWNER_NAME", "xgothboi") # isi dengan username kamu tanpa simbol @
DEV_NAME = getenv("DEV_NAME", "xgothboi")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
