## Description:

Use this skill for Dida365 requests, including reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Dida365 tasks, projects, habits, and habit check-ins through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path documents a remote installer script for the oo CLI.

Mitigation: Review or verify the installer before execution, or install the oo CLI from a trusted package source.

Risk: The skill can change or delete Dida365 account data through write and destructive actions.

Mitigation: Confirm the exact payload, target, and expected effect with the user before write or destructive operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dida365)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Dida365 homepage](https://dida365.com)

## Skill Output:

**Output Type(s):** [shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schema inspection before action payload construction]

## Skill Version(s):

1.0.5 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
