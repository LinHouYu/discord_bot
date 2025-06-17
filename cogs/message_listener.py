import discord
from discord.ext import commands
from discord import app_commands
import re

class MessageResponder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.recent_messages = []

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        # 问候语自动回复
        if "你好" in message.content or "大家好" in message.content:
            await message.reply(f"{message.author.mention} 你好！", mention_author=False)

        # 检查重复消息
        self.recent_messages.append(message.content)
        if len(self.recent_messages) > 2:
            self.recent_messages.pop(0)
        if len(self.recent_messages) == 2 and self.recent_messages[0] == self.recent_messages[1]:
            await message.channel.send(message.content)

        # 检查是否是回复别人
        if message.reference and (message.content.startswith("/") or message.content.startswith("$")):
            # 获取被回复的原始消息对象
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            target_user = replied_message.author.mention
            sender = message.author.mention
            content = message.content[1:].strip()

            # 回复消息，无论是中文（以 / 开头且有中文字符）还是英文（以 $ 开头）
            if (message.content.startswith("/") and re.search(r'[\u4e00-\u9fff]', content)) or message.content.startswith("$"):
                await message.reply(f"{sender} {content} {target_user}")
                # 合并分支：如果消息是回复且以 / 或 $ 开头，已在上面实现，无需重复实现
        # 仍处理指令（必要时）
        await self.bot.process_commands(message)


    # Slash 指令示例
    @app_commands.command(name="偷吃", description="对某人偷偷干点什么")
    async def steal_eat(self, interaction: discord.Interaction, target: discord.User):
        await interaction.response.send_message(f"{interaction.user.mention} 偷吃了 {target.mention}！")

    @app_commands.command(name="打", description="打一下某人")
    async def hit(self, interaction: discord.Interaction, target: discord.User):
        await interaction.response.send_message(f"{interaction.user.mention} 打了 {target.mention}！")

    @app_commands.command(name="捏", description="捏一捏某人")
    async def pinch(self, interaction: discord.Interaction, target: discord.User):
        await interaction.response.send_message(f"{interaction.user.mention} 捏了 {target.mention}！")

async def setup(bot):
    await bot.add_cog(MessageResponder(bot))
