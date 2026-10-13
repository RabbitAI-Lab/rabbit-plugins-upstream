## Description:

分析政府采购项目的投标可行性、竞争格局、历史成交价格与合规风险，并给出报价和参与建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and bid teams evaluate a specific government tender, compare historical awards and likely competitors, and prepare a go/no-go decision with a suggested price range.

### Deployment Geography for Use:

Global (focused on Chinese government procurement)

## Known Risks and Mitigations:

Risk: API queries consume account credits.

Mitigation: Confirm the estimated credit use before analysis and obtain approval before exceeding the planned budget.

Risk: Optional account registration uses device-derived features and stores an API key locally.

Mitigation: Request consent before registration; use a user-provided ZLBX_API_KEY to avoid auto-registration and protect the stored key.

Risk: Shared reports may contain signed links that grant account access.

Mitigation: Remove signed sk links before sharing reports publicly.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/government-procurement-bid-decision)
- [Skill installation documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [API quick reference](references/api-quick.md)
- [Bid analysis workflow](references/workflow.md)
- [Report template](references/report-template.md)
- [Account registration guide](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, Files]

**Output Format:** [Markdown decision report and optional HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a go/no-go recommendation, pricing benchmarks, competitor outlook, supporting sources, and risk notes.]

## Skill Version(s):

1.0.8 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
