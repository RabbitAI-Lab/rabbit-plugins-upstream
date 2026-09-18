## Description:

Operates n8n workflows, executions, data tables, tags, and variables through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read and manage n8n workflows, executions, data tables, tags, variables, and related metadata from an agent session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer snippets for the oo CLI.

Mitigation: Install the oo CLI only through a verified, user-approved method, and do not allow an agent to run remote installer snippets automatically.

Risk: The skill can run write and destructive n8n actions that change or remove workflows, tables, tags, variables, or execution state.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before executing any write or destructive action.

## Reference(s):

- [ClawHub n8n skill](https://clawhub.ai/oomol/skills/oo-n8n)
- [n8n homepage](https://n8n.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI commands, action names, request payloads, and setup guidance for n8n connector access.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
