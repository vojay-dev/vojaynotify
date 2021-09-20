import json

from discord.ext import commands
from discord.ext.tasks import loop

from twitch import get_notifications

bot = commands.Bot(command_prefix="$")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@loop(seconds=90)
async def check_twitch_online_streamers():
    channel = bot.get_channel(864629508244766740)
    if not channel:
        return

    notifications = get_notifications()
    for notification in notifications:
        await channel.send("streamer {} ist jetzt online: {}".format(notification["user_login"], notification))


with open("config.json") as config_file:
    config = json.load(config_file)

if __name__ == "__main__":
    check_twitch_online_streamers.start()
    bot.run(config["discord_token"])
