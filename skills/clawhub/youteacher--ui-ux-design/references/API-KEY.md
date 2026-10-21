# API 密钥

推荐在平台创建通用 Key，并执行 `openclaw config set env.AI_SKILLS_API_KEY "你的平台APIKey"` 和 `openclaw gateway restart`，全平台 Skill 只需配置一次。仍需开通目标产品。下列 `UI_UX_DESIGN_API_KEY` 配置是兼容的产品专用覆盖项；调用优先使用该变量，为空时回退到 `AI_SKILLS_API_KEY`。两个变量均缺失时停止调用，不发送空 Bearer 请求。不要把旧请求换 Key 自动重试；幂等记录按 Key 隔离。


默认 API 根地址为 `https://ai-skills.open-idea.net/api/v1`；仅在平台运营方明确给出自托管地址时设置 `AI_SKILLS_API_URL`。密钥环境变量为 `UI_UX_DESIGN_API_KEY`。

每次请求使用：

```text
Authorization: Bearer ${UI_UX_DESIGN_API_KEY:-$AI_SKILLS_API_KEY}
Content-Type: application/json
Idempotency-Key: 每次新任务生成的新 UUID
```

不要在聊天、日志、截图或产物中显示完整密钥。此 Skill 使用平台本地规则生成基础设计方案，不需要 Figma 账号、第三方模型 Key 或第三方付费服务。

## 费用

- `design.plan` 生成设计方案：默认 ¥0.50/份。
- `design.checklist` 获取验收清单：免费。

价格可由管理员调整，以[UI/UX 设计助手产品页面](https://ai-skills.open-idea.net/skills/ui-ux-design)以及响应头 `X-AI-Skills-Billing-Currency`、`X-AI-Skills-Billing-Charged`、`X-AI-Skills-Billing-Balance` 为准。执行付费操作前向用户说明会扣除平台余额。
