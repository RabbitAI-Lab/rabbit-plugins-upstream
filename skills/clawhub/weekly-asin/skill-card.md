## Description:

Generates an operations weekly report for a single subscribed Amazon ASIN after quote review and explicit user confirmation, using product details, snapshots, and review evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, ecommerce operators, and supporting developers use this skill to request a weekly operations brief for one subscribed ASIN after checking data readiness and quoted cost.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI actions can consume credits after a quote is accepted.

Mitigation: Review the quote and require explicit user confirmation before running collect or operations run commands.

Risk: The security summary flags broader workflow options than the single-ASIN weekly-report description promises.

Mitigation: Use the documented weekly/asin flow and avoid workflow, focus, or competitor overrides unless the publisher explicitly documents and scopes them for this skill.

Risk: The skill requires an ari_live API key and sends Amazon ASIN and report data to ARI.

Mitigation: Install only if you trust funewa and ARI with that data, and store the key through setup, configure, or ARI_API_KEY rather than placing it in the skill artifact.

## Reference(s):

- [Amazon ASIN Weekly Brief API Reference](artifact/references/reference.md)
- [Amazon ASIN Weekly Brief Operations Workflow](artifact/references/operation-workflow.md)
- [ClawHub Skill Listing](https://clawhub.ai/funewa/skills/weekly-asin)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown or plain-text weekly brief, with JSON responses from ARI CLI commands when technical output is shown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection or analysis should run only after a quote and explicit user confirmation.]

## Skill Version(s):

1.4.13 (source: artifact/_meta.json, artifact/scripts/ari.py, artifact/CHANGELOG.md, server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
