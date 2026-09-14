## Description:

Collects and analyzes Amazon reviews through ARI to produce consumer insight summaries, VOC reports, trend analysis, competitor comparisons, listing suggestions, and exportable review or report files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and operators use this skill to analyze Amazon ASIN review data, understand pain points and buying motivations, compare competitors, monitor review changes, and turn review evidence into product, listing, keyword, and support actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI collection or analysis actions may spend account credits, including flows where server account rules allow small charges with limited per-action confirmation.

Mitigation: Use quote-only requests when evaluating cost, ask the agent to require confirmation before every charge when desired, and review balances before confirming paid operations.

Risk: Changing spending-confirmation settings can allow future ARI credits to be spent without a separate prompt for each action.

Mitigation: Avoid enabling auto-confirm thresholds unless intentional, and reset confirmation behavior to per-action prompts when stricter control is needed.

Risk: Exports can write review or report data to local files.

Mitigation: Export only to trusted local directories and avoid sharing generated CSV, Markdown, or HTML reports outside the intended account workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/sellerari)
- [ARI CLI and API Reference](references/reference.md)
- [ARI Usage Guide](使用说明.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing and Plans](https://ari.funewa.com/zh/billing)
- [ARI Report Center](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown and text responses with shell commands; CLI responses may include JSON, CSV exports, Markdown reports, HTML reports, and report URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and uses ARI credits for paid collection or analysis flows.]

## Skill Version(s):

1.4.11 (source: server release metadata, frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
