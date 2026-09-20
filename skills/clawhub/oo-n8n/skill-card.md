## Description:

n8n (n8n.io). Use this skill for ANY n8n request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage n8n workflows, executions, data tables, tags, variables, and insights through an OOMOL-connected account. It supports read actions and gated write or destructive actions that require the agent to check the target and payload before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running a remote CLI installer script directly in a shell.

Mitigation: Install the oo CLI yourself from trusted OOMOL documentation before using the skill, or review the installer source before execution.

Risk: Write and destructive n8n actions can change, stop, delete, or overwrite workflows, data tables, variables, tags, and execution metadata.

Mitigation: Confirm the exact action, target, and JSON payload before allowing write or destructive commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-n8n)
- [n8n homepage](https://n8n.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI connector schema and run commands; command results are JSON when invoked with --json.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
