import discord
from discord.ext import commands
import requests

# 机器人令牌
token = "YOUR_BOT_TOKEN"  # 替换为你的 Discord 机器人令牌
# 机器人 ID

# 设置所需的意图
intents = discord.Intents.default()
intents.message_content = True

# 创建 bot 实例
bot = commands.Bot(command_prefix="!", intents=intents)

# 同步指令命令
@bot.command()
async def synccommands(ctx):
    try:
        # 强制同步所有命令
        synced = await bot.tree.sync()
        await ctx.send(f"同步完成！已同步 {len(synced)} 个命令.")
    except Exception as e:
        await ctx.send(f"同步失败：{e}")

# 最近消息存储列表
recent_messages = []
max_recent_messages = 10  # 设置最大存储消息数量

# 当 bot 准备好时的事件
@bot.event
async def on_ready():
    print(f'已登录为 {bot.user}')
    try:
        await bot.tree.sync()
        print("命令已成功同步！")
    except Exception as e:
        print(f"命令同步失败：{e}")

# 监听消息的事件
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # 简单的文本响应
    if "你好" in message.content or "大家好" in message.content:
        await message.reply(f"{message.author.mention} 你好！", mention_author=False)

    await bot.process_commands(message)

# 定义 /ip 指令
@bot.tree.command(name="ip", description="查询 IP 地址的地理位置")
async def ip(interaction: discord.Interaction, ip_address: str):
    """请使用 /ip [ip地址] 来查询 ~ """
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
                f"**ZIP**: `{data.get('zip', '无邮编信息')}`\n"
            )

            await interaction.response.send_message(f"{interaction.user.mention} 查询结果:\n{result}")
        else:
            await interaction.response.send_message(f"{interaction.user.mention} 无法查询此 IP 地址的信息，请检查输入是否正确。")
    except Exception as e:
        await interaction.response.send_message(f"{interaction.user.mention} 查询 IP 地址时发生错误：{str(e)}")

# 定义 /mc 指令，用于查询 Minecraft Java 服务器状态
@bot.tree.command(name="mc", description="查询 Minecraft Java 服务器状态")
async def mc(interaction: discord.Interaction, server_address: str):
    API_URL = f"https://api.mcsrvstat.us/3/{server_address}"
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # 检查 HTTP 请求是否成功
        data = response.json()

        # 打印调试信息
        print(f"API 响应数据: {data}")

        # 检查服务器是否在线
        if data.get("online"):
            players = data.get("players", {})
            motd = data.get("motd", {}).get("clean", ["未知"])
            motd_text = ''.join(motd)  # 将 MOTD 列表合并为字符串

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
            await interaction.response.send_message(f"服务器 `{server_address}` 处于离线状态，无法查询更多信息。")
    except requests.exceptions.RequestException as req_err:
        await interaction.response.send_message(f"查询 Minecraft 服务器状态时发生网络错误：{str(req_err)}")
    except KeyError as key_err:
        await interaction.response.send_message(f"查询 Minecraft 服务器状态时发生数据解析错误：缺少字段 {str(key_err)}")
    except Exception as e:
        await interaction.response.send_message(f"查询 Minecraft 服务器状态时发生未知错误：{str(e)}")

# 定义 /mcbd 指令，用于查询 Minecraft Bedrock 服务器状态
@bot.tree.command(name="mcbd", description="查询 Minecraft Bedrock 服务器状态")
async def mcbd(interaction: discord.Interaction, server_address: str):
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
            await interaction.response.send_message(f"服务器 `{server_address}` 处于离线状态，无法查询更多信息。")
    except Exception as e:
        await interaction.response.send_message(f"查询 Minecraft Bedrock 服务器状态时发生错误：{str(e)}")

# 定义 /mcicon 指令，用于查询 Minecraft 服务器图标
@bot.tree.command(name="mcicon", description="查看 Minecraft 服务器图片")
async def mcicon(interaction: discord.Interaction, server_address: str):
    API_URL = f"https://api.mcsrvstat.us/icon/{server_address}"
    try:
        await interaction.response.send_message(f"服务器 `{server_address}` 的图标如下：\n{API_URL}")
    except Exception as e:
        await interaction.response.send_message(f"查询 Minecraft 服务器图片时发生错误：{str(e)}")

# 定义 /hbot 指令
@bot.tree.command(name="hbot", description="踢一下查询机器人是否活着！")
async def hbot(interaction: discord.Interaction):
    """踢一下，检查机器人是否活着"""
    await interaction.response.send_message("OH MAII GOTTO!!! 我还活着！！！")

# 启动机器人
bot.run(token)


