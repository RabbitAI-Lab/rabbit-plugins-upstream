## Description:

Google Tasks (tasks.google.com). Use this skill for ANY Google Tasks request: reading, creating, updating, and deleting task data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to let an agent inspect Google Tasks lists and tasks, then create, update, move, clear, or delete Google Tasks items after required confirmation for write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that can execute code on the user's machine.

Mitigation: Review the installer source before use and prefer package-manager or verified-download installation paths when available.

Risk: Write and destructive actions can modify, clear, or delete Google Tasks data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running actions marked write or destructive.

Risk: Connector schemas may change over time, causing stale payload assumptions.

Mitigation: Fetch the live action schema with `oo connector schema` before constructing each connector payload.

## Reference(s):

- [Google Tasks homepage](https://tasks.google.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL Google Tasks connection](https://console.oomol.com/app-connections?provider=googletasks)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and return connector responses as JSON.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
