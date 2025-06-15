import discord
from discord.ext import commands
import os
from config import TOKEN

TOKEN = os.getenv("DISCORD_TOKEN")  #如果你不是把他部署到render上可以直接在config.py中设置TOKEN变量然后把这一行注释掉

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'已登录为 {bot.user}')
    try:
        await bot.tree.sync()
        print("命令已成功同步！")
    except Exception as e:
        print(f"命令同步失败：{e}")

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    await load_cogs()
    await bot.start(TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())