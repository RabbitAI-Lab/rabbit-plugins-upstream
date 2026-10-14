## Description:

Guides developers in choosing, creating, and managing Neon database branches for testing and development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to select normal or schema-only Neon branches, test migrations, manage branch lifecycles, and reset child branches when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Resetting a child branch replaces its data and discards changes made on that branch.

Mitigation: Review the target and confirm the reset before execution; preserve the previous state as a backup branch when needed.

Risk: Updating DATABASE_URL in a local environment file can redirect the app or tests to a different database.

Mitigation: Ask for explicit confirmation before changing an existing environment key, and verify the new branch connection string.

## Reference(s):

- [Neon branching documentation](https://neon.com/docs/introduction/branching.md)
- [Schema-only branching](https://neon.com/docs/guides/branching-schema-only.md)
- [Reset from parent](https://neon.com/docs/guides/reset-from-parent.md)
- [Neon CLI quickstart](https://neon.com/docs/cli/quickstart.md)
- [Neon MCP server](https://neon.com/docs/ai/neon-mcp-server.md)
- [ClawHub skill listing](https://clawhub.ai/andrelandgraf/skills/neon-postgres-branches)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with shell commands and optional TypeScript configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide a branch connection string or an actionable next step.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
