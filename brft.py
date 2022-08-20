# This example requires the 'message_content' intent.

import discord
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel:
       msg_to_send = "*" +  member.name + " " + "has joined vocal*"
       await client.get_channel(993172735880601643).send(msg_to_send)
       channel = after.channel
       # Code here...


client.run(process.env.TOKEN)