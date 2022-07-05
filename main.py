import os
from discord.ext import commands

bot = commands.Bot("*")
token = os.getenv('token_ds_etios')  # aqui vai o token do bot(criei uma variável de ambiente para inserir o token)


def load_cogs(bot):
    bot.load_extension('manager')
    bot.load_extension('tasks.dates')
    for file in os.listdir('commands'):
        if file.endswith('.py'):
            cog = file[:-3]
            bot.load_extension(f'commands.{cog}')


load_cogs(bot)
bot.run(str(token))
