## Description:

Generates a weekly operations brief for a single subscribed Amazon ASIN after quote review and explicit user confirmation, using ARI product detail, snapshot, and review evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to request a quoted, confirmed weekly Amazon ASIN operations brief for a subscribed product. It helps summarize product details, snapshots, review evidence, findings, and evidence gaps without claiming unsupported real-time store metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key, stores it locally, contacts ari.funewa.com, and can spend ARI credits after explicit confirmation.

Mitigation: Configure the key only in a trusted environment, review the quoted cost and requestId, and run paid analysis only after explicit user confirmation.

Risk: The security summary states that the bundled CLI can expose broader operation modes than the single-ASIN weekly brief promised by the skill.

Mitigation: Use only the documented weekly ASIN commands and decline requests for broader workflow, focus, competitor, or unrelated operation modes.

Risk: The brief is based on available product, snapshot, and review evidence, not real-time price, sales, inventory, advertising, order, profit, or return-rate data.

Mitigation: Call out missing evidence explicitly and avoid converting unsupported data gaps into operational conclusions.

## Reference(s):

- [Amazon ASIN Weekly Operations Workflow](artifact/references/operation-workflow.md)
- [Amazon ASIN Weekly API Reference](artifact/references/reference.md)
- [ClawHub weekly-asin Skill Page](https://clawhub.ai/funewa/skills/weekly-asin)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown brief with concise findings, evidence notes, and optional inline shell commands for setup, quote, run, and status workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid ARI credit usage.]

## Skill Version(s):

1.4.11 (source: server release evidence, artifact _meta.json, script VERSION, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
