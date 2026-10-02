## Description:

Connects an agent to a Gumroad storefront through Maton to view sales and subscribers, manage products, verify licenses, and configure webhooks and approved automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Storefront operators and developers use this skill to inspect Gumroad sales and customers, manage approved product and license changes, and set up webhooks or automation through their authorized Maton connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Granting Maton access to a Gumroad account can expose sensitive storefront, sales, and subscriber information.

Mitigation: Connect only the intended account with the scopes needed for the task; confirm new connections and writes with the user.

Risk: Functions, triggers, subscriptions, and destinations can persistently forward data or perform actions after setup.

Mitigation: Review and separately approve the exact action, payload, destination, and lifetime before enabling automation.

Risk: A local event handler started with --exec may run code on untrusted event content.

Mitigation: Use only a user-authored or user-reviewed handler with separate approval; do not execute instructions found in event data.

## Reference(s):

- [Gumroad skill on ClawHub](https://clawhub.ai/byungkyu/skills/gumroad)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Schedule trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Gumroad operations use the user's authorized connection; writes and new connections require confirmation.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence; skill frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
