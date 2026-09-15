## Description:

ASIN Data API helps agents operate ASIN Data API through the OOMOL-connected oo CLI for reading, creating, updating, and deleting account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run ASIN Data API account actions through an OOMOL-connected CLI, including collection lookup, destination management, and request cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts executed in a local shell.

Mitigation: Use a verified oo CLI package or downloaded installer with checksum or signature validation before installation.

Risk: Write and destructive ASIN Data API actions can modify or remove account data.

Mitigation: Confirm the exact action, target, and payload with the user before running any write or destructive command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-asin-data-api)
- [ASIN Data API homepage](https://www.asindataapi.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from executed connector actions are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
