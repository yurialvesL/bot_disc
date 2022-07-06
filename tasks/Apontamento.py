from discord.ext import commands, tasks
import datetime
from datetime import date

class Friday_note(commands.Cog):
    """ Work with Dates """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.note.start()

    @tasks.loop(hours=7)  # função que executa a um determinada quantidade de tempo
    async def note(self):
        hoje=date.today()
        channel = self.bot.get_channel(981517619486150658)
        if hoje.strftime('%A') == "Friday":
            await channel.send("🔴🔴HOJE É SEXTAAAAA NÃO ESQUEÇA DO APONTAMENTO DO MILTOLA🔴🔴")
        elif hoje.strftime('%A') == "Wednesday":
            await channel.send("🔴🔴FALTAM 2 DIAS PARA O APONTAMENTO DO MILTOLA, NÃO ESQUEÇA🔴🔴")
        elif hoje.strftime('%A') == "Thursday":
            await channel.send("🔴🔴AMANHÃ É O DIA DE MANDAR O APONTAMENTO PARA O MILTOLA, NÃO ESQUEÇA🔴🔴")
        elif hoje.strftime('%A') == "Saturday":
            await channel.send("😀 SABADÃO HOJE, BORA DA UM ROLEZIN?😎😎")
        elif hoje.strftime('%A') == "Sunday":
            await channel.send("😴😴 DOMINGÃO BOM PRA DESCANSAR UM POUQUIN🥱🥱")
        elif hoje.strftime('%A') == "Monday":
            await channel.send("😴😴 SEGUNDONA F, FALTA 4 DIAS PARA O APONTAMENTO DO MILTOLA🥱🥱")
        elif hoje.strftime('%A') == "Tuesday ":
            await channel.send("😉😉 TERÇA F, FALTA 3 DIAS PARA O APONTAMENTO DO MILTOLA🥱🥱")

def setup(bot):
    bot.add_cog(Friday_note(bot))
