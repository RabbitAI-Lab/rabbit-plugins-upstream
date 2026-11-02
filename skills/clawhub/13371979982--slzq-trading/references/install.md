# 安装、升级与发布（维护者 / 本机安装）

> 运行时规则在上级 `SKILL.md`。本页给人装包、发版用，健康检查不要读。

## 环境变量

| 变量 | 说明 |
|------|------|
| `SLZQ_OPENCLAW_DOMAIN` | `https://` + 主机名；网关前缀要带上，结尾不要 `/mobile-api` |
| `SLZQ_OPENCLAW_API_KEY` | 模拟盘可会话内领取；实盘在小立助理个人中心绑定 |
| `SLZQ_OPENCLAW_ENV` | 默认 `sim`；实盘 `live` |

zip 地址含 `/sanli/mobile-api/` 时，域名填到 `https://主机名/sanli`。

## ClawHub

1. `npm i -g clawhub` 后 `clawhub login`
2. `clawhub install slzq-trading`（slug 以首次 publish 为准）
3. 在 OpenClaw Skills 填 API Key / 环境变量；新开会话
4. 宿主支持 MCP 时注册 `runtime/mcp/dist/index.js`（ClawHub 包）或独立 `slzq-trading-mcp`

升级：`clawhub update slzq-trading`

## 自托管 zip（与 App 下载一致）

1. `{SLZQ_OPENCLAW_DOMAIN}/mobile-api/static/openclaw/slzq-trading.zip`（URL 勿夹密钥）
2. 解压到 workspace `skills/slzq-trading/`
3. 无 Key 可先跳过，会话内按 `api-auth.md` 领取
4. 连通：对智能体说「健康检查」，只打 `health`。`doctor.sh` / `test_connection.sh` / `test_mcp_tools.sh` / `npm ci` **只给人在自己的终端跑**，禁止在智能体会话里执行（stdout 和 `tools/list` schema 会进上下文）。

## 连通测试（不要下单）

连通口令只调 `health`。不要为了自检去打 `skill/version` / `me`，也不要拉热门合约、快照、持仓或成交，不要 `tools/list` 全文。

## 维护者发版

- 版本与 `VERSION`、`SKILL.md` frontmatter、MCP `package.json` 同步递增 semver
- 自托管 zip：仓库脚本 `scripts/package-slzq-trading-skill.sh`
- ClawHub：改 `static/openclaw/clawhub/overlay/` 后执行 `clawhub/build.cmd`，上传生成目录 `clawhub/slzq-trading/`（网页或 `clawhub skill publish`，slug `slzq-trading`）
- 没有 `scripts/publish-slzq-trading-clawhub.sh`；华源才有 hyqh 那份
- publish 目录不要含 `.git`

## MCP

Node ≥ 18。`npm ci && npm run build`，入口 `dist/index.js`。注入示例见 `runtime/mcp/README.md` 或独立包 `slzq-trading-mcp/README.md`。

`npm run test:mcp-tools` 至少应看到 auth/health/me/行情/持仓/下单/云单及 `slzq_open_v1_skill_prefs_mute_stop_profit_loss_reminder`。
