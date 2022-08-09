from discord.ext import commands
from utils.utils import *


async def setup(bot:commands.Bot):
    await bot.add_cog(CogManagement(bot))


class CogManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, cog_name):
        """Load a specific cog
        Take in the name of a cog from a user. Send a message confirming the action, and call load_extension
        command from Discord.ext, passing in cog_name. If the cog is ServerManagment, call load_server_managment
        method from CogManagment.py

        Args:
            cog_name (str): Name of the cog being loaded

        Outputs:
            Message to user informing them of what cog is being loaded.
        """

        await ctx.send(f'Loading {cog_name}')
        await self.bot.load_extension(f'Cogs.{cog_name}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, cog_name):
        """Reload a specific cog
        Take in the name of single cog from a user and reload it. Output a message confirming reload action
        and use reload extension method on the cog. If reloading server managment, call load_server_managment
        method from CogManagment.py

        Args:
            cog_name (str): Name of the cog that will be reloaded

        Outputs:
            Message to user informing them of what cog is being restarted.
        """

        await ctx.send(f'Reloading {cog_name}')
        await self.bot.reload_extension(f'Cogs.{cog_name}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, cog_name):
        """Unload a specific cog
        Take in the name of a cog from a user. If the user is not trying to unload the CogManagment cog,
        send a message confirming the action. Call unload_extension command from Discord.ext, passing in
        the cog_name.

        Args:
            cog_name (str): Name of the cog being unloaded

        Outputs:
            Message to user informing them of what cog is being unloaded.
        """
        
        if cog_name != 'CogManagement':
            await ctx.send(f'Unloading {cog_name}')
            await self.bot.unload_extension(f'Cogs.{cog_name}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def sync(self, ctx):
        """Syncs all slash commands
        Syncs application commands to the bot's global tree.
        Copies to current server.
        """

        await self.bot.tree.sync()      # syncs global tree to server/guild
        self.bot.tree.copy_global_to(guild=ctx.guild)       # needs to be run the first time a bot syncs to a server
