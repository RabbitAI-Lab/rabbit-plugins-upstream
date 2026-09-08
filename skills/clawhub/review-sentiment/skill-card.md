## Description:

Analyzes Amazon review sentiment by product dimension, grouping positive and negative themes so sellers can understand buyer pain points, purchase drivers, trends, and improvement opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and operators use this skill to analyze Amazon ASIN reviews, compare positive and negative themes, inspect trends, and turn review evidence into product, listing, and customer-response decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits through review collection and analysis flows, including account-level auto-confirm behavior.

Mitigation: Set auto-confirm off or explicitly say only quote, do not execute when cost approval is required.

Risk: Recurring schedule, watch, or competitor settings can change ongoing account behavior and future collection costs.

Mitigation: Review recurring settings before enabling them and require explicit user approval for schedule or watch changes.

Risk: The integration processes Amazon review and account data through ARI services.

Mitigation: Install only when the user trusts ARI for that data and avoid sharing API keys in chat, reports, or examples.

Risk: Exports can write report or review files to local paths.

Mitigation: Check export destinations before running export commands to avoid overwriting local files.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/review-sentiment)
- [Usage guide](artifact/使用说明.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [Account and authorization](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [Billing](https://ari.funewa.com/zh/billing)
- [Online reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and concise text summaries, with shell commands or configuration steps when setup or troubleshooting is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, sample ranges, credit usage, exported file paths, and data-limit notes when returned by ARI.]

## Skill Version(s):

1.4.8 (source: frontmatter, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
