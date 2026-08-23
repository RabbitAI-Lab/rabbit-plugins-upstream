## Description:

中标概率与投标胜率评估助手。当用户给出一个具体的招标项目并希望评估中标可能性时，必须使用此SKILL：中标概率评估、投标胜率分析、该不该投/值不值得投、采购方偏好供应商分析（在位者/关系户信号识别）、竞争对手预测与实力对比、自家公司业绩匹配度分析、报价参考、废标风险评估。基于全网招中标历史数据输出带胜率结论的决策报告。即使用户没有提到「中标概率」，只要涉及投标能不能中、胜算多大、对手是谁、该不该参与等需求，都应使用本SKILL。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External teams and procurement-facing users use this skill to evaluate whether to bid on a specific tender, estimate likely competitors, assess buyer and incumbent signals, and produce a decision report with pricing and risk guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts Zhiliaobiaoxun services and consumes paid or trial API quota during analysis.

Mitigation: Tell users the expected quota cost before analysis and pause before exceeding the documented call budget.

Risk: The skill may store an API key in ~/.zlbx/config.json when opt-in auto-registration succeeds.

Mitigation: Use a preconfigured ZLBX_API_KEY when possible, avoid exposing credentials in conversation, and review local credential storage before installation.

Risk: Opt-in auto-registration collects platform, CPU architecture, and a SHA-256 hash of a MAC address for free-trial device de-duplication.

Mitigation: Require explicit user consent before registration and allow users to skip the flow by configuring an API key manually.

Risk: Generated reports may contain project details and signed access links returned by the API.

Mitigation: Share generated reports only with intended recipients and preserve signed links exactly as returned so users understand what access they expose.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/bid-win-rate-analyzer)
- [Publisher Profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [API Quick Reference](references/api-quick.md)
- [Analysis Workflow](references/workflow.md)
- [Report Template](references/report-template.md)
- [Auto Registration Flow](references/auto-register.md)
- [Zhiliaobiaoxun API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool})
- [Zhiliaobiaoxun Account Portal](https://ai.zhiliaobiaoxun.com/?ch=s73)

## Skill Output:

**Output Type(s):** [text, markdown, files, configuration, guidance]

**Output Format:** [Markdown decision report in conversation, with optional self-contained HTML report file generated from structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Complete reports typically use 12-25 API calls; quick checks use 5-8 API calls. Generated HTML reports may include signed source links returned by the API.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
