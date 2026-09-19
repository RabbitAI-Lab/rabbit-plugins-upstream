## Description:

This skill helps agents handle sevdesk contact workflows through OOMOL's oo CLI connector, including reading, creating, updating, and deleting contact data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate sevdesk contacts through an OOMOL-connected account, including creating, reading, listing, updating, and deleting contact records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote installer scripts in a shell.

Mitigation: Review the installer source before execution and prefer a pinned or verified oo CLI installation method.

Risk: The skill can create, update, or delete sevdesk contact data.

Mitigation: Confirm exact payloads, targets, and expected effects with the user before allowing write or destructive contact actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sevdesk)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [sevdesk homepage](https://sevdesk.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
