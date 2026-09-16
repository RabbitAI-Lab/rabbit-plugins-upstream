## Description:

Helps an agent read, create, update, move, and delete Google Tasks data through the OOMOL-connected Google Tasks connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to operate Google Tasks task lists and tasks through an authenticated OOMOL connection. It supports read workflows as well as confirmed write and destructive task-management actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Use a verified, versioned oo CLI installation path and do not run remote installer commands automatically.

Risk: Write and destructive connector actions can change or delete Google Tasks data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any write or destructive action.

Risk: The skill relies on an OOMOL-managed Google Tasks connection.

Mitigation: Use it only when the user accepts OOMOL handling the Google Tasks connection and required account access.

## Reference(s):

- [ClawHub Google Tasks skill page](https://clawhub.ai/oomol/skills/oo-googletasks)
- [Google Tasks homepage](https://tasks.google.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when commands run with --json.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
