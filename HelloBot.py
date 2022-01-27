import discord

TOKEN = "OTM2MjE5ODg1MDgyNjYwODg0.YfKAtg.JigyOn0s6624ziyYyJPmSG8OhKg"

client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} is now online!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello there!')

client.run(TOKEN)
