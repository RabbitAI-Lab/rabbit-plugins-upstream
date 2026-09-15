## Description:

Tally API integration with managed OAuth for managing forms, submissions, workspaces, webhooks, organization users, and organization invites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Tally forms, submissions, workspaces, organization membership, webhooks, and approved automations through Maton-managed authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act on real Tally business data.

Mitigation: Use OAuth where possible and confirm each write before changing forms, submissions, workspaces, members, invites, or webhooks.

Risk: Persistent webhooks or automations can continue sending or acting on data after setup.

Mitigation: Confirm every webhook, destination URL, or hosted function before creation and remove connections or automations when they are no longer needed.

Risk: Organization user removal and invite management can affect account membership.

Mitigation: Confirm the target account member, invite, and intended effect before making membership changes.

## Reference(s):

- [Tally Skill on ClawHub](https://clawhub.ai/byungkyu/skills/tally-api)
- [Maton Homepage](https://maton.ai)
- [Tally API Introduction](https://developers.tally.so/api-reference/introduction)
- [Tally API Reference](https://developers.tally.so/llms.txt)
- [Tally Help Center](https://help.tally.so/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Code, Configuration]

**Output Format:** [Markdown with bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and authorization for the connected Tally account.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
