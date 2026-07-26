# Gmail IMAP PR 邮件管理

## 用途

定期检查邮箱中的 GitHub PR 通知邮件，及时响应审查意见。

## 配置

- 账号：lrg913427@gmail.com
- 需要 Gmail App Password（不是普通密码）
- 设置地址：https://myaccount.google.com/apppasswords

## 操作流程

1. 连接 Gmail IMAP
2. 搜索 `FROM "notifications@github.com"`
3. 读取邮件内容，识别需要处理的 PR
4. 按 pr-workflow-discipline 处理
5. 删除已停止跟踪的 PR 邮件（不要删其他邮件）

## 注意

- IMAP 连接可能被代理干扰 → 先 `unset HTTP_PROXY HTTPS_PROXY`
- 不要删非 PR 相关邮件
- 每次 PR 动作（推代码、回复审查、CI 通过/失败）都更新 Obsidian 笔记
