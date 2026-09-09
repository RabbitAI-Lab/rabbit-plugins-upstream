---
name: product-operations
description: "使用场景: 用户需要把产品或活动目标转换为可执行运营计划、用真实汇总数据计算漏斗与 ROI、执行上线检查，或导出任务和复盘文件时。"
metadata:
    {
        "packageVersion": "1.1.0",
        "openclaw":
            {
                "emoji": "📈",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "PRODUCT_OPERATIONS_API_KEY",
                "requires": { "env": ["PRODUCT_OPERATIONS_API_KEY"] },
            },
    }
---

# 产品运营

## Skill 简介

产品运营助手把目标转换为带日期、负责人、优先级和验收指标的任务计划，并使用后端公式计算点击率、漏斗转化率、目标完成率、转化成本、增长率和 ROI。它也能生成上线检查清单，并将计划或复盘导出为 CSV、Excel、Markdown；运营计划还可导出系统日历文件。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys) 创建并复制 API 密钥。

## Skill 安装与配置

1. 在 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API 密钥。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的密钥配置到本 Skill 的 API 密钥环境变量，然后重启 Gateway：

```sh
openclaw config set env.PRODUCT_OPERATIONS_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## Skill 使用

1. 制定新计划时，收集产品名称、明确目标、日期范围、执行渠道、预算和团队人数，调用“制定运营计划”操作 `operation.plan`。
2. 复盘时只使用用户提供的真实数据。可读取用户指定的 CSV 或 XLSX，在本地提取曝光、访问、线索、转化、收入和成本后调用“复盘运营数据”操作 `operation.review`；不得上传原始文件或自行补造缺失数据。
3. 发布产品、活动、App 版本、促销、内容专题或召回任务前，调用免费的“获取运营检查清单”操作 `operation.checklist`。
4. 用户需要文件时，对成功的计划或复盘任务调用“导出运营结果”操作 `operation.export`。只能使用当前用户、当前 Skill 的成功来源任务 ID。
5. 指标结果由平台确定性计算。解释结论时区分原始数据、计算结果和行动建议，不把相关性写成因果关系。

## 参考资料

- [API 密钥配置](https://ai-skills.open-idea.net/skill-docs/product-operations/API-KEY.md)
- [HTTP 请求与任务轮询](https://ai-skills.open-idea.net/skill-docs/product-operations/HTTP-REQUESTS.md)
- [操作与字段说明](https://ai-skills.open-idea.net/skill-docs/product-operations/OPERATIONS.md)
- [指标与行为规则](https://ai-skills.open-idea.net/skill-docs/product-operations/BEHAVIOR-RULES.md)
