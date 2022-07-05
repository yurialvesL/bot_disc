from discord.ext import commands, tasks
import datetime


class Dates(commands.Cog):
    """ Work with Dates """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()

    @tasks.loop(hours=3)  # função que executa a um determinada quantidade de tempo
    async def current_time(self):
        now = datetime.datetime.now()

        now = now.strftime("%d/%m/%Y às %H:%M:%S")

        channel = self.bot.get_channel(981517619486150658)

        await channel.send("Data atual:" + now)


def setup(bot):
    bot.add_cog(Dates(bot))
