from app import client
from app.config import ALLOW_SERVERS, SITES
from app.functions import get_codes, template
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
                                await message.edit(content = template(codes))
                        else:
                            for url in SITES:
                                codes = get_codes(url)
                                await channel.send(template(codes))
        await sleep(1800)


