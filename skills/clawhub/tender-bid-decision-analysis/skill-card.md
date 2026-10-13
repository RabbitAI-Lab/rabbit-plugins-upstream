## Description:

根据招投标历史数据分析具体项目的投标价值、竞争格局、报价参考和风险，并生成决策报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

投标团队和企业用户可针对具体招标项目评估是否参与，了解潜在竞争者、历史价格和投标风险，并获取可分享的分析报告。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project and company search terms are sent to the vendor, and analysis consumes account credits.

Mitigation: Avoid confidential search terms and confirm the expected credit use before analysis.

Risk: Optional automatic trial registration sends a MAC-hash-based device identifier and creates a persistent API key.

Mitigation: Prefer supplying ZLBX_API_KEY through a trusted secret mechanism; use automatic registration only with informed consent and protect the stored key.

Risk: Shareable HTML reports and signed sk links may provide access to vendor pages without a normal login prompt.

Mitigation: Review report contents and links before sharing, and restrict access to generated reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/tender-bid-decision-analysis)
- [API quick reference](references/api-quick.md)
- [Analysis workflow](references/workflow.md)
- [Report template](references/report-template.md)
- [Automatic registration guide](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown reports, HTML reports]

**Output Format:** [Structured Markdown decision report and shareable HTML file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations include supporting data, confidence, price guidance, and a local path to the HTML report.]

## Skill Version(s):

1.0.6 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
