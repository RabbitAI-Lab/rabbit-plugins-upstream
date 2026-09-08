## Description:

Tally API integration with managed OAuth for managing forms, submissions, workspaces, webhooks, organization users, and organization invites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Tally forms, submissions, workspaces, webhooks, and organization membership through Maton-mediated OAuth access. It is intended for normal account administration workflows where read/list calls are preferred and write operations require explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify Tally forms, workspaces, webhooks, organization users, and organization invites after user approval.

Mitigation: Confirm the selected Tally connection, target resource, payload, and intended effect before approving any write operation.

Risk: Webhook subscriptions can continuously send form submission data to an external URL.

Mitigation: Confirm the webhook destination URL, who controls that host, and the associated form before creating or updating a webhook.

Risk: Organization user removal and invite management can change account access.

Mitigation: Confirm the target user or email address and the intended membership change before approving organization operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/tally-api)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Tally API Introduction](https://developers.tally.so/api-reference/introduction)
- [Tally API Reference](https://developers.tally.so/llms.txt)
- [Tally Help Center](https://help.tally.so/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration]

**Output Format:** [Markdown with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a valid Maton account, and user approval for write operations or new Tally connections.]

## Skill Version(s):

1.2.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
