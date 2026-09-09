## Description:

ARI helps agents collect and analyze Amazon reviews through the ARI API, producing consumer insights, VOC reports, trends, competitor comparisons, and listing improvement suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to analyze review samples for pain points, purchase drivers, trends, competitor differences, alerts, and listing or product improvement opportunities. It can also guide setup, authorization, quoting, monitoring, export, and report retrieval workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI collection, analysis, and some report workflows can consume account credits, and server-side auto-confirm rules may allow small operations to execute without a fresh chat confirmation.

Mitigation: Use quote-only mode or disable auto-confirm before analysis when cost control matters, and confirm returned cost, balance, and scope before running paid operations.

Risk: The skill uses an ARI API key and sends ASIN and review-analysis data to ARI services.

Mitigation: Install only if the publisher is trusted with the data, store the API key locally or in ARI_API_KEY, avoid pasting keys into chat or reports, and revoke or rotate keys from the ARI account page when needed.

Risk: Ongoing monitoring or schedule changes can create recurring collection activity and future credit use.

Mitigation: Require explicit user agreement on monitoring frequency, monthly cost notes, and scope before enabling weekly or daily monitoring.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/sellerari)
- [Publisher profile](https://clawhub.ai/user/funewa)
- [README](artifact/README.md)
- [User guide](artifact/使用说明.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI account and API key management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI product management](https://ari.funewa.com/zh/products)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text with optional shell commands, JSON summaries, report links, and exported CSV, Markdown, or HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and bases analysis on ARI-collected Amazon review samples; paid collection, analysis, and monitoring may consume account credits.]

## Skill Version(s):

1.4.8 (source: server release evidence, _meta.json, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
