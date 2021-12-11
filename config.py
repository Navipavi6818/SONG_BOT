import os
from os import environ
from youtube_dl import YoutubeDL

class Config:
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

