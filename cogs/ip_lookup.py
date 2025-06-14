import discord
from discord.ext import commands
from discord import app_commands
import requests

class IpLookup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ip", description="查询 IP 地址的地理位置")
    async def ip(self, interaction: discord.Interaction, ip_address: str):
        API_URL = f"http://ip-api.com/json/{ip_address}"
        try:
            response = requests.get(API_URL)
            data = response.json()

            if data["status"] == "success":
                result = (
                    f"**IP地址**: `{data['query']}`\n"
                    f"**国家**: `{data['country']}`\n"
                    f"**省份**: `{data['regionName']}`\n"
                    f"**城市**: `{data['city']}`\n"
                    f"**经度**: `{data['lon']}`\n"
                    f"**纬度**: `{data['lat']}`\n"
                    f"**时区**: `{data['timezone']}`\n"
                    f"**组织**: `{data.get('org', '无组织信息')}`\n"
                    f"**运营商**: `{data.get('isp', '无运营商信息')}`\n"
                    f"**AS**: `{data.get('as', '无AS信息')}`\n"
                    f"**ZIP**: `{data.get('zip', '无邮编信息')}`"
                )
                await interaction.response.send_message(f"{interaction.user.mention} 查询结果:\n{result}")
            else:
                await interaction.response.send_message(f"{interaction.user.mention} 无法查询此 IP 地址的信息。")
        except Exception as e:
            await interaction.response.send_message(f"{interaction.user.mention} 查询 IP 地址时发生错误：{str(e)}")

async def setup(bot):
    await bot.add_cog(IpLookup(bot))