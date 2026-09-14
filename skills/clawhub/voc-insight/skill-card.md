## Description:

VOC洞察 analyzes Amazon review data through ARI to summarize customer voice, pain points, purchase motivations, sentiment, trends, competitive context, and Listing or product-improvement recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators and ecommerce teams use this skill to turn Amazon reviews for an ASIN into concise VOC summaries, trend checks, competitor comparisons, alerts, and actionable Listing or product recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI analysis or monitoring can consume credits automatically under account rules.

Mitigation: Before running paid analysis, ask the skill to quote only or require confirmation before every deduction, and review monitoring or auto-confirm settings that could create future charges.

Risk: The skill requires an ARI API key, which could expose account access if stored on an unprotected shared machine.

Mitigation: Use browser authorization or environment-based configuration on a trusted machine, avoid pasting keys into chat, and protect or revoke the local key if the machine is shared.

Risk: Review coverage and trend conclusions depend on ARI's collected sample and may not cover all Amazon reviews or variants.

Mitigation: Read the reported sample scope and trend caveats, and validate high-impact product or Listing decisions against additional data when samples or time windows are limited.

Risk: Interrupted paid runs may already have generated a report and consumed credits.

Mitigation: Check existing reports or task status before retrying a paid command to avoid duplicate generation and charges.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/voc-insight)
- [README](artifact/README.md)
- [使用说明](artifact/使用说明.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI account and API key management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and text summaries with optional JSON, CSV, Markdown, or HTML exports from ARI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include sample scope, review evidence, trend caveats, credit usage, report links, and local export paths when the user requests exports.]

## Skill Version(s):

1.4.11 (source: frontmatter, _meta.json, evidence.release.version, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
