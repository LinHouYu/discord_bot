#这个脚本用户部署在render的web services上加入了 flask 与 token 来欺骗render让脚本能在web services免费运行。

import discord
from discord.ext import commands
import os
from config import TOKEN
import os
import threading
from flask import Flask

TOKEN = os.getenv("TOKEN")  #如果你不是把他部署到render上可以直接在config.py中设置TOKEN变量然后把这一行注释掉


# # 启动 Flask 假服务，Render 扫端口用的   #被遗忘的RENDER服务器/(ㄒoㄒ)/~~ #X(被重新使用的欺骗代码
def run_flask():
    app = Flask('')

    @app.route('/')
    def home():
        return "Bot is alive!"

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_flask).start()



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
