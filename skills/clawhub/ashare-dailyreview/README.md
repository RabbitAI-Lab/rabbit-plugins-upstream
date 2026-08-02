# AShare Daily Review（A股复盘）

面向有短线交易经验的 A 股投资者的 Cursor / OpenClaw Agent Skill：收盘后按固定结构输出盘面综述、题材预期、热点梳理、连板容量弹性（含仓位与情绪票）。

> 免责声明：本 skill 输出仅为盘面梳理与交易思路参考，不构成投资建议。

## 仓库内容

| 文件 | 说明 |
|------|------|
| `SKILL.md` | Skill 主文件（触发条件、数据收集、文风、输出模板） |
| `examples.md` | 文风锚点示例 |

## 安装

### Cursor

复制到个人 skills 目录：

```bash
# Windows
xcopy /E /I SKILL.md %USERPROFILE%\.cursor\skills\fupan\
copy examples.md %USERPROFILE%\.cursor\skills\fupan\
```

或把整个仓库放到 `~/.cursor/skills/fupan/`（需包含 `SKILL.md`）。

### ClawHub

```bash
clawhub install ashare-daily-review
```

（发布后可用；slug 以 ClawHub 页面为准。）

## 发布到 ClawHub

需已安装 [clawhub CLI](https://github.com/openclaw/clawhub) 并登录：

```bash
clawhub login
clawhub publish . --slug ashare-daily-review --name "A股复盘" --version 1.0.0 --changelog "Initial release: A-share daily review skill"
```

## 触发词

复盘、今日盘面、收盘总结、明日预期、盘面分析、题材梳理；或发送收盘截图 / 板块涨跌 / 自选股列表。

## License

MIT
