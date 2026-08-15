# @opc/skill-content-events

MCP Skill: read OPC events from OPC 一人公司 tool station via personal API Key.

Works with Claude Desktop / Cursor / Cline.

## Install

```bash
npx -y @opc/skill-content-events
```

## Quick Start

**第一步：获取 OPC 个人 API Key**
1. 打开 https://mrkjai.com 并登录/注册
2. 进入**个人中心/账户设置**
3. 找到「**个人集成(API Key)**」或「API Key」入口
4. 复制你的 Key（格式：`opc_user_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`）

**第二步：配置环境变量**
将 Key 配置到你的 AI 客户端 MCP 设置的 `OPC_API_KEY` 环境变量中。

**第三步：开始使用**
在 AI 助手中直接提问，例如：
> 「最近有什么北京地区的创业大赛？」

## Configure

Set these environment variables:

- `OPC_API_BASE` — OPC 站点地址，默认 `https://mrkjai.com`
- `OPC_API_KEY` — 你的个人 API Key（在个人中心/账户设置的「个人集成」页面获取）

## Tools

- `opc_list_events` — 读取赛事活动列表

## 关于作者

**桂皮 Guipi** — AI Agent 开发者 · 超级个体践行者
专注 AI 效率工具与一人公司方法论，帮普通人用 AI 成为超级个体

| 平台 | 账号 |
|------|------|
| 📱 小红书 | [桂皮AI实战](https://www.xiaohongshu.com/user/profile/5a409dda44363b313b9d7e15) |
| 🎬 抖音 | [桂皮AI实战](https://v.douyin.com/QJRjHGAtrvA/) |
| 📺 视频号 | 微信内搜「桂皮AI实战」|
| 💬 公众号 | 微信搜「桂皮AI实战」|
| 🐙 GitHub | [guipi888](https://github.com/guipi888) |
| 💬 微信 | guipi996（注明来意）|

## License

MIT
