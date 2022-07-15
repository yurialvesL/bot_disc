from discord.ext import commands
import discord
import os
from time import sleep

ffmpeg = os.getenv('ffmpeg')

ffmpeg_options = {
    'options': '-vn'
}


class Faro(commands.Cog):
    """ Talks with user """

    def __init__(self, bot):
        self.bot = bot

    # *oi chama a função abaixo e ao invés do  @bot.command vira @commands.command
    @commands.command(name="dancagatinho", help="toca 'danca gatinho'")
    async def dancagatinho(self, ctx):
        try:

            voice_channel = ctx.author.voice.channel
            channel = None
            if voice_channel is not None:
                channel = voice_channel.name
                self.bot = await voice_channel.connect()
                self.bot.play(discord.FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe', source="faro/dancagatinho.mp3"))
                while self.bot.is_playing():
                    sleep(5)
                await self.bot.disconnect()
                await ctx.message.delete()
        except:
            await ctx.send(str(ctx.author.name) + " " + "Não está em um canal.")
        await ctx.message.delete()

    @commands.command(name="ai", help="toca 'ai'")
    async def ai(self, ctx):
        try:

            voice_channel = ctx.author.voice.channel
            channel = None
            if voice_channel is not None:
                channel = voice_channel.name
                self.bot = await voice_channel.connect()
                self.bot.play(discord.FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe', source="faro/ai.mp3"))
                while self.bot.is_playing():
                    sleep(5)
                await self.bot.disconnect()
                await ctx.message.delete()
        except:
            await ctx.send(str(ctx.author.name) + " " + "Não está em um canal.")
        await ctx.message.delete()

    @commands.command(name="aigostei", help="toca 'ai gostei'")
    async def aigostei(self, ctx):
        try:

            voice_channel = ctx.author.voice.channel
            channel = None
            if voice_channel is not None:
                channel = voice_channel.name
                self.bot = await voice_channel.connect()
                self.bot.play(discord.FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe', source="faro/aigostei.mp3"))
                while self.bot.is_playing():
                    sleep(5)
                await self.bot.disconnect()
                await ctx.message.delete()
        except:
            await ctx.send(str(ctx.author.name) + " " + "Não está em um canal.")
        await ctx.message.delete()

    @commands.command(name="aimamae", help="toca 'ai mamaeeee'")
    async def aimamae(self, ctx):
        try:

            voice_channel = ctx.author.voice.channel
            channel = None
            if voice_channel is not None:
                channel = voice_channel.name
                self.bot = await voice_channel.connect()
                self.bot.play(discord.FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe', source="faro/aimamae.mp3"))
                while self.bot.is_playing():
                    sleep(7)
                await self.bot.disconnect()
                await ctx.message.delete()
        except:
            await ctx.send(str(ctx.author.name) + " " + "Não está em um canal.")
        await ctx.message.delete()

    @commands.command(name="brincadeira", help="toca 'brincadeira'")
    async def brincadeira(self, ctx):
        try:

            voice_channel = ctx.author.voice.channel
            channel = None
            if voice_channel is not None:
                channel = voice_channel.name
                self.bot = await voice_channel.connect()
                self.bot.play(discord.FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe', source="faro/brincadeira.mp3"))
                while self.bot.is_playing():
                    sleep(5)
                await self.bot.disconnect()
                await ctx.message.delete()
        except:
            await ctx.send(str(ctx.author.name) + " " + "Não está em um canal.")
        await ctx.message.delete()

    @commands.command(name="cavalo", help="toca 'cavalo'")
    async def cavalo(self, ctx):
        try:

            voice_channel = ctx.author.voice.channel
            channel = None
            if voice_channel is not None:
                channel = voice_channel.name
                self.bot = await voice_channel.connect()
                self.bot.play(discord.FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe', source="faro/cavalo.mp3"))
                while self.bot.is_playing():
                    sleep(5)
                await self.bot.disconnect()
                await ctx.message.delete()
        except:
            await ctx.send(str(ctx.author.name) + " " + "Não está em um canal.")
        await ctx.message.delete()

    @commands.command(name="chega", help="toca 'chegaaa'")
    async def chega(self, ctx):
        try:

            voice_channel = ctx.author.voice.channel
            channel = None
            if voice_channel is not None:
                channel = voice_channel.name
                self.bot = await voice_channel.connect()
                self.bot.play(discord.FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe', source="faro/chega.mp3"))
                while self.bot.is_playing():
                    sleep(5)
                await self.bot.disconnect()
                await ctx.message.delete()
        except:
            await ctx.send(str(ctx.author.name) + " " + "Não está em um canal.")
        await ctx.message.delete()

    @commands.command(name="elegosta", help="toca 'ele gostaaaa'")
    async def elegosta(self, ctx):
        try:

            voice_channel = ctx.author.voice.channel
            channel = None
            if voice_channel is not None:
                channel = voice_channel.name
                self.bot = await voice_channel.connect()
                self.bot.play(discord.FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe', source="faro/elegosta.mp3"))
                while self.bot.is_playing():
                    sleep(5)
                await self.bot.disconnect()
                await ctx.message.delete()
        except:
            await ctx.send(str(ctx.author.name) + " " + "Não está em um canal.")
        await ctx.message.delete()

    @commands.command(name="queisso", help="toca 'que issooo'")
    async def queisso(self, ctx):
        try:

            voice_channel = ctx.author.voice.channel
            channel = None
            if voice_channel is not None:
                channel = voice_channel.name
                self.bot = await voice_channel.connect()
                self.bot.play(discord.FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe', source="faro/queisso.mp3"))
                while self.bot.is_playing():
                    sleep(6)
                await self.bot.disconnect()
                await ctx.message.delete()
        except:
            await ctx.send(str(ctx.author.name) + " " + "Não está em um canal.")
        await ctx.message.delete()



    @commands.command(name="semgraca", help="toca 'sem gracaaaa'")
    async def semgraca(self, ctx):
        try:

            voice_channel = ctx.author.voice.channel
            channel = None
            if voice_channel is not None:
                channel = voice_channel.name
                self.bot = await voice_channel.connect()
                self.bot.play(discord.FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe', source="faro/semgraca.mp3"))
                while self.bot.is_playing():
                    sleep(6)
                await self.bot.disconnect()
                await ctx.message.delete()
        except:
            await ctx.send(str(ctx.author.name) + " " + "Não está em um canal.")
        await ctx.message.delete()

    @commands.command(name="som", help="toca 'som audasidbasudubasida'")
    async def som(self, ctx):
        try:

            voice_channel = ctx.author.voice.channel
            channel = None
            if voice_channel is not None:
                channel = voice_channel.name
                self.bot = await voice_channel.connect()
                self.bot.play(discord.FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe', source="faro/som.mp3"))
                while self.bot.is_playing():
                    sleep(5)
                await self.bot.disconnect()
                await ctx.message.delete()
        except:
            await ctx.send(str(ctx.author.name) + " " + "Não está em um canal.")
        await ctx.message.delete()

    @commands.command(name="tome", help="toca 'tomi'")
    async def tome(self, ctx):
        try:

            voice_channel = ctx.author.voice.channel
            channel = None
            if voice_channel is not None:
                channel = voice_channel.name
                self.bot = await voice_channel.connect()
                self.bot.play(discord.FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe', source="faro/tome.mp3"))
                while self.bot.is_playing():
                    sleep(4)
                await self.bot.disconnect()
                await ctx.message.delete()
        except:
            await ctx.send(str(ctx.author.name) + " " + "Não está em um canal.")
        await ctx.message.delete()

    @commands.command(name="ui", help="toca 'uiiiiiiiiii'")
    async def tome(self, ctx):
        try:

            voice_channel = ctx.author.voice.channel
            channel = None
            if voice_channel is not None:
                channel = voice_channel.name
                self.bot = await voice_channel.connect()
                self.bot.play(discord.FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe', source="faro/ui.mp3"))
                while self.bot.is_playing():
                    sleep(5)
                await self.bot.disconnect()
                await ctx.message.delete()
        except:
            await ctx.send(str(ctx.author.name) + " " + "Não está em um canal.")
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Faro(bot))
