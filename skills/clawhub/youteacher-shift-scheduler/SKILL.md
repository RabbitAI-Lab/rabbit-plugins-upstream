---
name: shift-scheduler
description: "使用场景: 用户要求按日期、班次、员工可用性和劳动约束生成、读取、人工调整或导出智能排班，并希望通过 AI Skills 平台 API 获得结构化排班、PDF 与 CSV 时。"
license: MIT-0
metadata:
    {
        "packageVersion": "1.0.0",
        "openclaw":
            {
                "emoji": "📅",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "SHIFT_SCHEDULER_API_KEY",
                "requires":
                    { "env": ["SHIFT_SCHEDULER_API_KEY"], "bins": ["curl"] },
                "envVars":
                    [
                        {
                            "name": "SHIFT_SCHEDULER_API_KEY",
                            "required": true,
                            "description": "AI Skills 平台智能排班 API Key。",
                        },
                        {
                            "name": "AI_SKILLS_API_URL",
                            "required": false,
                            "description": "可选的自托管 API 根地址；未设置时使用官方平台。",
                        },
                    ],
            },
    }
---

# Shift Scheduler

## Skill 简介

智能排班 Skill 用于根据员工、班次、不可用日期和明确约束生成、读取、人工调整及导出排班，并提供结构化结果、私有 PDF 和 CSV。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## API Key 获取与配置

1. 在 API Key 管理中选择已开通的“智能排班”，创建并复制 API Key。
2. 在 OpenClaw 中安装 `shift-scheduler` Skill。
3. 将 Key 配置到本 Skill 的环境变量，然后重启 Gateway：

```sh
openclaw config set env.SHIFT_SCHEDULER_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## Skill 使用

配置完成后，用户可以直接说明排班周期、人员、班次和规则，例如：

- “为 6 名门店员工生成下周排班，每天早晚两班，每人最多 5 班。”
- “小王周三不可用，请重新安排并列出仍未填补的岗位。”
- “把当前排班导出为 PDF 和 CSV。”

## 参考资料

- [API Key 配置](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/shift-scheduler/references/API-KEY.md)：安装、配置或更换 Key 时阅读。
- [Operations 契约](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/shift-scheduler/references/OPERATIONS.md)：生成请求或确认成员、班次、约束和结果格式时阅读。
- [HTTP 请求与任务轮询](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/shift-scheduler/references/HTTP-REQUESTS.md)：调用 API、处理幂等或轮询任务时阅读。
- [行为与错误规则](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/shift-scheduler/references/BEHAVIOR-RULES.md)：处理缺失信息、未填岗位、版本冲突和劳动规则边界时阅读。
