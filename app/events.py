from app import client
from app.config import ALLOW_SERVERS, SITES, IP
from app.functions import get_codes, template, get_server_info
from asyncio import sleep


@client.event
async def on_ready():
    print('Logged on {0.user}'.format(client))
    while True:
        for guild in client.guilds:
            if guild.id in ALLOW_SERVERS:
                for channel in await guild.fetch_channels():
                    if channel.name.lower() == 'codes':
                        messages = await channel.history(limit = 1).flatten()
                        if messages != []:
                            for url in SITES:
                                codes = get_codes(url)
                                message = await channel.fetch_message(messages[0].id)
                                await message.edit(content = template(codes[0], codes[1]))
                        else:
                            for url in SITES:
                                codes = get_codes(url)
                                await channel.send(template(codes[0], codes[1]))
        server = get_server_info(IP)
        channel = await client.fetch_channel(1008722183536779386)
        await channel.edit(name = 'SERVER STATUS: {0}'.format(server[0]))
        channel = await client.fetch_channel(1008722185168359485)
        await channel.edit(name = 'ONLINE: {0}'.format(server[1]))
        await sleep(30)
        print('OK')

@client.event
async def on_message(msg):
    if msg.author.id != 1003722971413749840:
        if 'айпи' in msg.content.lower():
            msg_reply = await msg.reply('IP: {0}'.format(IP))
            await sleep(20)
            await msg_reply.delete()
            await msg.delete()


@client.event
async def close():
    channel = await client.fetch_channel(1008722183536779386)
    await channel.edit(name = 'BOT OFF')
    channel = await client.fetch_channel(1008722185168359485)
    await channel.edit(name = 'BOT OFF')

