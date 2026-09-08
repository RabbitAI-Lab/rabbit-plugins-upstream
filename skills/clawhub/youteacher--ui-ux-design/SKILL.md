---
name: ui-ux-design
description: "使用场景: 用户要求规划、实现、改版或检查网页端、Flutter、React Native、iOS、Android 或微信小程序界面，并需要平台化设计约束与验收清单时。"
metadata:
    {
        "packageVersion": "1.1.0",
        "openclaw":
            {
                "emoji": "🎨",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "UI_UX_DESIGN_API_KEY",
                "requires": { "env": ["UI_UX_DESIGN_API_KEY"] },
            },
    }
---

# UI/UX 设计

## Skill 简介

UI/UX 设计助手用于把产品目标转换为可执行的界面方案，并在用户提供项目或截图时完成检查、实现和验证。支持响应式网页端、Flutter、React Native、iOS、Android 与微信小程序，不强制更换现有技术栈或组件库。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys) 创建并复制 API 密钥。

## Skill 安装与配置

1. 在 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API 密钥。
2. 在 OpenClaw 中安装 `ui-ux-design` Skill。
3. 将复制的密钥配置到本 Skill 的 API 密钥环境变量，然后重启 Gateway：

```sh
openclaw config set env.UI_UX_DESIGN_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## Skill 使用

1. 先识别目标平台、核心用户任务、现有技术栈和交付物。用户已提供项目、页面、截图或设计系统时，先检查这些材料。
2. 需要形成设计合同或补齐遗漏时，调用“生成设计方案”操作 `design.plan`；只需要检查某类风险时，调用免费的“获取验收清单”操作 `design.checklist`。
3. 设计方案必须覆盖信息架构、视觉 Token、加载/空数据/错误/权限/成功状态、无障碍、屏幕适配和平台特有行为。
4. 用户要求实现时，在其现有项目内修改并运行；网页端通过目标宽度截图检查，App 优先通过真机或模拟器检查。不能运行时，交付代码并列明未验证项目。
5. 只有实际检查过的结果才写成“已通过”；设计建议、代码实现和运行验证分别说明。

## 平台选择

- 网页端：响应式布局、键盘操作、浏览器缩放和窄屏信息重排。
- Flutter / React Native：安全区域、键盘避让、字体缩放以及 iOS/Android 返回差异。
- iOS / Android：遵循各自系统导航、手势、控件和无障碍语义。
- 微信小程序：关注授权触发、包体、弱网和机型安全区域。

## 参考资料

- [API 密钥配置](https://ai-skills.open-idea.net/skill-docs/ui-ux-design/API-KEY.md)
- [HTTP 请求与任务轮询](https://ai-skills.open-idea.net/skill-docs/ui-ux-design/HTTP-REQUESTS.md)
- [网页端与 App 平台指南](https://ai-skills.open-idea.net/skill-docs/ui-ux-design/PLATFORM-GUIDE.md)
- [行为与验收规则](https://ai-skills.open-idea.net/skill-docs/ui-ux-design/BEHAVIOR-RULES.md)
