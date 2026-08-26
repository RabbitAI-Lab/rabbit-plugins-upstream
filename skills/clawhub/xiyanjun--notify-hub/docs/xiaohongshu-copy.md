# notify-hub · 小红书文案（教程版 · 去敏感）

## 标题

如何让腾讯 workbuddy 产出的内容，推送到字节的飞书

## 正文

**第 1 步 · 拿代码**
GitHub 仓库（零依赖，纯 Python）：https://github.com/xiyanjun/notify-hub

**第 2 步 · 飞书群建机器人，拿 webhook**
飞书群 → 右上「设置」→ 群机器人 → 添加「自定义机器人」→ 复制 Webhook 地址（可勾选「签名校验」）。
官方文档：https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot

**第 3 步 · 把 webhook 配进去**
```bash
python3 scripts/notify.py config add feishu 我的群 \
  --url https://open.feishu.cn/open-apis/bot/v2/hook/xxx \
  --secret xxx
```

**第 4 步 · 推送**
```bash
# 发文本
python3 scripts/notify.py send text "日报已生成，请查收" --to feishu:我的群

# 发卡片（表格+按钮，自动适配）
python3 scripts/notify.py send card examples/card_report.json --to feishu:我的群

# 不确定长啥样？先零配置预览
python3 scripts/notify.py send card examples/card_report.json --dry-run
```

**第 5 步 · 接入 workbuddy 自动化**
· workbuddy 里用 `@skill:notify-hub`，作为日报 / 监控告警的收尾一步
· 或配一个 workbuddy 定时任务，跑完自动推

**链接汇总**
· 仓库：https://github.com/xiyanjun/notify-hub
· 飞书机器人文档：https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot

## 标签

#AI #AIAgent #AI工具 #WorkBuddy #飞书 #自动化 #Python #效率工具

## 首图文字

「WorkBuddy 产出 → 自动推送飞书」
