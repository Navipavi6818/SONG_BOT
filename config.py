import os
from os import environ
from youtube_dl import YoutubeDL

class Config:
API_ID = int(os.environ.get("API_ID", 12345))
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
PICS = environ.get("PICS", "")
