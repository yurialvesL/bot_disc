import datetime
import os
import requests
from time import sleep
import discord
from discord.ext import commands, tasks

bot = commands.Bot("*")
token = os.getenv('token_ds_etios')

@bot.event
async def on_ready():
    print(f'estou pronto e conectado como {bot.user}')
    current_time.start()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'palavrão' in message.content:
        await message.channel.send(f'Por favor, {message.author.name}, não ofenda os demais usuários')

        await message.delete()

    await bot.process_commands(message)


# *oi chama a função abaixo
@bot.command(name='oi')
async def speak_hello(ctx):
    name = ctx.author.name

    response = 'Ola,' + name

    await ctx.send(response)

@bot.command(name='calcular')
async def calculate_expression(ctx,*expression):
    expression = ''.join(expression)
    response = eval(expression)

    await ctx.send('A resposta é:' + str(response))

#Função abaixo pega um dado de um API e mostra no bot(aqui no caso mostra a cotação de uma criptmoeada)
@bot.command()
async def binance(ctx,coin,base):
    try:
        response =  requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")

        data = response.json()
        price = data.get('price')
        if price:
            await ctx.send(f"O valor do par {coin}/{base} é {price}")
        else:
            await ctx.send("Está moeda não existe")
    except Exception as error:
        await ctx.send('Ooops.... Deu algum error!')
        print(error)

#Função abaixo manda mensagem ao PV da pessoa
@bot.command(name='segredo')
async def secret(ctx):
    try:
        await ctx.author.send('Me segue na Twitch: twitch.tv'
                        '/colddemoon')

    except discord.error.Forbidden:
        await  ctx.send('Caso não tenha chegado o segredo é porquê você desabilitou o recebimento'
                        'de mensagens de qualquer pessoa do servidor, ative-as em: (opções > Privacidade) ')

@tasks.loop(hours=3)  # função que executa a um determinada quantidade de tempo
async def current_time():
    now = datetime.datetime.now()

    now = now.strftime("%d/%m/%Y às %H:%M:%S")

    channel = bot.get_channel(981517619486150658)

    await channel.send("Data atual:" + now)


bot.run(str(token))
