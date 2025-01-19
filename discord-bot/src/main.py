import discord
import os
from discord.ext import tasks, commands
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
USER_ID = int(os.getenv('USER_ID'))
VIDEO_URL = os.getenv('VIDEO_URL')
SEND_DATE = os.getenv('SEND_DATE')  # Format: YYYY-MM-DD

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@tasks.loop(hours=24)
async def send_video():
    now = datetime.now()
    if now.strftime('%Y-%m-%d') == SEND_DATE:
        user = await bot.fetch_user(USER_ID)
        await user.send(VIDEO_URL)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    send_video.start()

bot.run(TOKEN)