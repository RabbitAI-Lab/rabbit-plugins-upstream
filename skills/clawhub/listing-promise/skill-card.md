## Description:

核对 Amazon Listing 中的功能、效果和使用承诺与评论反馈是否一致，并标出证据缺口。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and operators use this skill to compare product-page promises against ARI-collected review evidence, identify gaps, and produce concise operational findings before changing copy or planning product improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires ARI account access and exposes broader ARI operations than the narrow listing-promise use case.

Mitigation: Install only for accounts where this access is acceptable, run the initial account check, and review schedule, watch, competitor, export, and workbench-status actions before approving them.

Risk: Paid analysis, collection, monitoring, leaderboard, and advice actions can consume credits or affect ongoing account workflows.

Mitigation: Use quote or status commands for review, require explicit confirmation before paid or persistent actions, and set autoconfirm to ask every time when per-charge control is needed.

Risk: Interrupted paid operations may already have charged credits or created a report before the local command returns.

Mitigation: Check the relevant report or operation status using the original request identifier before retrying any confirmed paid action.

Risk: External webpage instructions or unverified prompts could steer the agent outside the intended review workflow.

Mitigation: Avoid pasting external website instructions into the agent unless they have been verified, and keep the workflow fixed to listing/promise for this dedicated skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/listing-promise)
- [Usage guide](使用说明.md)
- [Dedicated listing promise workflow](references/operation-workflow.md)
- [ARI CLI and API reference](references/reference.md)
- [ARI API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI product management](https://ari.funewa.com/zh/products)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and concise text summaries, with shell command guidance when setup or troubleshooting is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include data range, review evidence, trend caveats, ARI report URLs, credit usage, and export file details when relevant.]

## Skill Version(s):

1.4.8 (source: evidence.release.version, artifact/SKILL.md frontmatter, artifact/CHANGELOG.md, artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
