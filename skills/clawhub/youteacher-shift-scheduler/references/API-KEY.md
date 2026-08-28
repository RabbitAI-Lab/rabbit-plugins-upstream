# API Key

默认 API 根地址为 `https://ai-skills.open-idea.net/api/v1`；仅在平台运营方明确提供自托管地址时设置 `AI_SKILLS_API_URL`。密钥变量为 `SHIFT_SCHEDULER_API_KEY`。

```text
Authorization: Bearer $SHIFT_SCHEDULER_API_KEY
Content-Type: application/json
Idempotency-Key: 每次新排班动作使用的新 UUID
```

不要把完整 Key 写入聊天、日志或导出文件。Skill 使用平台本地能力，不配置 Provider，不需要外部模型或第三方付费服务。

## 费用与账户

从 ClawHub 安装 Skill 免费。调用 AI Skills 平台需要注册账号、开通“智能排班”并使用平台钱包余额；平台只对成功操作扣费。当前默认价格为：

- `schedule.generate`：¥0.50/份
- `schedule.read`：免费
- `schedule.update`：¥0.20/次
- `schedule.export`：¥0.15/份

价格可能由平台管理员调整，实际金额以[智能排班产品页面](https://ai-skills.open-idea.net/skills/shift-scheduler)及响应中的 `X-AI-Skills-Billing-Charged`、`X-AI-Skills-Billing-Currency` 和 `X-AI-Skills-Billing-Balance` 为准。执行付费操作前向用户说明会扣除平台余额。
