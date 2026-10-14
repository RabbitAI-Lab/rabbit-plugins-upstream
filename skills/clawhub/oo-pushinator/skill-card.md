## Description:

Creates Pushinator channels and sends notifications to their subscribers through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Pushinator users and developers can create channels for subscribers and send notifications to a selected channel, subject to confirmation before changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The suggested CLI setup executes remote installer scripts that may change before installation.

Mitigation: Inspect the installer or use a verified, pinned package with a checked checksum or signature before running it.

Risk: Creating channels and sending notifications change Pushinator state.

Mitigation: Confirm the exact channel, notification payload, and intended effect with the user before each write action.

## Reference(s):

- [Pushinator skill on ClawHub](https://clawhub.ai/oomol/skills/oo-pushinator)
- [Pushinator](https://pushinator.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON action results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creating channels and sending notifications require user confirmation.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
