## Description:

Use this skill to read, create, update, and delete UptimeRobot data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage UptimeRobot monitors, account details, and alert contacts through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes executing remote installer scripts directly in a shell.

Mitigation: Review setup steps before installation and prefer a trusted, versioned, integrity-checked oo CLI installation method.

Risk: Monitor create, update, and delete actions can change or remove UptimeRobot resources.

Mitigation: Confirm the exact payload, target monitor, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [UptimeRobot homepage](https://uptimerobot.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-uptimerobot)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: skill metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
