## Description:

Guides agents through authenticated Pipedrive CRM reads and user-approved updates to deals, people, organizations, activities, and pipelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams and their assistants use this skill to find Pipedrive CRM records and, with explicit approval, update records or arrange scheduled CRM actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A write or deletion could change the wrong CRM record or account.

Mitigation: Confirm the exact connection, record, payload, and intended effect with the user before making changes.

Risk: Functions, triggers, or destinations can continue acting on or forwarding data after setup.

Mitigation: Review scope and destination, obtain separate explicit approval for persistent automation, and remove it when no longer needed.

Risk: Raw API keys or broad account access could expose sensitive CRM data.

Mitigation: Prefer CLI-managed OAuth, limit connection scopes, and use raw API keys only when the CLI cannot be used.

## Reference(s):

- [Pipedrive skill release](https://clawhub.ai/byungkyu/skills/pipedrive-api)
- [Maton](https://maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Pipedrive API Overview](https://developers.pipedrive.com/docs/api/v1)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with inline commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authorized Pipedrive connection; changes require user approval.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
