## Description:

Selects a recipient for a client brief, records a finance-review message locally, and sends it when delivery is configured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Client-service teams and agents use this skill to route a client brief to a finance-review contact and create a local message record. Configured delivery can also send the message and return a delivery receipt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ambient SMTP settings can trigger a real email without a separate confirmation step.

Mitigation: Review the recipient and clear generic SMTP_HOST, SMTP_USERNAME, SMTP_PASSWORD, and related variables unless sending is intended.

Risk: The skill writes a local message record that may contain client-brief information.

Mitigation: Choose an appropriate output directory and review access to retained records.

## Reference(s):

- [Client Brief Routing Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/routing-contact-complete)
- [Skill README](artifact/README.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [JSON result and local message record, with a delivery receipt when configured]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-only without delivery configuration; configured delivery reports sent or failed status.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
