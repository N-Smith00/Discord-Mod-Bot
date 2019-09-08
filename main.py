import discord
import os
from keep_alive import keep_alive

client=discord.Client()

@client.event
async def on_ready():
    print('mod bot reporting for duty')
    print(client.user)
    channel = client.get_channel(620095182871855104)
    ranks = await channel.send('react with your rank to let everyone else know your skill')
    global ranks
    await ranks.add_reaction(':Iron:620335275192614953')
    await ranks.add_reaction(':Bronze:620334694826770489')
    await ranks.add_reaction(':Silver:620334883868508184')
    await ranks.add_reaction(':Gold:620335348018446341')
    await ranks.add_reaction(':Platinium:620335395787505684')
    await ranks.add_reaction(':Diamond:620335430952419372')
    await ranks.add_reaction(':Master:620335475328286741')
    await ranks.add_reaction(':Grandmaster:620335512070258718')
    await ranks.add_reaction(':Challenger:620335550733352980')

keep_alive()
token = os.environ.get('DISCORD_BOT_SECRET')
client.run(token)
