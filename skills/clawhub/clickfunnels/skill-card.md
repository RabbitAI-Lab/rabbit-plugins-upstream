## Description:

Helps agents manage ClickFunnels contacts, products, orders, courses, forms, and webhooks through an authorized account connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing and operations teams use this skill to manage ClickFunnels business records and set up account-connected workflows, with approval for changes and automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account actions can change contacts, orders, and other business records.

Mitigation: Start with read-only requests and obtain explicit approval for each write or new connection.

Risk: Functions, triggers, and webhooks can run unattended or forward customer data persistently.

Mitigation: Confirm each automation and its exact destination separately; use only destinations the user trusts.

Risk: Long-lived API keys or credentials in forwarded requests can be exposed.

Mitigation: Prefer the CLI OAuth flow, avoid raw API keys where possible, and never place provider credentials in destination requests.

## Reference(s):

- [ClickFunnels skill listing](https://clawhub.ai/byungkyu/skills/clickfunnels)
- [ClickFunnels API reference](https://developers.myclickfunnels.com/reference)
- [ClickFunnels webhooks overview](https://developers.myclickfunnels.com/docs/webhooks)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code examples; structured API results when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may contain customer data; share only fields needed for the task.]

## Skill Version(s):

1.2.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
