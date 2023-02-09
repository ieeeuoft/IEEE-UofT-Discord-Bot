import discord
from discord.ext import commands
import os
import ieee_discord_bot.config

class IEEEBot(commands.Bot):
    
    def __init__(self):
        """
            A discord bot created for IEEE Hackathons
        """

        # Turn on Events which the bot will see
        # For more information, see https://discordjs.guide/popular-topics/intents.html#privileged-intents
        intents = discord.Intents.default()
        intents.presences = True
        intents.members = True
        intents.message_content = True

        super().__init__(command_prefix=config.__cmd_prefix__, description=config.__description__, intents=intents)

    def run(self):
        super().run(config.__discord_api_secret__)
        
    async def on_ready(self):
        for cog in config.__cogs__:
            try:
                await self.load_extension(cog)
            except:
                print(f"Issue loading {cog}")