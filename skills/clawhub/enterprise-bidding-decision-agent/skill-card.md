## Description:

基于知了标讯的历史招中标数据，为具体招标项目生成含投标建议、竞争预测、报价参考和风险分析的决策报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

企业投标团队和采购商机分析人员可针对具体招标项目评估是否参投、潜在竞争者、历史成交价格及资格和废标风险，并获取有依据的行动建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shareable HTML reports may include signed no-login links to tender and company records.

Mitigation: Treat reports as sensitive and share them only with recipients intended to access the linked records.

Risk: Trial registration uses a hashed MAC-derived device identifier and persists an API key locally.

Mitigation: Request informed consent before registration; review local key storage under ~/.zlbx/config.json or provide an existing API key to skip registration.

Risk: Bid analysis consumes account credits through the Zhiliaobiaoxun API.

Mitigation: Disclose estimated credit use before analysis and ask before exceeding the planned call budget.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/enterprise-bidding-decision-agent)
- [投标决策分析工作流](references/workflow.md)
- [工具速查](references/api-quick.md)
- [投标决策报告模板](references/report-template.md)
- [自动注册与账户说明](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Files]

**Output Format:** [Markdown decision report; optional shareable HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full reports include evidence and confidence levels; HTML reports may contain signed no-login links to cited records.]

## Skill Version(s):

1.0.5 (source: SKILL.md frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
