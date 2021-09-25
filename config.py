import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Rio Music")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/0f6f8a8a5ad69fe5ecf3d.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/de6ab36d3f56ae2474ad4.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/28a04b865916e23aedde6.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/28a04b865916e23aedde6.jpg")
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
