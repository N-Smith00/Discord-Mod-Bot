import discord
import os
from keep_alive import keep_alive
from rank_list import ranks_list

client=discord.Client()

@client.event
async def on_ready():
    print('mod bot reporting for duty')
    print(client.user)
    channel = client.get_channel(620095182871855104)
    ranks = await channel.send('react with your rank to let everyone else know your skill')
    for rank in ranks_list:
        await ranks.add_reaction(rank)

keep_alive()
token = os.environ.get('DISCORD_BOT_SECRET')
client.run(token)
