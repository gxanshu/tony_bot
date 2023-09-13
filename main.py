# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all() # Create an instance of Intents
client = discord.Client(intents=intents) #pass the intents

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)