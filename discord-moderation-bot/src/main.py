# main.py (Python)

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create a bot instance
bot = commands.Bot(command_prefix='!')

# Load all cogs
initial_extensions = [
    'src.bot',
    'src.message_filter',
    'src.word_filters',
    'src.user_activity_tracker',
    'src.warning_and_mute_system',
    'src.role_management',
    'src.scheduled_tasks',
    'src.custom_commands',
    'src.monitoring',
    'src.updates_and_improvements'
]

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

    # Run the bot
    bot.run(TOKEN)