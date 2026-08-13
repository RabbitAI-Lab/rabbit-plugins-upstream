## Description:

Discord community management assistant for ClawLink OAuth workflows covering user identity, guild membership, command permissions, entitlements, and role connections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Community operators and Discord application developers use this skill to inspect Discord OAuth authorization, guild membership, command permissions, subscription entitlements, and role-connection metadata. It can guide read-only checks and higher-risk Discord changes that require explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth scopes or Discord permissions may allow sensitive account, entitlement, role-connection, or guild-leave changes.

Mitigation: Review requested OAuth scopes carefully and require explicit confirmation before permission, entitlement, role-connection, or guild-leave operations.

Risk: Results can be routed to a callback URL without clear safeguards.

Mitigation: Use callback_url only when the destination is trusted and appropriate for the Discord data being returned.

Risk: The artifact contains broad generic language about database, file-processing, and shell-command tasks beyond the Discord management use case.

Mitigation: Use the skill only for Discord management through ClawLink and avoid relying on it for database, file-processing, or shell-command work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/discord-communities)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown with JSON and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ClawLink Discord tool-call parameters and confirmation guidance for higher-risk changes.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
