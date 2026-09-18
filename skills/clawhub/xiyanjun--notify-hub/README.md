# notify-hub

> 你的选股扫描、监控告警、日报周报，自动推送到飞书群。

一个 skill 抽象掉所有消息通道：定义一次内容（text / card / file），广播到飞书 / 企业微信 / 钉钉 / Slack / Telegram / 邮件。同一张卡片在各通道自动降级渲染——飞书是完整卡片，企微/钉钉转文本对齐，邮件转 HTML 表格。

## 特性

- **6 通道统一**：飞书 / 企业微信 / 钉钉 / Slack / Telegram / 邮件，一个 CLI 全搞定
- **统一卡片 DSL**：title + sections（markdown / table / button / note），各通道自动降级渲染
- **多通道广播**：`--to all` 或逗号分隔，一份内容同时推多个群
- **内置签名与限流**：飞书 / 钉钉 HMAC-SHA256 加签，各通道按频率上限自动节流
- **零依赖**：纯 Python 标准库（3.7+），无第三方包
- **凭据隔离**：凭据存 `~/.notify-hub/config.json`（权限 0600），不落仓库

## 快速开始

```bash
# 0. 零配置体验：预览同一张卡片在各通道的渲染效果（无需任何凭据）
python3 scripts/notify.py send card examples/card_report.json --dry-run

# 1. 添加目标
python3 scripts/notify.py config add feishu 我的群 --url https://open.feishu.cn/open-apis/bot/v2/hook/xxx --secret xxx
python3 scripts/notify.py config add wecom 我的群 --url https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx

# 2. 连通性测试
python3 scripts/notify.py test --to feishu:我的群

# 3. 发文本
python3 scripts/notify.py send text "收盘提醒：沪指 +0.5%" --to feishu:我的群

# 4. 发卡片（统一 DSL，各通道自动降级渲染）
python3 scripts/notify.py send card examples/card_report.json --to feishu:我的群,wecom:我的群

# 5. 广播到所有已配置通道
python3 scripts/notify.py send card examples/card_report.json --to all

# 6. 发文件（邮件附件 / Telegram 文档）
python3 scripts/notify.py send file report.pdf --to email:老板 --title "今日报告"
```

## 通道支持

| 通道 | name | 接入方式 | 卡片降级 |
|------|------|---------|---------|
| 飞书 | feishu | 群机器人 webhook（支持加签） | 完整卡片（表格+按钮） |
| 企业微信 | wecom | 群机器人 webhook | 表格→文本对齐，按钮→链接 |
| 钉钉 | dingtalk | 群机器人 webhook（支持加签） | 表格→文本对齐 |
| Slack | slack | incoming webhook | blocks |
| Telegram | telegram | Bot token + chat_id | HTML + inline keyboard |
| 邮件 | email | SMTP | HTML（表格转 table） |

详细凭据字段与降级矩阵见 [`references/channels-schema.md`](references/channels-schema.md)。

## 统一卡片 DSL

```json
{
  "kind": "card",
  "title": "今日扫描 Top5",
  "color": "blue",
  "sections": [
    {"type": "markdown", "content": "**命中 367 只**"},
    {"type": "table", "headers": ["代码", "名称", "评分"], "rows": [["600583", "海油工程", "114.7"]]},
    {"type": "button", "text": "查看完整报告", "url": "https://example.com"},
    {"type": "note", "content": "数据仅供参考"}
  ]
}
```

## 卡片降级对比

同一张卡片在 6 个通道的渲染效果差异很大——飞书是完整卡片（表格+按钮），企微/钉钉降级为文本对齐，邮件转 HTML 表格。浏览器打开 [examples/card-preview.html](examples/card-preview.html) 看对比，或直接跑：

```bash
python3 scripts/notify.py send card examples/card_report.json --dry-run
```

## 测试

```bash
python3 -m unittest discover -s tests -v
```

## 安全

- 凭据即权限：webhook / token / SMTP 密码一旦泄漏，任何人都能替你发消息。`~/.notify-hub/config.json` 请勿提交公开仓库。
- 本项目只向你自己配置的目标发送，不读取任何通道内容，不上传第三方。
- 推送到群 = 公开发言，发送前确认内容适合该目标。

## License

[MIT-0](LICENSE)
