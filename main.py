import discord
from discord.ext import commands
import requests
import random
from logic import TOKEN
from collections import defaultdict

intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

tip = [
        "Drink at least 8 glasses of water a day. 💧",
        "Take a 5-min stretch every hour. 🧘",
        "Get 7-8 hours of sleep. 💤",
        "Eat more fruits and vegetables. 🍎🥦",
        "Take deep breaths to reduce stress. 😌"
    ]

tips = defaultdict(list)

# Event saat bot online
@bot.event
async def on_ready():
    print(f'{bot.user} is online!')

# Command: !ping
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong! 🏓')

# Command: !healthtip
@bot.command(name='healthtip')
async def healthtip(ctx):
    if ctx.author.id not in tips or not tips[ctx.author.id]:
        tips[ctx.author.id] = tip.copy()
    
    choice = random.randint(0, len(tips[ctx.author.id])-1)

    await ctx.send(tips[ctx.author.id].pop(choice))

# Command: !bmi weight height (contoh: !bmi 70 1.75)
@bot.command(name='bmi')
async def bmi(ctx, weight: float, height: float):
    bmi_value = weight / (height * height)
    category = ""
    if bmi_value < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi_value < 25:
        category = "Normal weight"
    elif 25 <= bmi_value < 30:
        category = "Overweight"
    else:
        category = "Obese"
    await ctx.send(f'Your BMI is {bmi_value:.2f} ({category})')

bot.run(TOKEN)
