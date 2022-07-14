import json
import discord
file = open('.json')
getFile = json.loads(file.read())
token = getFile['token']
botTestingGrounds = getFile['bot-testing-grounds']
client = discord.Client()
prefix = 'v'

@client.event 
async def on_ready(): 
    print('logged in as '+client.user.name)
    
@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return
    if message.content.find(prefix, 0, prefix.__len__())==0:
        if message.content==prefix+'sayhi':
            channel = message.channel
            await channel.send('ola ola ola')

client.run(token)