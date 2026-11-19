# Agent Mailbox（agent.qq.com）从零上手 · 人与机器人双视角

> 一个邮箱账号，一套 CLI，人和 AI Agent 都能收发信。
> 本文覆盖：**装不上、授权走不通、发信不回、附件带不上** 四类真实坑。

![platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-blue)
![node](https://img.shields.io/badge/node-%E2%89%A518-green)
![license](https://img.shields.io/badge/license-MIT-lightgrey)


> 🌐 在线版（可直接读、可下载）：http://1.14.104.78/agent-mailbox/

---

## 这个仓库解决什么问题

`agently-cli` 是腾讯 QQ 邮箱给 Agent 提供的命令行客户端。绝大多数人卡在三个地方：

1. **CLI 装不上** —— 机器上没有 Node，或者 npm 全局目录没权限；
2. **授权走不通** —— `auth login` 打印的链接是**一次性**的，几分钟就失效；
3. **发信不成功** —— 首次发送只返回 `confirmation_token`，很多人以为发成功了，其实没发。

本仓库给两套流程：**给人看的**（5 分钟上手）和**给 AI Agent 看的**（SKILL.md，可直接放进 Hermes / Claude Code 等技能目录）。

---

## 一、人：5 分钟上手

### 1. 装 Node（≥ 18）

```bash
# Linux / macOS
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
source ~/.bashrc
nvm install 20
node -v
```

Windows：装 <https://nodejs.org> 的 LTS 安装包，一路下一步。

### 2. 装 CLI

```bash
npm install -g @tencent-qqmail/agently-cli
agently-cli --version      # 有版本号即成功
```

国内网络建议先换源：

```bash
npm config set registry https://registry.npmmirror.com
```

### 3. 授权

```bash
agently-cli auth login
```

终端会打印一条授权链接 → **用浏览器打开** → 登录你要绑定的 Agent 邮箱账号 → 页面提示成功后，命令自动退出。

> ⚠️ 授权链接**一次性、几分钟内有效**。过期就重跑 `auth login`。

### 4. 确认你是哪个邮箱

```bash
agently-cli +me
```

返回的 `email` / `aliases` 才是你的真实地址，**别凭记忆填**。

### 5. 收发

```bash
# 收
agently-cli message +list --limit 10
agently-cli message +list --is-unread
agently-cli message +read --id msg_xxx
agently-cli message +search --q "关键词"

# 发
agently-cli message +send --to someone@example.com \
  --subject "标题" --body "正文"

# 回
agently-cli message +reply --id msg_xxx --body "收到，谢谢！"

# 带附件
agently-cli message +send --to someone@example.com \
  --subject "报表" --body "见附件" --attachment ./report.pdf

# 下载附件
agently-cli attachment +download --msg msg_xxx --att att_xxx --output ./downloads
```

### 6. 首次发信要二次确认

第一次调用 `+send` / `+reply` **不会真正发出**，只返回 `confirmation_token`：

```json
{ "confirmation_token": "ctk_xxx", "summary": { ... } }
```

**必须在 5 分钟内**带上它再调一次：

```bash
agently-cli message +send ... --confirmation-token ctk_xxx
```

或者一步到位：

```bash
agently-cli message +send ... --confirmed
```

---

## 二、机器人：把它当技能加载

`SKILL.md` 是标准技能文件（YAML frontmatter + 指令体），可直接放进：

```
~/.hermes/skills/<name>/SKILL.md
~/.claude/skills/<name>/SKILL.md
```

加载后 Agent 会自动：先 `+me` 确认身份 → 检查 `auth status` → 需要时 `auth login` → 再收发信。

---

## 三、排错速查表

| 现象 | 真正原因 | 解决 |
|---|---|---|
| `exec: node: not found` | 有 npm 没 node / PATH 未刷新 | 装 Node 后**重开终端**；nvm 用户先 `source ~/.nvm/nvm.sh` |
| `npm install` 卡住 | 官方源慢 | `npm config set registry https://registry.npmmirror.com` |
| `EACCES: permission denied` | 全局目录无权限 | `sudo npm install -g ...`；或 `npm config set prefix ~/.npm-global` |
| `agently-cli: command not found` | npm 全局 bin 不在 PATH | `npm bin -g` 查看并加入 PATH |
| 授权链接打不开 | 链接一次性、已过期 | 重跑 `agently-cli auth login` |
| 授权成功但命令报 401 | 本地 token 失效 | `agently-cli auth refresh`，仍不行则 `auth logout` 后重新 login |
| 发信返回 queued 但对方没收到 | 少了第二步确认 | 带 `--confirmation-token` 重发，或加 `--confirmed` |
| `ctk_` 无效 | 超过 5 分钟 | 重新发起一次发送 |
| 附件不生效 | 路径非相对路径 / 文件太大 | 用相对路径 `./file.pdf`；大文件先压 |
| 正文乱码/丢格式 | 纯文本里塞了 Markdown | 用 `--body-file ./body.md` |

---

## 四、安全铁律（人机都适用）

1. **授权码、密码、token 永远不进聊天窗口、不进邮件正文**。
2. 发信前 `--dry-run` 自检收件人、抄送、主题。
3. 对外邮件统一抄送自己的主管/审计地址。
4. 收到邮件必须回执，不空回、不沉默。
5. 换账号务必先 `auth logout`，避免把凭据留给下一个人。

---

## 五、给团队批量部署时

```bash
# 每台机器：装 CLI → 授权 → 验证一条链路
npm i -g @tencent-qqmail/agently-cli
agently-cli auth login
agently-cli +me
agently-cli message +list --limit 1
```

三行全过，这条邮箱链路才算通。任一步失败，按上面的排错表处理。

---

## License

MIT
