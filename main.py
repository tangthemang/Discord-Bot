import discord
import os
import requests
import json
from keep_alive import keep_alive

i = 0
s = ''
numbers = '1234567890'
arithmetic = '+-*/'
var = False
variables = 'qwertyuiopasfghjklzxcvbnm'

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith('$solve'):
      s = message.content[7:]

      for x in s:
        if x in variables:
          var = True
      
      if var == True:
        for x in s:
          if x in variables:
            print(x)
            
      else:
        for x in s:
          if x in arithmetic:
            print(x)
      await message.channel.send(s)

    elif message.content.startswith('$aops'):
        await message.channel.send("Here's a link to the AOPS website")
        await message.channel.send("https://artofproblemsolving.com/community")

    elif message.content.startswith('$physlib'):
        await message.channel.send("Here's the IB data booklet")
        await message.channel.send(
            "https://ibphysicsnotes.files.wordpress.com/2016/01/annotated-physics-data-booklet-2016.pdf"
        )

    elif message.content.startswith('$javadocs'):
        await message.channel.send("Here's a link to the Java docs")
        await message.channel.send(
            "https://docs.oracle.com/javase/7/docs/api/"
        )

    elif message.content.startswith('$cdocs'):
        await message.channel.send("Here's a link to the C++ docs")
        await message.channel.send(
            "https://www.tutorialspoint.com/c_standard_library/index.htm"
        )

    elif message.content.startswith('$pythondocs'):
        await message.channel.send("Here's a link to the Python docs")
        await message.channel.send(
            "https://ibphysicsnotes.files.wordpress.com/2016/01/annotated-physics-data-booklet-2016.pdf"
        )

    elif message.content.startswith('$spam'):     
      if message.author.name=='TangoMango':
        for x in range(100):
          await message.channel.send('@everyone')

keep_alive()
client.run(os.getenv("TOKEN"))
