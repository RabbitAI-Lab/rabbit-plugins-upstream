## Description:

Helps agents query and manage Monday.com boards, items, and workflows through an authenticated Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and developers use this skill to read Monday.com account context and manage boards, items, columns, groups, and workspaces. With explicit approval, they can also create connections, make changes, and configure scheduled or event-driven workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unintended changes or deletions to Monday.com business data.

Mitigation: Default to reads; verify the account and target, and obtain explicit approval for each write or deletion.

Risk: Webhooks and trigger destinations may forward data continuously to untrusted recipients.

Mitigation: Review each automation and its destination separately; use trusted destinations and require explicit approval before forwarding to a third-party URL.

Risk: Exposed API keys or overly broad account permissions may grant unintended access.

Mitigation: Prefer OAuth login, keep credentials out of logs and destinations, and limit connections to the access needed.

## Reference(s):

- [ClawHub Monday.com skill release](https://clawhub.ai/byungkyu/skills/monday)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Monday.com API basics](https://developer.monday.com/api-reference/docs/basics)
- [Monday.com GraphQL overview](https://developer.monday.com/api-reference/docs/introduction-to-graphql)
- [Schedule trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command, GraphQL, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and an authorized Maton connection; confirm changes before execution.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
