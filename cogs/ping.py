import discord
from discord.ext import commands
from discord import app_commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hbot", description="踢一下查询机器人是否活着！")
    async def hbot(self, interaction: discord.Interaction):
        await interaction.response.send_message("OH MAII GOTTO!!! 我还活着！！！")

async def setup(bot):
    await bot.add_cog(Ping(bot))