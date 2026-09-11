# API 密钥

默认 API 根地址为 `https://ai-skills.open-idea.net/api/v1`；仅在平台运营方明确给出自托管地址时设置 `AI_SKILLS_API_URL`。密钥环境变量为 `UI_UX_DESIGN_API_KEY`。

每次请求使用：

```text
Authorization: Bearer $UI_UX_DESIGN_API_KEY
Content-Type: application/json
Idempotency-Key: 每次新任务生成的新 UUID
```

不要在聊天、日志、截图或产物中显示完整密钥。此 Skill 使用平台本地规则生成基础设计方案，不需要 Figma 账号、第三方模型 Key 或第三方付费服务。

## 费用

- `design.plan` 生成设计方案：默认 ¥0.50/份。
- `design.checklist` 获取验收清单：免费。

价格可由管理员调整，以[UI/UX 设计助手产品页面](https://ai-skills.open-idea.net/skills/ui-ux-design)以及响应头 `X-AI-Skills-Billing-Currency`、`X-AI-Skills-Billing-Charged`、`X-AI-Skills-Billing-Balance` 为准。执行付费操作前向用户说明会扣除平台余额。
