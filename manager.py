
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound



class Manager(commands.Cog):
    """ Manage the bot """
    def __init__(self,bot):
        self.bot=bot



    # Ao invés de @bot.event fica commands.Cog.lister()
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'estou pronto e conectado como {self.bot.user}')



    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot.user:
            return
        if 'palavrão' in message.content:
            await message.channel.send(f'Por favor, {message.author.name}, não ofenda os demais usuários')

            await message.delete()





    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.send('Favor enviar todos os Argumentos')

        if isinstance(error,CommandNotFound):
            await ctx.send('O comando não existe. Digite *help para ver todos os comandos')

        else:
            raise error


def setup(bot):
    bot.add_cog(Manager(bot))