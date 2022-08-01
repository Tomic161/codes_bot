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
                        if channel.last_message_id != None:
                            for url in SITES:
                                codes = get_codes(url)
                                message = await channel.fetch_message(channel.last_message_id)
                                await message.edit(content = template(codes[1], codes[0]))
                        else:
                            for url in SITES:
                                codes = get_codes(url)
                                await channel.send(template(codes[1], codes[0]))

        await sleep(1800)


