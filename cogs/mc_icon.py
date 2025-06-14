import discord
from discord.ext import commands
from discord import app_commands

class MinecraftIcon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mcicon", description="查看 Minecraft 服务器图片")
    async def mcicon(self, interaction: discord.Interaction, server_address: str):
        API_URL = f"https://api.mcsrvstat.us/icon/{server_address}"
        await interaction.response.send_message(f"服务器 `{server_address}` 的图标如下：\n{API_URL}")

async def setup(bot):
    await bot.add_cog(MinecraftIcon(bot))