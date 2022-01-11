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
        await ctx.send("Dieses Land wurde nicht in der Datenbank gefunden.")
        print(f"&corona: Corona-Stats: Unvalid request by {ctx.message.author}!")
        return
    await ctx.send(f"Aktuelle COVID-19 Statistiken ({country}): ```{table}```")
    print(f"&corona: Corona-Stats:\n{table}\nsent to {ctx.message.author}!")

@client.command()
async def crypto(ctx):
    pass

@client.command()
async def meme(ctx):
    pass

if __name__ == '__main__':
    client.run(TOKEN)
