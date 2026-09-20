## Description:

Ongage (ongage.com). Use this skill for ANY Ongage request: reading, creating, updating, and deleting data through the OOMOL-connected Ongage connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate Ongage contact and list workflows through the oo CLI, including reads, updates, upserts, and contact status changes. The skill is intended for schema-first execution against an already connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs agents to execute remote installer scripts for the oo CLI.

Mitigation: Review the OOMOL CLI installation path first and prefer a trusted package manager or inspected installer before running installation commands.

Risk: The skill can perform write and destructive Ongage actions, including contact updates, upserts, and contact status changes.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running any write or destructive action.

## Reference(s):

- [Ongage homepage](https://www.ongage.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ongage)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live connector schemas before running actions; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
