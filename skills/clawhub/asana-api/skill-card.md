## Description:

Helps agents manage Asana tasks, projects, workspaces, users, and webhooks through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using Asana can ask an agent to find and manage work items, track projects, or set up approved workflow automations using their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected Asana account data or credentials may be exposed.

Mitigation: Prefer OAuth, select only needed access, keep API keys private, and limit shared or logged response data.

Risk: Writes or deletes can change or remove the wrong Asana resource.

Mitigation: Confirm the account, exact resource, and intended change before each write; do not use automatic confirmation for deletes.

Risk: Webhooks and trigger destinations can continue forwarding data after setup.

Mitigation: Get separate approval for each destination, review its recipient and forwarded fields, and remove automations when no longer needed.

## Reference(s):

- [Asana API documentation](https://developers.asana.com)
- [Asana API reference](https://developers.asana.com/reference)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)
- [Asana skill release](https://clawhub.ai/byungkyu/skills/asana-api)
- [Scheduled trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration instructions]

**Output Format:** [Markdown with command and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include instructions for approved, persistent automations and webhooks.]

## Skill Version(s):

1.2.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
