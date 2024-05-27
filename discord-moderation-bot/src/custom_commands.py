# custom_commands.py (Python)

import discord

class CustomCommands:
    def __init__(self, bot):
        self.bot = bot

    async def greet_user(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention}! How can I assist you today?")

    async def kick_user(self, ctx, user):
        if ctx.author.guild_permissions.kick_members:
            await user.kick()
            await ctx.send(f"{user.name} has been kicked from the server.")
        else:
            await ctx.send("You do not have permission to kick members.")

    async def ban_user(self, ctx, user):
        if ctx.author.guild_permissions.ban_members:
            await user.ban()
            await ctx.send(f"{user.name} has been banned from the server.")
        else:
            await ctx.send("You do not have permission to ban members.")

    async def add_role(self, ctx, user, role):
        role_obj = discord.utils.get(ctx.guild.roles, name=role)
        if role_obj:
            await user.add_roles(role_obj)
            await ctx.send(f"{user.name} has been given the {role} role.")
        else:
            await ctx.send(f"Role '{role}' not found.")

    async def remove_role(self, ctx, user, role):
        role_obj = discord.utils.get(ctx.guild.roles, name=role)
        if role_obj:
            await user.remove_roles(role_obj)
            await ctx.send(f"{user.name} no longer has the {role} role.")
        else:
            await ctx.send(f"Role '{role}' not found.")

    async def clear_messages(self, ctx, limit):
        if ctx.author.guild_permissions.manage_messages:
            await ctx.channel.purge(limit=limit)
        else:
            await ctx.send("You do not have permission to manage messages.")

# End of custom_commands.py