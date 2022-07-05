from discord.ext import commands
import discord


class Talks(commands.Cog):
    """ Talks with user """
    def __init__(self,bot):
        self.bot=bot

    # *oi chama a função abaixo e ao invés do  @bot.command vira @commands.command
    @commands.command( name='oi', help='Dá um oi')
    async def speak_hello(self,ctx):
        name = ctx.author.name

        response = 'Ola,' + name

        await ctx.send(response)

    # Função abaixo manda mensagem ao PV da pessoa e ao invés do  @bot.command vira @commands.command
    @commands.command(name='segredo', help='')
    async def secret(self,ctx):
        try:
            await ctx.author.send('Me segue na Twitch: twitch.tv'
                                  '/colddemoon')

        except discord.error.Forbidden:
            await  ctx.send('Caso não tenha chegado o segredo é porquê você desabilitou o recebimento'
                            'de mensagens de qualquer pessoa do servidor, ative-as em: (opções > Privacidade) ')

def setup(bot):
    bot.add_cog(Talks(bot))
