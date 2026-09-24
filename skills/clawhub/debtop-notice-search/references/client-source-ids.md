# 客户端标识对照表（`source` 取值）

> 输出详情链接时，`source` 按本表取值（规则见 SKILL.md §五「链接必须带来源标识」）。
> 本表取值同时用于两处：① 输出详情链接的 `source` 参数；② 创建游客时上报的 `skillId`（游客归属，见 `references/guest-access.md`）。同一客户端两处必须一致。
> 表内为**已约定**取值，直接采用；表里没有的客户端，按命名规则自造（小写 + 短横线）并在团队内登记，避免统计口径分裂。**同一产品多端共用一个标识**。

**命名规则**：小写英文 + 短横线（纯 ASCII）；同产品的 App / Web / 插件 / IDE 统一用一个标识，不加版本号或端类型；判断不出客户端时用 `mcp`。

**办公 / 通用 AI 助手**

| 客户端 / 平台 | 标识 |
|---|---|
| 千问办公 | `qwen-office` |
| 通义千问（阿里） | `qwen` |
| 豆包（字节） | `doubao` |
| 文心一言 / 文小言（百度） | `ernie` |
| 腾讯元宝 | `yuanbao` |
| Kimi（月之暗面） | `kimi` |
| 智谱清言（GLM） | `chatglm` |
| 讯飞星火 | `spark` |
| 秘塔 AI 搜索 | `metaso` |
| 天工（昆仑万维） | `tiangong` |
| 海螺 AI（MiniMax） | `hailuo` |
| 跃问（阶跃星辰） | `yuewen` |
| 商量 SenseChat（商汤） | `sensechat` |
| 纳米 AI（360） | `nami` |
| 盘古 / 小艺（华为） | `pangu` |
| ChatGPT | `chatgpt` |
| Claude | `claude` |
| Gemini | `gemini` |
| Grok（xAI） | `grok` |
| Perplexity | `perplexity` |
| Microsoft Copilot | `copilot` |
| Meta AI | `meta-ai` |
| Le Chat（Mistral） | `le-chat` |
| Poe | `poe` |
| Monica | `monica` |

**编程 / IDE Agent**

| 客户端 / 平台 | 标识 |
|---|---|
| WorkBuddy | `workbuddy` |
| CodeBuddy（腾讯云） | `codebuddy` |
| 通义灵码（阿里） | `lingma` |
| 文心快码 Comate（百度） | `comate` |
| Trae（字节） | `trae` |
| Qoder | `qoder` |
| Cursor | `cursor` |
| GitHub Copilot | `github-copilot` |
| Windsurf | `windsurf` |
| JetBrains AI | `jetbrains-ai` |
| Amazon Q | `amazon-q` |
| Cline | `cline` |
| Roo Code | `roo-code` |
| Continue | `continue` |
| Aider | `aider` |
| Zed | `zed` |
| Replit | `replit` |
| Devin | `devin` |

**Agent 平台 / 编排**

| 客户端 / 平台 | 标识 |
|---|---|
| 扣子 Coze（字节） | `coze` |
| Dify | `dify` |
| 阿里云百炼 | `bailian` |
| 腾讯元器 | `yuanqi` |
| 百度千帆 | `qianfan` |
| n8n | `n8n` |
| Manus | `manus` |
| Genspark | `genspark` |
| Zapier | `zapier` |

**企业协作 / 办公套件**

| 客户端 / 平台 | 标识 |
|---|---|
| 钉钉 AI 助理 | `dingtalk` |
| 飞书智能伙伴（Lark） | `feishu` |
| 企业微信 | `wecom` |
| Notion AI | `notion-ai` |
| Slack AI | `slack` |

**开源客户端 / 自建**

| 客户端 / 平台 | 标识 |
|---|---|
| Open WebUI | `open-webui` |
| LobeChat | `lobechat` |
| NextChat | `nextchat` |
| Cherry Studio | `cherry-studio` |
| Chatbox | `chatbox` |
| LibreChat | `librechat` |
| AnythingLLM | `anythingllm` |
| 兜底：自建 / 内部平台 / 判断不出客户端 | `mcp` |
