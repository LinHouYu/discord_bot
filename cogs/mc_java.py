import discord
from discord.ext import commands
from discord import app_commands
import requests

class MinecraftJava(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mc", description="查询 Minecraft Java 服务器状态")
    async def mc(self, interaction: discord.Interaction, server_address: str):
        API_URL = f"https://api.mcsrvstat.us/3/{server_address}"
        try:
            response = requests.get(API_URL)
            data = response.json()

            if data.get("online"):
                players = data.get("players", {})
                motd = data.get("motd", {}).get("clean", ["未知"])
                motd_text = ''.join(motd)

                result = (
                    f"🎮 **Minecraft Java 服务器状态**\n"
                    f"**服务器地址**: `{server_address}`\n"
                    f"**IP地址**: `{data.get('ip', '未知')}`\n"
                    f"**端口**: `{data.get('port', '未知')}`\n"
                    f"**版本**: `{data.get('version', '未知')}`\n"
                    f"**在线玩家**: `{players.get('online', 0)}/{players.get('max', 0)}`\n"
                    f"**MOTD**: `{motd_text}`"
                )
                await interaction.response.send_message(result)
            else:
                await interaction.response.send_message(f"服务器 `{server_address}` 处于离线状态。")
        except Exception as e:
            await interaction.response.send_message(f"错误：{str(e)}")

async def setup(bot):
    await bot.add_cog(MinecraftJava(bot))