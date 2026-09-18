## Description:

Amazon-VOC helps agents use ARI to collect Amazon reviews and produce buyer-voice reports covering pain points, purchase drivers, user segments, usage scenarios, trends, competitor comparisons, listing optimization, alerts, monitoring, and exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and agents use this skill to analyze Amazon review data through ARI, summarize buyer feedback, identify product and listing issues, compare competitors, and prepare exportable VOC reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some ARI review-analysis flows may spend ARI credits when account auto-confirmation rules allow it.

Mitigation: Set the ARI account to ask before every paid action when strict spend control is required, and use quote-only requests before running paid analysis or collection.

Risk: The skill can manage schedules, competitors, watches, autoconfirm limits, exports, and workbench status changes that may persist beyond the current chat.

Mitigation: Review requests that enable or change persistent settings, confirm the intended ASIN/site/schedule before applying them, and disable or revert settings when no longer needed.

Risk: The skill requires an ARI API key to access ARI account data and workflows.

Mitigation: Use the documented browser authorization or local configuration flow, avoid pasting keys into chat or reports, and keep requests on the fixed HTTPS ARI endpoint.

## Reference(s):

- [Amazon-VOC README](README.md)
- [Amazon-VOC User Guide](使用说明.md)
- [ARI CLI and API Reference](references/reference.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/amazon-voc)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown reports, concise text summaries, shell commands, and CSV/HTML/Markdown export files or links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and may rely on account-specific credit, confirmation, export, and monitoring settings.]

## Skill Version(s):

1.4.13 (source: frontmatter, _meta.json, CHANGELOG, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
