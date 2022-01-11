try:
    import discord
    import os
    from dotenv import load_dotenv
except ImportError:
    print("There are some libaries missing, please install them using 'pip3 install -r requirements.txt'")
    exit(1)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

if __name__ == '__main__':
    client.run(TOKEN)