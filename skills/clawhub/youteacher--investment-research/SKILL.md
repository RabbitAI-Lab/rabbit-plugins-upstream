---
name: investment-research
description: "使用场景: 用户需要检索公司公告或 XBRL 事实，并基于平台内真实来源任务生成带引用、无投资指令的风险分析或投资研究报告；需要 INVESTMENT_RESEARCH_API_KEY。"
metadata:
    {
        "packageVersion": "1.2.0",
        "openclaw":
            {
                "emoji": "📊",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "INVESTMENT_RESEARCH_API_KEY",
                "requires": { "env": ["INVESTMENT_RESEARCH_API_KEY"] },
            },
    }
---

# Investment Research

## Skill 简介

投资研究 Skill 用于检索公司公告和公开披露事实，提取可核验信息，并生成带来源、时间和风险说明的研究报告；它不提供投资指令。

## API Key 获取与配置

1. 注册并登录 AI Skills 平台，在「产品管理」中开通 Investment Research。
2. 进入「API Key」，选择该产品，创建并复制 API Key。
3. 在 OpenClaw 中安装本 Skill。
4. 将复制的 Key 配置到本 Skill 的 API Key 环境变量，然后重启 Gateway：

```sh
openclaw config set env.INVESTMENT_RESEARCH_API_KEY "你的平台APIKey"
openclaw gateway restart
```

不要把完整 Key 发到对话中或写入代码、日志和报告。

通过 AI Skills 平台检索公开申报证据并生成确定性的引用式研究。默认 API 根为
`https://ai-skills.open-idea.net/api/v1`。不要直连或
描述第三方 Provider endpoint。

## 执行流程

1. 按 [API Key 配置](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/investment-research/references/API-KEY.md)读取产品专属 Key，不回显完整值。
2. 从 [Operations 契约](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/investment-research/references/OPERATIONS.md)选择 operation，只发送白名单字段。
3. 按 [HTTP 请求与任务轮询](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/investment-research/references/HTTP-REQUESTS.md)为每个新逻辑 POST 生成 UUID。
4. 先取得真实 `filing.search`/`company.facts` 任务，再把其 `task_id` 作为
   `source_task_ids` 交给本地分析或报告。
5. 按 [来源、证据与投资安全规则](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/investment-research/references/BEHAVIOR-RULES.md)交付 structured 结果。

## 核心边界

- `risk.analyze` 与 `report.create` 只接受当前用户、当前产品的真实来源任务 ID，不接受用户
  自写证据、自由文本结论或虚构引用。
- 保留每项 `source`、`observed_at`、accession、申报日期、期间与单位，不把缺失数据写成事实。
- 所有分析固定包含“仅供信息参考，不构成投资建议”；拒绝买入、卖出、持有、目标价、保本或
  保证收益等指令。
- 不承诺数据完整、实时、固定价格、上游成功或任何投资回报。

## 参考资料

- [API Key 配置](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/investment-research/references/API-KEY.md)
- [Operations 契约](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/investment-research/references/OPERATIONS.md)
- [HTTP 请求与任务轮询](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/investment-research/references/HTTP-REQUESTS.md)
- [来源、证据与投资安全规则](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/investment-research/references/BEHAVIOR-RULES.md)
