import discord
import os
import eddistance1
client = discord.Client()


def get_d1(inp):
    search = inp.find('(')
    search1 = inp.find(')')
    #comma = inp.find(',', search)
    substring = inp[search+1 : search1]
    if (" " in substring):
        substring = substring.replace(" ","+")
    return substring

def get_d2(inp):
    comma = inp.find(',')
    search1 = inp.find(')',comma)
    substring = inp[comma+2 : search1]
    if (" " in substring):
        substring = substring.replace(" ","+")
    return substring

def get_jumps(inp):
    comma = inp.find('R')
    search1 = inp.find(')',comma)
    substring = inp[comma+1 : search1]
    if (" " in substring):
        substring = substring.replace(" ","+")
    return substring

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-ED'):
        await message.channel.send('Hello!')

    if message.content.startswith('-D') :
        tem = message.content
        tem = tem.replace('-D',"")
        mess = eddistance1.get_distance(get_d1(tem),get_d2(tem))
        await message.channel.send(mess)
    elif message.content.startswith('-Distance'):
        tem = message.content
        tem = tem.replace('-Distance',"")
        mess = eddistance1.get_distance(get_d1(tem),get_d2(tem))
        await message.channel.send(mess)


    if message.content.startswith('-R'):
      tem = message.content
      tem = tem.replace('-RuntimeError',"")
      mess = eddistance1.get_dist_range(get_d1(tem),get_d2(tem),get_jumps(tem))
      await message.channel.send(mess)
    
    









client.run(os.getenv('BOT_KEY'))



