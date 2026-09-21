## Description:

Virsical 威思客智慧空间管理平台集成技能，适用于查询或预订会议、创建工单报修、查询访客记录，并支持中英双语交互。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wafer](https://clawhub.ai/user/wafer)

### License/Terms of Use:

MIT-0

## Use Case:

Employees who use Virsical can query and book meeting rooms, review their meetings, look up visitor records, and create facility work orders from an agent conversation. The skill is intended for account-authenticated workspace operations where Virsical licenses determine which workflows are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Virsical Agent authorization codes and account tokens that can grant account-level access.

Mitigation: Use only in environments that treat chat input as sensitive, avoid sharing authorization codes, and log out or rotate credentials if a code or token may have been exposed.

Risk: The release evidence notes a recoverable OAuth client credential.

Mitigation: Ask the publisher to rotate or remove the embedded credential and move to PKCE or a backend token exchange.

Risk: The skill can create bookings and facility work orders through the user's Virsical account.

Mitigation: Require clear user confirmation before creating bookings or work orders, especially when project, room, time, priority, or type values are inferred.

## Reference(s):

- [Command Reference](references/commands.md)
- [API Reference](references/api_reference.md)
- [Authentication Flow](references/auth_flow.md)
- [Error Codes](references/error_codes.md)
- [Virsical Agent Authorization Guide](https://www.virsical.com/guide.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown tables, concise status text, and executable Python shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adapts response language to the user and summarizes API results instead of showing full raw JSON.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
