---
name: agent-mailbox
description: Use when a bot or person needs to install, authorize, or operate an Agent mailbox (agent.qq.com / agently-cli) — install failures, OAuth login, send/reply with two-step confirmation, attachments.
version: 1.0.0
---

# Agent Mailbox（agently-cli）

一张邮箱，人和 Agent 通用。本技能同时覆盖**安装 → 授权 → 收发 → 排错**全链路。

## 0. 判断当前处境

| 情况 | 跳转 |
|---|---|
| 机器上还没有 `agently-cli` | 第 1 节 |
| 有 CLI，但不知道绑的是哪个邮箱 | 第 2 节 |
| 授权过期 / 401 | 第 3 节 |
| 要发信、回信、带附件 | 第 4 节 |
| 报错看不懂 | 第 6 节 |

## 1. 安装

前提：Node.js ≥ 18。检查：

```bash
node -v && npm -v
```

没有 Node（或报 `exec: node: not found`）：

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
source ~/.bashrc
nvm install 20
```

装 CLI：

```bash
npm install -g @tencent-qqmail/agently-cli
agently-cli --version
```

国内网络先换源：`npm config set registry https://registry.npmmirror.com`

## 2. 确认身份（每次会话第一步）

```bash
agently-cli +me
```

返回的 `email` 才是真实地址。**禁止**凭记忆、凭别人转述填写发件身份。

## 3. 授权

```bash
agently-cli auth status     # 先看状态
agently-cli auth login      # 未授权时
agently-cli auth refresh    # token 快过期
agently-cli auth logout     # 换账号前
```

`auth login` 会打印**一次性授权链接**：把它发给用户，让用户在浏览器打开并登录。链接几分钟失效，过期就重新执行。

在后台/无 TTY 环境执行时必须用 `background + pty`，从 stdout 抓链接，不要把命令卡死在前台。

## 4. 收发

```bash
# 收
agently-cli message +list --limit 10
agently-cli message +list --is-unread
agently-cli message +read --id msg_xxx
agently-cli message +search --q "keyword"

# 发 / 回
agently-cli message +send --to a@b.com --subject "标题" --body "正文"
agently-cli message +reply --id msg_xxx --body "内容"
agently-cli message +reply --id msg_xxx --reply-all --body "内容"

# 长正文
agently-cli message +send --to a@b.com --subject "标题" --body-file ./body.md

# 附件（必须相对当前目录）
agently-cli message +send --to a@b.com --subject "标题" --body "见附件" --attachment ./report.pdf
agently-cli attachment +download --msg msg_xxx --att att_xxx --output ./downloads
```

正文常为 HTML，先剥标签再理解。

## 5. 两步确认（最高频的坑）

首次 `+send` / `+reply` 只返回 `confirmation_token`，**不会真正发出**。5 分钟内带 token 再调一次：

```bash
agently-cli message +send ... --confirmation-token ctk_xxx
```

或直接 `--confirmed` 跳过。**拿 token 与发送必须同一个 shell 连着做**，中间不要开新终端、不要查日志，否则超时作废。

## 6. 报错对照

| 报错 | 原因 | 处理 |
|---|---|---|
| `exec: node: not found` | 缺 Node / PATH 未刷新 | 装 Node 后重开终端 / `source ~/.nvm/nvm.sh` |
| `EACCES` | 全局目录权限 | `sudo npm i -g ...` |
| `command not found` | npm bin 不在 PATH | `npm bin -g` 加入 PATH |
| 401 / Invalid token | 授权失效 | `auth refresh` → 仍失败则 `auth logout` + `auth login` |
| 链接打不开 | 授权链接一次性且已过期 | 重跑 `auth login` |
| 发件 queued 但没送达 | 缺第二步确认 | 补 `--confirmation-token` |
| 附件丢失 | 绝对路径 / 过大 | 用 `./相对路径`；大文件先压缩 |

## 7. 铁律

- 收信必回执，不空回、不沉默。
- 密码、密钥、验证码**绝不**写进邮件正文，也绝不经聊天窗口传递。
- 发信前 `--dry-run` 自检收件人、抄送、主题。
- 对外邮件按组织要求统一抄送审计地址。
- 换账号先 `auth logout`，避免凭据残留。
