## Description:

Enables agents to read, create, and update Taiga projects and work items through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, project managers, and agents use this skill to operate Taiga projects, issues, tasks, and user stories through an OOMOL-connected account while confirming write payloads before changes are made.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes running downloaded installer scripts.

Mitigation: Prefer vendor-documented package or release options, inspect the downloaded script, and verify integrity before running it.

Risk: Write actions can change Taiga projects and work items.

Mitigation: Fetch the live action schema, confirm the exact payload and effect with the user before create or update actions, and require explicit approval for destructive actions.

Risk: OOMOL handles Taiga access through its connector.

Mitigation: Use the skill only when comfortable with OOMOL-managed Taiga access and connect an account with appropriate permissions.

## Reference(s):

- [Taiga homepage](https://taiga.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-taiga)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live oo connector schema inspection before payload construction and user confirmation for write or destructive actions.]

## Skill Version(s):

1.0.2 (source: SKILL.md metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
