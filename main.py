import json
import subprocess
from pyrogram.types.messages_and_media import message
from pyromod import listen
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import User, Message
import os
import requests
bot = Client(
    "Careerwill",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)
@bot.on_message(filters.command(["start"]))
async def start(bot, update):
       await update.reply_text("Hi i can download PDFs/NOTEs from Careerwill.\n\n")
