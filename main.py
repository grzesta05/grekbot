import os
import discord
import requests
from discord.ext import commands

bot = commands.Bot(command_prefix="rip ")
key = os.environ['key']
@bot.event
async def on_ready():
  print("lessgo")
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = "every step you take (prefix `rip`)"))

@bot.command(name = "ping")
async def ping(ctx):
  await ctx.channel.send(f"My ping is {round(bot.latency *1000)} ms which is exactly how much it takes for you to jump off a building")

@bot.command(name = "weather")
async def weather(ctx, city):
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}"
  response = requests.get(url)
  print(response.json())
 
  



    


  
  


bot.run(os.environ['token'])