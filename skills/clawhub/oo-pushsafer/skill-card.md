## Description:

Pushsafer (pushsafer.com). Use this skill for ANY Pushsafer request -- reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Pushsafer devices and groups and send Pushsafer notifications through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes direct execution of a remote installer.

Mitigation: Review the installer step before use and prefer installing the oo CLI through a verified package or a download-and-verify process.

Risk: The send_message action can deliver notifications to a selected device, group, or all devices.

Mitigation: Confirm the exact Pushsafer target and message payload with the user before running message-sending actions.

## Reference(s):

- [ClawHub Pushsafer skill](https://clawhub.ai/oomol/skills/oo-pushsafer)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Pushsafer homepage](https://www.pushsafer.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute Pushsafer connector actions through the oo CLI after confirming write payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
