import discord
from discord.ext import commands
import json

client = commands.Bot(command_prefix=".")

token_file = open("token.tk", 'r')
token = token_file.read()

@client.event
async def on_ready():
    print("Rodando")

@client.event
async def on_message(message):
    embeds = message.embeds # return list of embeds
    for embed in embeds:
        embedr = embed.to_dict()
        result = json.dumps(embedr) 
  
        # printing result as string
        waifulist = open('waifus.wa', 'r')
        waifusa = waifulist.readlines()
        print(waifusa)

        for waifu in waifusa:
            waifud = waifu.replace("\n", "")
            if waifud.lower() in result.lower():
                print(result)
                await message.add_reaction("💖")

client.run(token, bot=False)
