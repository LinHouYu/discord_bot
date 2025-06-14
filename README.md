# Discord 多功能 Bot 🤖

一个支持 Slash 指令、关键词自动回复、Minecraft 查询等功能的模块化 Discord Bot，适合学习与快速扩展！

> 🎨 **灵感来源：**  
> 本项目参考自 [焦糖波波 Sugarbobo](https://www.youtube.com/watch?v=vSJC5qiI3Rs&t=361s) 所介绍的 “客製化 Discord 指令” 教學影片，感谢其优秀内容带来的启发！

---

## 📦 功能介绍

- `/ip [IP地址]`：查询 IP 的地理位置
- `/mc [Java服务器地址]`：查询 Minecraft Java 状态
- `/mcbd [基岩版服务器地址]`：查询 Minecraft 基岩版状态
- `/mcicon [服务器地址]`：查看服务器图标
- `/hbot`：检查 Bot 是否活着
- `/偷吃 @用户`、`/打 @用户`、`/捏 @用户`：趣味互动
- 自动响应“你好”、“大家好”
- 相同消息自动复读（复读机）
- 输入 `/中文内容` → Bot 回复“你写的中文是 xxx！”
- 输入 `/$英文内容` → Bot 回复“你写的英文是 xxx”

---

## 📂 项目结构
discord_bot_project/
├── bot.py # 启动入口
├── config.py # 配置项（Bot Token）
├── cogs/
│ ├── ip_lookup.py # /ip 功能模块
│ ├── minecraft.py # Minecraft 功能模块
│ └── message_listener.py # 自动回复、复读、互动等
├── requirements.txt # 依赖列表
└── README.md # 项目说明文档

---

## 🚀 快速开始

### ✅ 第一步：克隆项目

```bash
git clone https://github.com/你的用户名/discord-bot.git
cd discord-bot
```

### ✅ 第二步：安装依赖
推荐在虚拟环境中安装!  [vscode里创建虚拟环境](https://www.bilibili.com/video/BV19r5WzkEjk/?share_source=copy_web&vd_source=af1b836b3dccf648b1eeecc5e9541b1e)
```bash
pip install discord
pip install requests
```
### ✅ 第三步：配置 Token
打开 config.py，替换里面的 BOT_TOKEN：
```bash
BOT_TOKEN = "你的DiscordBotToken"
```
### ✅ 第四步：运行机器人
python bot.py

这里我放个视频演示👉 [完整项目视频演示](https://www.bilibili.com/video/BV1wWMDzEENb/?share_source=copy_web&vd_source=af1b836b3dccf648b1eeecc5e9541b1e)

## 💡 如何添加新功能？

1️⃣ 在 `cogs/` 目录中新增一个 `.py` 文件，例如 `my_feature.py`  
2️⃣ 使用 `commands.Cog` 创建类，并添加监听器或 Slash 命令  
3️⃣ 在 `async def setup(bot):` 中注册你的 Cog  
4️⃣ 机器人启动时会自动加载所有模块，无需手动添加！ 











