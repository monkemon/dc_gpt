# main.py
import os
import random

import discord
from discord.ext import commands
from pymongo import MongoClient
from dotenv import load_dotenv
import requests

import utils

load_dotenv()
DC_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DC_GUILD = os.getenv("DISCORD_GUILD")
AI_TOKEN = os.getenv("OPENAI_API_KEY")

if not DC_TOKEN or not AI_TOKEN:
    print("not enough tokens")
    exit(1)

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix="$",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"{bot.user.name} connected")

@bot.command(name="info", brief="Get info about client")
async def command_ping(ctx: commands.Context):
    msg = f"""
    Message info:
    guild = {ctx.guild}
    message = {ctx.message}
    author = {ctx.author}
    """
    await ctx.send(msg)

@bot.command(name="good", brief="make him a good boi")
async def command_good_boi(ctx: commands.Context):
    res = discord.Embed()
    res.color = discord.Colour(utils.get_random_hex_color())
    try:
        author = ctx.author
        msg = f"""
        Thank you so much, great master **{author.display_name}**, AKA the mighty {author.global_name}.
        """
        await ctx.send(msg)
    except Exception as e:
        ctx.send(f"Im sorry :( something went wrong: {str(e)}")

@bot.command(name="ask", brief="Ask chatgpt")
async def command_ai_ask(ctx: commands.Context):
    message = ctx.message
    content = message.clean_content[len("$ask "):]
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type" : "application/json",
        "Authorization": f"Bearer {AI_TOKEN}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role":"user",
                "content":content
            }
        ],
        "temperature": 1.0 
    }
    try:
        resp = requests.post(url=url, headers=headers, json=data)
    except Exception as e:
        ctx.send(f"Im sorry :( something went wrong: {str(e)}")
    
    ans: dict = resp.json()
    total_tokens = ans.get("usage", {}).get("total_tokens", 0)
    model = ans.get("model", "unknown")
    answer = "Non answer (something went probably wrong)"

    choices = ans.get("choices", [])
    for choice in choices:
        answer = choice.get("message", {}).get("content", "No answer")
        break

    msg_answer = f"[tokens: {total_tokens}, model: {model}]\n{answer}"
    await ctx.send(msg_answer)


bot.run(DC_TOKEN)



