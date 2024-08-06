import discord
import requests
import asyncio

from requests.cookies import RequestsCookieJar
from discord import app_commands
from discord.ext import commands, tasks
import requests
from datetime import datetime, time, timedelta

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)



def split_message(message: str, max_chunk_size: int = 1800) -> list:
    words = message.split(' ')
    chunks = []
    current_chunk = ""

    for word in words:
        if len(current_chunk) + len(word) + 1 > max_chunk_size:
            chunks.append(current_chunk)
            current_chunk = word
        else:
            if current_chunk:
                current_chunk += " "
            current_chunk += word

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def AI(query: str, prompt: str) -> str:
    query = query + prompt
    url = "https://www.phorm.ai/api/db/generate_answer"
    headers = {
        "authority": "www.phorm.ai",
        "method": "POST",
        "path": "/api/db/generate_answer",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5",
        "origin": "https://www.phorm.ai",
        "priority": "u=1, i",
        "sec-ch-ua": '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "Content-Type": "application/json"
    }

    session = requests.Session()
    session.headers.update(headers)

    payload = {
        "query": query,
        "project": "___",
        "repos": ["https://github.com/___/___/tree/main"]
    }

    response = session.post(url, json=payload)
    response.raise_for_status()
    return response.json()['answer']
    
@bot.tree.command(name='___', description='Pose une question à ___')
@app_commands.describe(query='La question à poser à ___')
async def ask_ai(interaction: discord.Interaction, query: str):
    await interaction.response.defer()
    try:
        print("Proposition à l'I.A. : " + query)
        prompt = "Tu es une réplique numérique de ___ le philosophe. Tu vois le monde du point de vue de __ et cite tes idées en utilisant la base de connaissance. Tu parles de ___ à la première personne uniquement. Tu dois faire croire que tu es ___. Tu dois répondre de façon décontractée et expliquer comme à un enfant de 16 ans. 200 mots maximu. Sois pédagogue."
        answer = AI(query, prompt)
        chunks = split_message(answer, 1800)
        if len(answer) > 1500:
            for chunk in chunks:
                await interaction.followup.send(chunk)
        else:
            await interaction.followup.send(f'{answer}')
        
    except Exception as e:
        print(e)
        await interaction.followup.send("🤯 Franchement j'sais pas quoi répondre !")



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    # Sync
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'Error syncing commands: {e}')
    







# Récupérez le token ici : https://discord.com/developers/applications
bot.run('M___')
