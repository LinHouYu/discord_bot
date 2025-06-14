import discord
from discord.ext import commands
from discord import app_commands
import requests

class MinecraftBedrock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mcbd", description="查询 Minecraft Bedrock 服务器状态")
    async def mcbd(self, interaction: discord.Interaction, server_address: str):
        API_URL = f"https://api.mcsrvstat.us/bedrock/3/{server_address}"
        try:
            response = requests.get(API_URL)
            data = response.json()
            if data["online"]:
                result = (
                    f"🎮 **Minecraft Bedrock 服务器状态**\n"
                    f"**服务器地址**: `{server_address}`\n"
                    f"**IP地址**: `{data.get('ip', '未知')}`\n"
                    f"**端口**: `{data.get('port', '未知')}`\n"
                    f"**版本**: `{data.get('version', '未知')}`\n"
                    f"**在线玩家**: `{data['players']['online']}/{data['players']['max']}`\n"
                    f"**MOTD**: `{''.join(data['motd']['clean'])}`"
                )
                await interaction.response.send_message(result)
            else:
                await interaction.response.send_message(f"服务器 `{server_address}` 处于离线状态。")
        except Exception as e:
            await interaction.response.send_message(f"查询失败：{str(e)}")

async def setup(bot):
    await bot.add_cog(MinecraftBedrock(bot))