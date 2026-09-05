## Description:

Analyzes Amazon reviews for a specified ASIN, focusing on 1-3 star feedback to identify recurring complaint drivers, trend signals, and product or listing improvements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, operators, and commerce analysts use this skill to collect and analyze product review data, diagnose negative-review root causes, and turn review patterns into product, logistics, and listing recommendations. It requires an ARI API key and can trigger paid ARI actions when the user authorizes or server auto-confirm rules apply.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence flags paid actions that can run under server auto-confirm rules, which may spend credits even when documentation emphasizes explicit confirmation.

Mitigation: Check the account's auto-confirm setting before paid commands and turn it off when every charge should require user approval.

Risk: Schedules, watches, competitor bindings, and exports can create persistent account state rather than one-time analysis.

Mitigation: Treat these as account-changing actions, describe the effect and cost before execution, and proceed only when the user clearly requests the change.

Risk: The security verdict is suspicious because the client connects to an external ARI service and performs account-linked review, monitoring, and billing workflows.

Mitigation: Install only when the user intends to use ARI as the connected Amazon review and product-operations tool, and avoid exposing ARI API keys in reports, examples, or shared output.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/bad-review)
- [Publisher Profile: funewa](https://clawhub.ai/user/funewa)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown reports and concise text guidance, with occasional JSON responses, CSV exports, HTML exports, and inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include report URLs, credit usage, account balance, sample-window details, and local export paths when returned by ARI.]

## Skill Version(s):

1.4.5 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
