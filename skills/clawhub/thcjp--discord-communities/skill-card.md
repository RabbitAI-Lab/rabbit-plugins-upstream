## Description:

Discord社区管理 helps agents manage Discord OAuth connection checks, user and guild lookups, application command permissions, commercial entitlements, and role-connection workflows through ClawLink.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Community operators and developers use this skill to inspect Discord account, guild, role, command-permission, entitlement, and role-connection state, and to guide scoped Discord changes that require explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says the skill's instructions and requested authority are too inconsistent and broad for automatic approval.

Mitigation: Review before installation and limit the agent to narrowly scoped Discord account, guild, permission, entitlement, and role-connection tasks.

Risk: The artifact asks for read, exec, and write authority even though the core workflow is Discord management guidance.

Mitigation: Do not grant broad file or command-execution authority unless the deployment explicitly requires it.

Risk: Discord mutation actions can leave guilds, edit command permissions, consume or delete entitlements, or change role-connection metadata.

Mitigation: Require explicit confirmation for confirm operations and second confirmation with impact explanation for high-impact operations.

Risk: Discord OAuth scopes or token type may be insufficient or overbroad for the requested operation.

Mitigation: Check the connected Discord integration, token type, and OAuth scopes before making calls, and use least-privilege authorization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/discord-communities)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline code examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Discord read or mutation actions; mutation guidance should preserve explicit confirmation steps for confirm and high-impact operations.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
