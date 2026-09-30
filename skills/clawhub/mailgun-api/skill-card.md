## Description:

Connects an agent to Mailgun through Maton to send and track email and manage domains, routes, templates, mailing lists, suppressions, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other authorized users use this skill to manage a connected Mailgun account, send transactional email, review delivery activity, and set up user-approved email automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email sends and account changes can affect recipients, account configuration, and stored data.

Mitigation: Start with read-only requests and confirm the exact recipients, target, payload, and effect before every write or deletion.

Risk: Webhooks and triggers can continuously forward data or perform actions after setup.

Mitigation: Get explicit approval for the destination and ongoing behavior; review who controls the destination and remove unneeded automations.

Risk: Exposed Mailgun or Maton credentials can grant account access.

Mitigation: Prefer managed login and least-privilege connections; do not expose, log, or embed credentials in commands or destinations.

## Reference(s):

- [Mailgun skill on ClawHub](https://clawhub.ai/byungkyu/skills/mailgun-api)
- [Maton homepage](https://maton.ai)
- [Mailgun API documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/api-overview)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Related API gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with CLI commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account and an authorized Mailgun connection; the gateway defaults to Mailgun's US region.]

## Skill Version(s):

1.2.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
