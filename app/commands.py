from app import client


@client.command()
async def test(ctx, arg):
    await ctx.send(arg)