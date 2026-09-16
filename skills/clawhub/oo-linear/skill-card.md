## Description:

Operate Linear through an OOMOL-connected account using the oo CLI to read, create, update, and delete Linear data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to manage Linear workspaces from an agent, including issues, projects, comments, labels, cycles, users, attachments, and workflow states. It supports both read workflows and state-changing Linear operations when the user confirms the exact payload and effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify Linear data available to the connected account, including broad write and delete actions.

Mitigation: Review the live action schema and confirm the exact action, target, payload, and expected effect before running any write or destructive command.

Risk: The skill exposes raw Linear GraphQL query and mutation actions, including mutations that can change workspace data.

Mitigation: Prefer the named connector actions when available, and require explicit user approval for any raw mutation payload.

Risk: First-time setup includes remote pipe-to-shell installer commands for the oo CLI.

Mitigation: Use a signed, pinned, or manually inspected installation path before running installer commands.

## Reference(s):

- [ClawHub Linear Skill](https://clawhub.ai/oomol/skills/oo-linear)
- [Linear](https://linear.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command results are returned as JSON when run with --json.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
