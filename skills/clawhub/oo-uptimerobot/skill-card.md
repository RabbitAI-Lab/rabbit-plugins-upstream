## Description:

UptimeRobot (uptimerobot.com). Use this skill for reading, creating, updating, and deleting UptimeRobot monitors through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage UptimeRobot monitors through an OOMOL-connected account, including monitor lifecycle operations, account details, alert contacts, and status inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Review or verify the installer through OOMOL's official installation guide before running remote installation commands.

Risk: Create, update, and delete actions can change or remove UptimeRobot monitor data.

Mitigation: Confirm exact payloads, affected monitors, and expected effects with the user before running write or destructive actions.

## Reference(s):

- [UptimeRobot homepage](https://uptimerobot.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill relies on live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
