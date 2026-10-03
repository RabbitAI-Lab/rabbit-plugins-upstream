## Description:

Helps agents access Gumroad products, sales, subscribers, and licenses through Maton, and set up approved webhooks and automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Storefront operators and developers use this skill to inspect Gumroad sales and products, verify licenses, and manage approved account integrations or notifications through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an account or modifying storefront data may grant access or make unintended changes.

Mitigation: Review requested access and confirm each new connection or write, including its target and effect, before approval.

Risk: Webhooks, triggers, and destinations can forward events continuously, including sensitive information from other connected services.

Mitigation: Approve each destination and hosted function separately, verify its source and URL, and limit forwarded fields to those needed.

Risk: Access credentials or private customer data could be exposed through logs or destination payloads.

Mitigation: Keep credentials out of destinations and responses; share only the data needed for the requested task.

## Reference(s):

- [ClawHub Gumroad skill](https://clawhub.ai/byungkyu/skills/gumroad)
- [Maton homepage](https://maton.ai)
- [Gumroad API overview](https://gumroad.com/api)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Supported scheduled trigger events](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command, API, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and an authorized Maton connection; confirm writes and automations before execution.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
