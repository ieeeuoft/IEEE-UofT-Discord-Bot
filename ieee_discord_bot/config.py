import os
from dotenv import load_dotenv

load_dotenv()

# Load cogs 
__cogs__ = []
for f in os.listdir("ieee_discord_bot/cogs"):
    if f.endswith(".py") and f != "__init__.py":
        cog = "ieee_discord_bot.cogs." + f.split(".", 1)[0]
        __cogs__.append(cog)


__discord_api_secret__ = os.getenv("DISCORD_API_SECRET")
__cmd_prefix__ = str(os.getenv("cmd_prefix") or '/')
__description__ = os.getenv("description")