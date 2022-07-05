from discord.ext import commands


class Reactions(commands.Cog):
    """ Work with reactions """
    def __init__(self,bot):
        self.bot=bot

    #bot.events ==> commands.Cog.listener()
    @commands.Cog.listener()
    async def on_reaction_add(self,reaction, user):  # Função para executar um ação após o usuário usar um emoji
        print(reaction.emoji)
        if reaction.emoji == "👍":
            role = user.guild.get_role(993213659054624909)
            await user.add_roles(role)


        elif reaction.emoji != "👍":
            role = user.guild.get_role(993214204309934171)
            await user.add_roles(role)


def setup(bot):
    bot.add_cog(Reactions(bot))
