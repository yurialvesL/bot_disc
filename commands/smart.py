from discord.ext import commands


class Smart(commands.Cog):
    """ Talks with user """
    def __init__(self,bot):
        self.bot=bot

    @commands.command(name='calcular', help="mostra o resultado de uma conta que você deseja fazer")
    async def calculate_expression(self,ctx, *expression):
        expression = ''.join(expression)
        response = eval(expression)


def setup(bot):
    bot.add_cog(Smart(bot))
