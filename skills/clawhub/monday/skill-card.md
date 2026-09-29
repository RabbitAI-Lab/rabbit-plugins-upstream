## Description:

Helps agents query and manage Monday.com boards, items, and workspaces through a Maton-managed account connection, with optional workflow automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and developers use this skill to inspect and update Monday.com workspaces, boards, and tasks, and to set up approved scheduled or event-driven actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account access and data-changing operations can affect Monday.com boards, items, and users.

Mitigation: Authorize the connection explicitly, use only the access needed, and confirm each write and its target before execution.

Risk: Deployed functions, triggers, and destination URLs can create persistent actions or forward event and business data.

Mitigation: Review each deployment, trigger, and destination separately; send data only to destinations the user controls and trusts.

Risk: A local event handler can run code against untrusted event payloads.

Mitigation: Require a user-authored or reviewed handler and separate approval before using local --exec execution.

## Reference(s):

- [Monday.com skill release](https://clawhub.ai/byungkyu/skills/monday)
- [Maton homepage](https://maton.ai)
- [Monday.com GraphQL API overview](https://developer.monday.com/api-reference/docs/introduction-to-graphql)
- [Maton documentation](https://docs.maton.ai)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Guidance]

**Output Format:** [Markdown with GraphQL, JSON, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include account or business data; limit disclosure to what the task requires.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
