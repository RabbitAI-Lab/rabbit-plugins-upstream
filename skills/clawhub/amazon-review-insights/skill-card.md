## Description:

Amazon Review Insights helps global e-commerce sellers collect Amazon reviews, analyze negative feedback, find issues in high-rated reviews, generate improvement suggestions, and track review trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sparkbayes](https://clawhub.ai/user/sparkbayes)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers and their agents use this skill to create or query AstrMap review-analysis tasks, inspect sentiment, tags, trends, representative reviews, and manage incremental updates for Amazon products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends an AstrMap API key to api.astrmap.com for authentication.

Mitigation: Use CUSTOMER_INSIGHTS_API_KEY rather than hardcoding credentials, do not share the key, and rotate or disable it when no longer needed.

Risk: Review collection may require installing the AstrMap desktop client and logging it into an Amazon buyer account.

Mitigation: Use a dedicated buyer account, avoid seller or primary accounts, and verify desktop downloads, checksums, and code signatures before installation.

Risk: Task creation, incremental fetch, or AI analysis can deduct AstrMap points.

Mitigation: Check available points and obtain explicit user confirmation before point-deducting actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sparkbayes/skills/amazon-review-insights)
- [AstrMap API Reference](references/api_reference.md)
- [AstrMap Desktop Client Security Guide](references/security.md)
- [AstrMap website](https://www.astrmap.com/)
- [AstrMap download configuration](https://www.astrmap.com/download-config.json)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CUSTOMER_INSIGHTS_API_KEY; some collection and analysis actions require user confirmation before point-deducting operations.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
