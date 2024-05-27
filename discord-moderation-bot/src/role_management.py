# role_management.py (Python)

# Import necessary packages and modules
import discord
from discord.ext import commands

# Define RoleManagement class to handle role-related functionalities
class RoleManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Function to assign a role to a user
    @commands.command(name='assign_role')
    async def assign_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.add_roles(role)
            await ctx.send(f"Role {role.name} has been assigned to {member.display_name}")
        except discord.Forbidden:
            await ctx.send("Insufficient permissions to assign roles")
        except discord.HTTPException:
            await ctx.send("Failed to assign role")

    # Function to revoke a role from a user
    @commands.command(name='revoke_role')
    async def revoke_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.remove_roles(role)
            await ctx.send(f"Role {role.name} has been revoked from {member.display_name}")
        except discord.Forbidden:
            await ctx.send("Insufficient permissions to revoke roles")
        except discord.HTTPException:
            await ctx.send("Failed to revoke role")

# Setup function to add RoleManagement cog to the bot
def setup(bot):
    bot.add_cog(RoleManagement(bot))