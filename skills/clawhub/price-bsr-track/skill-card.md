## Description:

从已保存的 Amazon 商品快照中摘要展示价格与主要 BSR 字段的确定性变化，并标注采样时间；需要 ARI API key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External ClawHub users and developers use this skill to have an agent summarize saved Amazon product snapshots, create or manage daily/weekly price and BSR watches, and return deterministic watch digest summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release presents a focused price/BSR watch skill, but the packaged authenticated ARI CLI exposes broader paid analysis, export, account-management, and state-changing workflows.

Mitigation: Limit agent execution to the documented watch commands for price/BSR summaries, and require explicit human review before any non-watch command is run.

Risk: Autoconfirm settings or non-watch commands could allow paid or state-changing ARI actions outside the normal watch digest workflow.

Mitigation: Disable or verify autoconfirm settings before use, explain daily/weekly quotas and scan costs before watch changes, and require clear user confirmation for management actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/price-bsr-track)
- [Amazon Price/BSR Watch Reference](artifact/references/reference.md)
- [Amazon Price/BSR Watch Workflow](artifact/references/watch-workflow.md)
- [ARI Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON watch digest results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and saved Amazon product snapshots; documented watch digest output uses 0 credits.]

## Skill Version(s):

1.4.8 (source: server release, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
