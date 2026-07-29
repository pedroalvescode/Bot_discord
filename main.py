import discord
import requests
import pyttsx3
from discord.ext import commands 
from deep_translator import GoogleTranslator
from bot_logic import senhaa
from bot_emoji import emojii


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

tradutor_ptbr = GoogleTranslator(source='en', target='pt')

engine = pyttsx3.init() 


def fato_aleatorio():
    url = f' https://uselessfacts.jsph.pl/random.json'
    response = requests.get(url)
    if response.status_code == 200:  
        dados = response.json()
        return dados["text"], dados["permalink"]
    else:
        return "Desculpe, não consegui pegar agora! Tente novamente mais tarde."

def speak(text: str): 
    engine.say(text) 
    engine.runAndWait()  

@bot.event 
async def on_ready(): 
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def olá(ctx):
    await ctx.send(f'Seja bem-vindo {ctx.author.mention} !!')

@bot.command()
async def senha(ctx):
    await ctx.send("Sua senha é " + senhaa(10))

@bot.command()
async def emoji(ctx):
    await ctx.send("Seu emoji é" + emojii())

@bot.command()
async def membros(ctx):
    guild = ctx.guild
    await ctx.send(f'Esse servidor possui {guild.member_count} membros contando comigo!')


@bot.command()
async def fato(ctx):

    fato, link = fato_aleatorio()
    fato_traduzido = tradutor_ptbr.translate(fato)
    await ctx.send(f'FATO ALEATÓRIO: \n{fato_traduzido} \nlink do fato: {link}')
    speak(fato_traduzido)

@bot.command()
async def ajuda(ctx):
    await ctx.send("MEUS COMANDOS: \n!olá - Eu te dou boas vindas \n!senha - Eu crio uma senha de 10 dígitos aleatórios \n!emoji - Eu mando um emoji que te define \n!membros - Eu digo quantos membros tem no server \n!fato - Eu falo um fato aleatório")



bot.run('YOUR TOKEN HERE!! SEU TOKEN AQUI!!')
