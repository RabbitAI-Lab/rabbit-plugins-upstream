---
name: presentation-generation
description: "使用场景: 用户要求把简报、文档或表格整理为带来源引用的可编辑演示文稿时。"
license: MIT-0
metadata:
    {
        "packageVersion": "1.2.0",
        "openclaw": {
            "emoji": "📊",
            "homepage": "https://ai-skills.open-idea.net",
            "primaryEnv": "PRESENTATION_GENERATION_API_KEY",
            "requires": {
                "bins": ["curl"]
            },
            "envVars": [
                {
                    "name": "AI_SKILLS_API_KEY",
                    "required": false,
                    "description": "通用平台 Key；与产品专用变量任选其一。"
                },
                {
                    "name": "PRESENTATION_GENERATION_API_KEY",
                    "required": false,
                    "description": "AI Skills 平台演示文稿生成 API 密钥。"
                },
                {
                    "name": "AI_SKILLS_API_URL",
                    "required": false,
                    "description": "可选 API 根地址。"
                }
            ]
        }
    }
---

# 演示文稿生成

## Skill 简介

演示文稿生成 Skill 先从简报或 TXT、Markdown、DOCX、PDF、CSV、XLSX 提取带位置引用的来源，再生成 6–15 页可审核大纲，最后使用 PptxGenJS 4.0.1、LibreOffice 和 Poppler 在平台内本地生成可编辑 PPTX、PDF 和逐页 PNG。不联网找图，不调用图片生成，不要求用户配置第三方付费凭据。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## Skill 安装与配置

当前控制台直接创建通用 Key，无需选择产品；每个账号最多保留一把未撤销的通用 Key，已有时直接复制复用，更换时先撤销旧 Key。下列产品选择说明适用于旧版控制台。

1. 在 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API 密钥。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的密钥配置到本 Skill 的 API 密钥环境变量，然后重启 Gateway：

```sh
openclaw config set env.AI_SKILLS_API_KEY "你的平台APIKey"
openclaw gateway restart
```

推荐创建账号通用 Key，以上全局变量只需配置一次即可供各 Skill 使用；仍需在产品管理中开通目标产品。原有产品专用 Key 仅能调用对应产品。

兼容旧配置：如需隔离本产品，可改用 `openclaw config set env.PRESENTATION_GENERATION_API_KEY "你的平台APIKey"`，然后重启 Gateway。调用时优先读取 `PRESENTATION_GENERATION_API_KEY`，为空时读取 `AI_SKILLS_API_KEY`；两者均缺失时停止调用并引导创建密钥。不要输出、记录或要求用户在对话中粘贴完整密钥。


## Agent 执行规则

1. 按 `presentation.inspect` → `presentation.outline` → `presentation.generate` 执行。先说明材料可读范围，再让用户复核大纲；用户要求生成文件后才执行最后一步。
2. 数字结论必须引用已冻结的 section ID；不得补写新数据、URL、路径、HTML、脚本、远程图片或任意模板。
3. 大纲只能使用 `title`、`section`、`bullets`、`two-column`、`quote`、`metric-cards`、`table`、`chart`、`timeline`、`summary` 版式和 `clear`、`midnight`、`warm` 主题。
4. 编辑只能更改标题、顺序、正文、要点、备注和版式，不得篡改来源引用。产物只通过当前用户的私有下载入口交付。

## 完成标准

- 轮询到终态；网络结果不确定时保留原 `Idempotency-Key` 和完全相同输入，`reconciliation_required` 不得自动重试或声称已退款。
- 交付前说明页数、主题、用户编辑、来源引用和质检结果。`partial` 只表示 PPTX 可交付但部分预览或质检失败，不得称为完整成功。
- 演示文稿仍需业务、数据和品牌负责人复核。发布、发送或写入外部系统前必须另行获得授权。

## 参考资料

按当前任务读取对应资料；无需预读全部文档。

- [API 密钥配置与价格](https://ai-skills.open-idea.net/skill-docs/presentation-generation/API-KEY.md)
- [操作字段、大纲与导出](https://ai-skills.open-idea.net/skill-docs/presentation-generation/OPERATIONS.md)
- [HTTP 请求、幂等与任务轮询](https://ai-skills.open-idea.net/skill-docs/presentation-generation/HTTP-REQUESTS.md)
- [隐私、复核与部分结果](https://ai-skills.open-idea.net/skill-docs/presentation-generation/BEHAVIOR-RULES.md)
