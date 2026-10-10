---
name: free-llm-installer
slug: free-llm-installer
displayName: 免费 LLM 一键安装
version: 1.0.3
description: 一键安装并实测验证已验证可用的免费 LLM 到 WorkBuddy/Claude Code，无需注册、无需 API Key。当用户说「装免费模型」「加免费模型」「免费 LLM」「免费模型一键装」「验证免费模型可用吗」「免费模型怎么接入」「帮我配几个免费模型」「监控免费模型」「免费模型挂了吗」「kilo 网关」「kilo-auto」「step-5-preview-free」「nemotron 免费」「space-bunny」「免费模型工具调用」时使用。也用于验证已有免费模型配置是否真的可用（tool calling 是否支持、是否限流、是否支持读图），以及定期 watch 监控免费模型是否下线/限流/失去工具调用能力。
agent_created: true
---

# 免费 LLM 一键安装与实测验证

## 核心原则

**「标 free」不等于「真能用」。** 本技能内置的模型都是逐个发真实请求
（含 function calling）验证过的。使用者不需要自己再验证一遍。

已踩过的坑，不要重复：

|坑 | 表现 | 正确做法 |
|---|---|---|
| 模型 id 被简化 | `kilo-auto-free` → 401 PAID_MODEL_AUTH_REQUIRED | 必须写完整 `provider/model:free` |
| 空 apiKey | 回落宿主平台 token → 鉴权失败 | 用单空格 `" "` |
| 假多模态 | 返回 200 但 `image_tokens=0`，模型瞎猜 | Kilo 三个模型都是这种，写 `supportsImages: false` |
| 误判假多模态 | Zen 侧 429 测不出读图，就武断写 false | **space-bunny-free 实测支持读图**，写 `true`（用户截图佐证） |
| 假工具调用 | 能对话但从不返回 `tool_calls` | 必须发带 `tools` 的请求实测 |
| Cloudflare拦 UA | 403 `code:1010` | 必须带浏览器 User-Agent |
| 标 free 但需充值 | 50 RPD / 1000 RPD 那种 | 只有本清单里的才是真免密 |

## 内置模型（2026-10-10 实测）

| 模型 id | 端点 | 上下文 | 工具调用 | 读图 |
|---|---|---|---|---|
| `kilo-auto/free` | Kilo Gateway | 256k | ✅ | ❌ |
| `nvidia/nemotron-3-ultra-550b-a55b:free` | Kilo Gateway | 1000k | ✅ | ❌ |
| `space-bunny-free` | OpenCode Zen | — | ✅ | ✅ |

- **Kilo Gateway**：`https://api.kilo.ai/api/gateway/v1/chat/completions`
  免注册免 key，18 个免费模型，是首选。
- **OpenCode Zen**：`https://opencode.ai/zen/v1/chat/completions`
  免key，但免费层已收紧为仅 `space-bunny-free` 可从 API 直连
  （其余报 403「free tier can only be used from within OpenCode」）。
  **`space-bunny-free` 支持读图**（用户实测确认：`supportsImages: false` 时
  WorkBuddy 贴图报 "does not support reading images"，设为 `true` 后识别成功）。

⚠️ **space-bunny-free 的免费额度绑在出口 IP 上，按 UTC 天重置（北京时间 08:00）。**
    不需要 key，也不看 UA/Cookie——**同一 IP 下所有用户共享一份日额度**。
    VPN / 代理 / 运营商 NAT 都可能让多人共用一个 IP，别人刷完你跟着锁。
    429 报错带 `Retry-After`（秒），指到 UTC 00:00 就是额度重置时间。
    证据：OpenCode Zen 维护者 GitHub issue #1659（同请求换出口 IP，429↔200）。
    → 排查：`api.ipify.org` 看出口 IP；换网络/换 VPN 出口再试，变 200 就证实。

**kilo-auto/free 和 nemotron 是纯文本模型，不支持读图。** 读图请用
`space-bunny-free`（Zen，真·免 key）。

## 执行流程

### 场景 A：用户要装免费模型

直接运行（脚本会自动备份 + 写入 + 实测验证）：

```bash
python scripts/install_free_llms.py
```

Windows 若`python` 不在 PATH，用：
```bash
py scripts/install_free_llms.py
```

跑完向用户报告：装了哪些、验证结果、以及建议把 `kilo-auto/free` 设为默认
（自动路由到当前可用模型，某个模型挂了会自动切换）。

### 场景 B：用户要验证已有配置

```bash
python scripts/install_free_llms.py --verify
```

这会发真实请求逐个验证。常见失败原因：

- `429` → 免费池高峰限流，等几分钟重试，**不是配置错**
- `401` → apiKey 写成了空串或id 被简化
- `未调工具` → 该模型不支持 function calling，不能用于 agent
- `HTTP404` → 模型已下线，用 `--refresh` 拉当前清单

### 场景 C：用户问「现在还有哪些免费模型」

```bash
python scripts/install_free_llms.py --refresh --dry-run
```

从服务端拉实时清单（只读，不写文件）。告诉用户哪些已在配置里、哪些可加。
**注意**：新拉到的模型不在实测清单内，必须先 `--verify` 确认工具调用可用再推荐。

### 场景 D：用户要清理

```bash
python scripts/install_free_llms.py --uninstall
```

只移除本脚本添加的（按 `vendor` 识别），保留用户自己的模型。

### 场景 E：用户问「免费模型还能用吗 / 有没有挂」

直接开监控（每轮每模型只发 **1 个**带 tools 的请求，额度消耗最低）：

```bash
python scripts/install_free_llms.py --watch
```

默认每 30 分钟一轮。**只在状态变化时报告**，正常时不刷屏。
状态分5 档：`OK` / `NO_TOOL`（能聊但工具调用挂了）/ `RATELIMIT`（限流，不算故障）/
`DOWN`（下线）/ `ERROR`。

长期挂机（Windows 可交给计划任务）：
```bash
python scripts/install_free_llms.py --watch --watch-interval 1800
```

跑固定轮数后自动退出（便于做定时任务）：
```bash
python scripts/install_free_llms.py --watch --watch-rounds 3 --watch-interval 3600
```

状态持久化在 `~/.workbuddy/free_llm_watch_state.json`，
首轮会写入基线状态，
之后每轮只追加一行变化记录（实测已抓到 `OK -> RATELIMIT -> OK` 双向切换）。

**汇报时必须转述**：RATELIMIT 是免费池正常现象，别让用户误以为模型挂了。

## 其他命令

```bash
python scripts/install_free_llms.py --list          # 列出已配置的模型
python scripts/install_free_llms.py --dry-run        # 只看要做什么，不写文件
python scripts/install_free_llms.py --force          # 覆盖同 id 的现有配置
python scripts/install_free_llms.py --deepseek-key sk-xxx   # 顺便加 DeepSeek
python scripts/install_free_llms.py --models /path/to/models.json  # 指定配置路径
python scripts/install_free_llms.py --watch --watch-log /path/to/watch.log   # 监控+自定义日志
```

## 监控相关参数

| 参数 | 默认 | 说明 |
|---|---|---|
| `--watch` | 关 | 开启定期探测模式 |
| `--watch-interval` | `1800`（秒） | 两轮之间的间隔 |
| `--watch-rounds` | 无限 | 跑够N 轮后自动退出 |
| `--watch-gap` | `1.0`（秒） | 同轮内模型间的请求间隔，避免打爆限流 |
| `--watch-log` | `~/.workbuddy/free_llm_watch.log` | 变化日志路径 |

## 关键实现细节

- **配置文件位置**：`~/.workbuddy/models.json`（脚本会自动探测，也支持
  `XDG_CONFIG_HOME`）。路径不存在时自动创建目录。
- **原子写入**：先写 `.tmp` 再 `os.replace`，避免写一半损坏配置。
- **每次写入前自动备份**到同目录 `backups/models.json.bak-install-free-<时间戳>`。
- **网络抖动重试**：SSL 中断等`NET` 类错误自动重试 2 次（间隔 3s）；
  429 限流在工具调用验证阶段重试 2 次（间隔 8s）。
- **非法 JSON 拒绝写入**：配置文件损坏时报错退出，不覆盖用户数据。
- **必须带浏览器 UA**：Kilo 和 Zen 前面都有 Cloudflare，Python 默认 UA 会被拦。

## 注意事项（转述给用户时用）

- 免费模型**不适合当生产主力**：50 RPD 级别的额度几天就烧完，agent 循环一轮要5-20 次调用。
- 免费池高峰会429，`kilo-auto/free` 的自动路由能缓解这个问题。
- 免费渠道的数据可能进上游训练集，**不要放密钥、用户数据、生产代码**。
- 政策随时变。`--refresh` 能查到当前真实情况，但「能列出来」≠「能调用」，
  仍需 `--verify` 确认。
- 免费模型会突然限流或下线。`--watch` 挂在后台跑就能第一时间知道，
  每个模型每轮只花 1 个请求，30 分钟一轮的话一天不到 200 个请求，额度完全无压力。