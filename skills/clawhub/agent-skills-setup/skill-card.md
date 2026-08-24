## Description:

Use when a user names two supported IDEs or agent products to plan, migrate, or inspect specific skills, instructions, and MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inventory local agent or IDE configuration, plan migrations between supported products, and apply reviewed changes for portable skills, instructions, and MCP entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill inspects local IDE and agent configuration that may contain sensitive paths, MCP entries, or local setup details.

Mitigation: Install and run it only when local configuration inspection is intended, and review generated plans, diffs, bundles, and manifests before approving writes.

Risk: Applying untrusted plans or bundles could change local agent or IDE configuration in unintended ways.

Mitigation: Use only trusted plans and bundles, verify bundles before restore, and apply the exact reviewed plan with explicit approval.

Risk: The all-installed mode performs a broader local scan across installed products.

Mitigation: Avoid all-installed unless a broad local inventory or migration is desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/luckycat133/skills/agent-skills-setup)
- [IDE Reference Index](references/ide-registry.md)
- [Registry v2](references/registry-v2.json)
- [Migration Safety](references/migration-safety.md)
- [MCP Migration](references/mcp-migration.md)
- [Object Migration](references/object-migration.md)
- [Verification](references/verification.md)
- [Agent Skills specification](https://raw.githubusercontent.com/agentskills/agentskills/main/docs/specification.mdx)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [VS Code agent skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)
- [Gemini CLI skills](https://github.com/google-gemini/gemini-cli/blob/main/docs/skills.md)
- [Cursor rules](https://docs.cursor.com/context/rules)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON files]

**Output Format:** [Markdown guidance with shell commands plus generated plans, manifests, and bundles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline execution only; apply and restore actions are gated by reviewed plans and explicit approval.]

## Skill Version(s):

0.8.29 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
