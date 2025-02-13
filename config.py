import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "20817057"))
API_HASH = getenv("API_HASH", "e2530f82f8168f7f4e7b6f68d2e44dc3")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7550267981:AAGR1zRFvwQW1pdroNNQo9kNknMSniYIuiw")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://lelouchinuzuma:ff6hsp0ftlC4gw3F@cluster0.grpk0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002496076514"))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5094606253"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/hutaobest/janedoe69",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/beasts_network")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/beasts_community")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-remmusic-08-14")


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION", "BQE9pKEAKaF9oxZWUqs1hZN4A25hcA1d4jqbVuvWaUArNEx0WO0jpooX-yel1ahgUbwmaiQVS32P9_5F4Tqiu6XyaSOCAY4SxVn6mmNhvAOe2C94P5ZiT5LUFK1A9mL0A3_vszOH9V07CuhNEEmABs60jt91G4i7u1uwraSPCoJh5SLY3Y1AuwPcIXQ1luumNmQQl3mEShkzIszHQj3pVMGmPIwPv3uamkFBMMuMgQTsW0IjWmilb0sH-wyfHTdr_I2Nfb4fW6MQYsB-DLjD34lu6yqZA8Cak8WnNttwKV1rXk4daQIXurrxrQZF76thTuDqvGyfIDU5IBBP8Tbei9XkYozglwAAAAHSV-lIAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/eef212469624b21ac0e8c-fe12be732045808b6f.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/a340875fe416dbcf53cfb-8391390f638b79435f.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/90932024774fb71280082-c0711c0e5a43a9d050.jpg"
STATS_IMG_URL = "https://graph.org/file/add2eefc0e1ce89ebd864-19aaf3cf29ef373e33.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
STREAM_IMG_URL = "https://graph.org/file/6ee562ae03adc65982b67-f349400e9d9b946706.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/c1d824fa94a862872a1dc-499622303672a23b1a.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/1cce27d98efed430e008d-59b5a21ad87bda59aa.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/c1d824fa94a862872a1dc-499622303672a23b1a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/c1d824fa94a862872a1dc-499622303672a23b1a.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/c1d824fa94a862872a1dc-499622303672a23b1a.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
