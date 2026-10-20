---
name: ui-ux-design
description: "使用场景: 用户需要通过平台生成网页或 App 的 UI/UX 设计方案、验收清单并用于实现或检查时。"
license: MIT-0
metadata:
    {
        "packageVersion": "1.3.0",
        "openclaw": {
            "emoji": "🎨",
            "homepage": "https://ai-skills.open-idea.net",
            "primaryEnv": "UI_UX_DESIGN_API_KEY",
            "envVars": [
                {
                    "name": "AI_SKILLS_API_KEY",
                    "required": false,
                    "description": "通用平台 Key；与产品专用变量任选其一。"
                },
                {
                    "name": "UI_UX_DESIGN_API_KEY",
                    "required": false,
                    "description": "兼容产品专用 Key；设置时优先使用。"
                }
            ]
        }
    }
---

# UI/UX 设计

## Skill 简介

UI/UX 设计助手用于把产品目标转换为可执行的界面方案，并在用户提供项目或截图时完成检查、实现和验证。支持响应式网页端、Flutter、React Native、iOS、Android 与微信小程序，不强制更换现有技术栈或组件库。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys) 创建并复制 API 密钥。

## Skill 安装与配置

当前控制台直接创建通用 Key，无需选择产品；每个账号最多保留一把未撤销的通用 Key，已有时直接复制复用，更换时先撤销旧 Key。下列产品选择说明适用于旧版控制台。

1. 在 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API 密钥。
2. 在 OpenClaw 中安装 `ui-ux-design` Skill。
3. 将复制的密钥配置到本 Skill 的 API 密钥环境变量，然后重启 Gateway：

```sh
openclaw config set env.AI_SKILLS_API_KEY "你的平台APIKey"
openclaw gateway restart
```

推荐创建账号通用 Key，以上全局变量只需配置一次即可供各 Skill 使用；仍需在产品管理中开通目标产品。原有产品专用 Key 仅能调用对应产品。

兼容旧配置：如需隔离本产品，可改用 `openclaw config set env.UI_UX_DESIGN_API_KEY "你的平台APIKey"`，然后重启 Gateway。调用时优先读取 `UI_UX_DESIGN_API_KEY`，为空时读取 `AI_SKILLS_API_KEY`；两者均缺失时停止调用并引导创建密钥。不要输出、记录或要求用户在对话中粘贴完整密钥。


## Skill 使用

1. 先识别目标平台、核心用户任务、现有技术栈和交付物。用户已提供项目、页面、截图或设计系统时，先检查这些材料。
2. 需要形成设计合同或补齐遗漏时，调用“生成设计方案”操作 `design.plan`；只需要检查某类风险时，调用免费的“获取验收清单”操作 `design.checklist`。
3. 设计方案必须覆盖信息架构、视觉 Token、加载/空数据/错误/权限/成功状态、无障碍、屏幕适配和平台特有行为。
4. 用户要求实现时，在其现有项目内修改并运行；网页端通过目标宽度截图检查，App 优先通过真机或模拟器检查。不能运行时，交付代码并列明未验证项目。
5. 只有实际检查过的结果才写成“已通过”；设计建议、代码实现和运行验证分别说明。

## 平台选择

根据用户项目选择网页端、Flutter / React Native、iOS / Android 或微信小程序；平台特有的导航、适配与无障碍要求查 PLATFORM-GUIDE.md 对应小节，无需同时检查无关平台。

## 完成标准

- 在用户已授权范围内完成请求；收到异步任务时持续轮询任务状态，按 HTTP-REQUESTS.md 的终态与等待上限停止。未规定上限时，开始轮询前设定有限等待预算；超时保留任务 ID、最后状态与查询方式，不宣称成功或失败、不重复提交。
- 429/503 等可恢复错误按参考规则有限退避；同一逻辑请求复用原 `Idempotency-Key` 和相同输入。结果不确定或规则要求人工核对时停止自动重试；已授权范围内的安全续查无需重复确认。
- 多文件或多步骤任务完成后逐项交付结果；部分失败、仍在处理或等待人工核对的项目分别说明，并给出下一步。

## 参考资料

按当前任务读取对应资料；无需预读全部文档。

- 首次配置或排查鉴权时：[API 密钥配置](https://ai-skills.open-idea.net/skill-docs/ui-ux-design/API-KEY.md)
- 调用 API 前，确认请求、响应与重试规则：[HTTP 请求与任务轮询](https://ai-skills.open-idea.net/skill-docs/ui-ux-design/HTTP-REQUESTS.md)
- 设计或实现时，只读目标平台小节：[网页端与 App 平台指南](https://ai-skills.open-idea.net/skill-docs/ui-ux-design/PLATFORM-GUIDE.md)
- 执行前，确认本次授权、安全与结果解释边界：[行为与验收规则](https://ai-skills.open-idea.net/skill-docs/ui-ux-design/BEHAVIOR-RULES.md)
