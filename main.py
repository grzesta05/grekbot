import os
import discord
import requests
import json
from discord.ext import commands
import time
pref = "rip "
start = time.time()
bot = commands.Bot(command_prefix=pref)
key = os.environ['key']
@bot.event
async def on_ready():
 
  print("lessgo " + str(start))
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f"every step you take (prefix `{pref}`)"))

@bot.command(name = "ping")
async def ping(ctx):
  now = time.time()
  await ctx.channel.send(f"```My ping is {round(bot.latency *1000)} ms which is exactly how much it takes for you to jump off a building. Running for {round((now-start) / 3600, 2)} h```")

@bot.command(name = "weather")
async def weather(ctx,*,city):
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}"
  response = requests.get(url)

  #url_forecast = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&cnt=5&appid={key}"
  #forecast = requests.get(url_forecast)

 #---photo from a city---
  images_API = requests.get('https://api.teleport.org/api/urban_areas/')
  images_API_text = json.dumps(images_API.json(), sort_keys=True, indent=4)
  foundImage = images_API_text.find(city)
 
 #---sending the photo---
  if foundImage != -1:

    images_API = requests.get(f'https://api.teleport.org/api/urban_areas/slug:{(city.lower()).replace(" ", "-")}/images/')
    images_API_text = json.dumps(images_API.json(), sort_keys=True, indent=4)
    print(images_API_text)
    await ctx.channel.send(images_API.json()["photos"][0]["image"]["mobile"])
 
  #---weather info---
  #text = json.dumps(response.json(), sort_keys=True, indent=4)
  #text = json.dumps(forecast.json(), sort_keys=True, indent=4)
  #print(text)
  description = response.json()["weather"][0]["description"]
  print(description)
  await ctx.channel.send(f'```AsciiDoc\n ***{description} uwu***\n Temperature: {response.json()["main"]["temp"]} *C \n Feels like {response.json()["main"]["feels_like"]} *C \n Day duration: {(response.json()["sys"]["sunset"] - response.json()["sys"]["sunrise"])/ 3600} h```')
 

bot.run(os.environ['token'])