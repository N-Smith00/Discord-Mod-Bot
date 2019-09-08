import discord
import os
from keep_alive import keep_alive

client=discord.Client()

@client.event
async def on_ready():
    print('mod bot reporting for duty')
    print(client.user)
    channel = client.get_channel(620095182871855104)
    print(channel)
    ranks = await channel.send('react with your rank to let everyone else know your skill')
    # emoji = client.get_emoji(\N{HEART})
    await ranks.add_reaction('\U0001F493')

@client.event
async def ranks():
    channel = client.get_channel(620095182871855104)
    print(channel)
    ranks = await client.send(channel, 'react with your rank to let everyone else know your skill')
    await client.add_reaction(ranks, ':rose:')

keep_alive()
token = os.environ.get('DISCORD_BOT_SECRET')
client.run(token)
