from discord.ext import commands
import requests


class Crypto(commands.Cog):
    """ Works with Cryptocurrency """
    def __init__(self,bot):
        self.bot=bot

    # Função abaixo pega um dado de um API e mostra no bot(aqui no caso mostra a cotação de uma criptmoeada)
    @commands.command()
    async def binance(self,ctx, coin, base, help="mostra a cotação de uma moeda específica que deseja EX:(btc usd)"):
        try:
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")

            data = response.json()
            price = data.get('price')
            if price:
                await ctx.send(f"O valor do par {coin}/{base} é {price}")
            else:
                await ctx.send("Está moeda não existe")
        except Exception as error:
            await ctx.send('Ooops.... Deu algum error!')
            print(error)


def setup(bot):
    bot.add_cog(Crypto(bot))
