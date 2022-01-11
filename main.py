
try:
    import discord
    from discord.ext import commands
    import os
    from dotenv import load_dotenv
    import prettytable as pt
    import modules.corona_stats as corona_stats
    import modules.get_meme as get_meme
except ImportError:
    print("There are some libaries missing, please install them using 'pip3 install -r requirements.txt'")
    exit(1)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='&')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def corona(ctx, country="Germany"):
    covid_data = corona_stats.get_data()
    key_names = ['Aktive Fälle', 'Kritische Fälle', 'Alle Fälle', 'Neue Fälle', 'Todesfälle', 'Neue Todesfälle', 'Genesene', 'Neue Genesene']
    
    table = pt.PrettyTable(['Statistik', 'Wert'])
    table.align['Statistik'] = 'l'
    table.align['Wert'] = 'r'
    try:
        for i, j in enumerate(key_names):
            table.add_row([j, covid_data[country][i]])
    except KeyError:
        embed=discord.Embed(title="Fehler", description="Dieses Land wurde nicht in der Datenbank gefunden.", timestamp=ctx.message.created_at, color=0xee2f45)
        await ctx.send(embed=embed)
        return
    embed=discord.Embed(title=f"Aktuelle COVID-19 Statistiken ({country})", url="https://www.worldometers.info/coronavirus/#countries", timestamp=ctx.message.created_at, color=0x65c465)
    embed.add_field(name=f"Neuste Werte:", value=f"```{table}```", inline=False)

    await ctx.send(embed=embed)

@client.command()
async def crypto(ctx):
    pass

@client.command()
async def meme(ctx, subreddit="memes"):
    try:
        meme = await get_meme.generate_meme(subreddit)
    except Exception:
        embed=discord.Embed(title="Fehler", description="Dieser Subreddit existiert nicht.", timestamp=ctx.message.created_at, color=0xee2f45)
        await ctx.send(embed=embed)
        return
    embed=discord.Embed(title=meme[0], url=meme[2], timestamp=ctx.message.created_at, color=0xee752f)
    embed.set_image(url=meme[1])

    await ctx.send(embed=embed)

if __name__ == '__main__':
    client.run(TOKEN)
