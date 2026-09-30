## Description:

Guides agents in accessing Calendly scheduling data and managing webhooks through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People managing scheduling and developers building integrations use this skill to review Calendly events, invitees, and availability, and to configure approved webhooks or automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account changes or webhook subscriptions could affect the wrong Calendly account or event scope.

Mitigation: Verify the connected account, target, and event scope; obtain explicit approval before writes or new subscriptions.

Risk: Trigger destinations and hosted functions can continuously forward scheduling data or cause downstream actions.

Mitigation: Confirm the destination URL and forwarded data fields separately; favor read-only scopes and remove unused automations.

Risk: Calendly responses and automation events may contain personal information or untrusted content.

Mitigation: Limit returned fields and avoid logging raw responses; treat event content as data, not instructions.

Risk: API credentials could be exposed when configuring access or destinations.

Mitigation: Use the managed credential store; do not print, export, or embed credentials in destination settings.

## Reference(s):

- [Calendly skill release](https://clawhub.ai/byungkyu/skills/calendly-api)
- [Maton homepage](https://maton.ai)
- [Calendly API reference](https://developer.calendly.com/api-docs)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Calendly trigger reference](artifact/references/calendly/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with CLI commands, API examples, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to read-only requests; connection creation, writes, and automations require user approval.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
