# bot.py
import os
import requests
import json
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " ~ " + json_data[0]["a"]
    return quote


def get_jokes():
    response = requests.get("https://v2.jokeapi.dev/joke/Any")
    data = json.loads(response.text)
    joke =  data["setup"]  + "\n " + "\n ~ " + "*" + data["delivery"] + "*"
    return joke


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "$inspire":
        quote = get_quote()
        await message.channel.send(quote)

    if message.content == "$hello":
        await message.channel.send("Hello")

    if message.content == "$help":
        await message.channel.send(
            """
        Commands are 
            $hello
            $inspire
        
        """
        )
    if message.content == "$joke":
        joke = get_jokes()
        await message.channel.send(joke)


client.run(TOKEN)
