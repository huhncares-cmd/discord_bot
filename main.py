
try:
    import discord
    from discord.ext import commands
    import os
    from dotenv import load_dotenv
    import prettytable as pt
    import modules.corona_stats as corona_stats
    import modules.search_reddit as search_reddit
except ImportError:
    print("There are some libaries missing, please install them using 'pip3 install -r requirements.txt'")
    exit(1)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='&')
client.remove_command("help")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Game(name="&help | www.huhncares.de"))

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help", timestamp=ctx.message.created_at, color=0x00ff00)
    embed.add_field(name="&corona [country]", value="Shows the corona stats (default: Germany)", inline=False)
    embed.add_field(name="&reddit [subreddit]", value="Shows a random image from the subreddit (default: memes)", inline=False)
    embed.set_author(name=f"{ctx.message.author}", icon_url=f"{ctx.message.author.avatar_url}")
    embed.set_footer(text="Coded with <3 by huhncares")
    await ctx.send(embed=embed)

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
async def reddit(ctx, subreddit="memes"):
    try:
        post = await search_reddit.get_random_reddit_image(subreddit)
    except Exception:
        embed=discord.Embed(title="Fehler", description="Dieser Subreddit existiert nicht.", timestamp=ctx.message.created_at, color=0xee2f45)
        await ctx.send(embed=embed)
        return
    embed=discord.Embed(title=post[0], url=post[2], timestamp=ctx.message.created_at, color=0xee752f)
    embed.set_author(name=f"r/{subreddit}")
    embed.set_image(url=post[1])

    await ctx.send(embed=embed)

if __name__ == '__main__':
    client.run(TOKEN)
