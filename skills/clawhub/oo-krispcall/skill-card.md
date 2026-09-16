## Description:

Use this skill for KrispCall requests such as reading, creating, updating, and deleting KrispCall data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected KrispCall workspace through the OOMOL oo CLI, including contacts, workspace profile, and team member visibility. Write and destructive contact actions require user confirmation before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup documents pipe-to-shell installer commands for the oo CLI.

Mitigation: Independently trust and verify the oo CLI installer before running remote installer commands.

Risk: KrispCall write and destructive operations can create, update, or delete contact data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [KrispCall homepage](https://krispcall.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-krispcall)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schema and run commands; responses may include JSON data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
