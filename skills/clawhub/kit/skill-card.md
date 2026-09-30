## Description:

Helps agents manage Kit email-marketing subscribers, forms, tags, sequences, broadcasts, purchase records, and webhooks through an authorized account connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and their agents use this skill to inspect and manage Kit subscriber lists, campaigns, and related account data, with optional webhooks and automations when explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Subscriber emails and purchase records may be exposed or changed.

Mitigation: Use OAuth where possible, request only necessary data, and obtain user approval before specific writes.

Risk: Webhooks and automations can continue sending account data after setup.

Mitigation: Confirm the exact destination and intended data before creation; avoid broad or third-party forwarding unless needed, and remove unneeded automations or webhooks.

## Reference(s):

- [Kit skill release](https://clawhub.ai/byungkyu/skills/kit)
- [Maton homepage](https://maton.ai)
- [Kit API overview](https://developers.kit.com/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Text or Markdown with commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Kit account data; avoid exposing unnecessary subscriber or purchase details.]

## Skill Version(s):

1.2.5 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
