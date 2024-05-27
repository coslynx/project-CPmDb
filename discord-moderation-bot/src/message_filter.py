# message_filter.py (Python)

import discord

class MessageFilter:
    def __init__(self, client):
        self.client = client

    async def filter_message(self, message):
        if message.author == self.client.user:
            return

        # Implement message filtering logic here
        if "bad_word" in message.content:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please refrain from using inappropriate language.")

        # Add more filtering rules as needed

# Dependencies: discord.py