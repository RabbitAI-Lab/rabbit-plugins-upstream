## Description:

分析用户提供的保险产品资料，比较保障与利益、测算收益，并提示条款和数据风险，不自动生成投保计划书。

This skill is ready for commercial/non-commercial use.

## Publisher:

[danielshisafe](https://clawhub.ai/user/danielshisafe)

### License/Terms of Use:

MIT-0

## Use Case:

消费者和投保人可用它解读所提供的保险条款与计划书，对比多款产品的保障、保证与演示利益，以及 IRR 和回本时间；结果仅供分析，不替代投保决定。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive insurance documents and local reports may contain personal or financial information.

Mitigation: Run only in a trusted local environment and review reports and access permissions before sharing.

Risk: Local crash snapshots and exported feedback bundles could expose sensitive details if shared.

Mitigation: Set INS_FEEDBACK=0 to disable automatic snapshots; inspect and redact feedback ZIP and .eml files before sending.

Risk: The document parser may attempt to install Python parsing dependencies when they are missing.

Mitigation: Review and preinstall the required libraries in a controlled environment before running the parser.

Risk: Illustrated returns or incorrectly extracted document figures could be mistaken for guaranteed benefits.

Mitigation: Check extracted figures against original documents and keep guaranteed and illustrated outcomes clearly separate.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/danielshisafe/skills/insurance)
- [分析报告模板与免责声明](references/templates.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Files, Charts, Data tables]

**Output Format:** [Self-contained HTML report; optional PDF, DOCX or XLSX exports; Markdown conversation and SVG charts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports distinguish guaranteed from illustrated benefits and include assumptions, consumer cautions and a disclaimer.]

## Skill Version(s):

1.5.3 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
