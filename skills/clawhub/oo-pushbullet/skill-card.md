## Description:

Operate Pushbullet through an OOMOL-connected account for reading, creating, updating, and deleting Pushbullet data instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to perform Pushbullet read, write, and destructive actions through the OOMOL `oo` CLI after checking the live connector schema and confirming state-changing requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes direct remote script execution for installing the OOMOL CLI.

Mitigation: Review the installer before running it and prefer a signed or checksum-verified installation path when available.

Risk: Write and destructive Pushbullet actions can create, update, mute, dismiss, or delete user data.

Mitigation: Check the live action schema, exact target, and complete payload, then obtain explicit user approval before running state-changing commands.

Risk: Commands operate against the currently connected OOMOL Pushbullet account.

Mitigation: Confirm the intended account and connection state before executing actions that expose profile, chat, device, or push data.

## Reference(s):

- [ClawHub Pushbullet skill page](https://clawhub.ai/oomol/skills/oo-pushbullet)
- [Pushbullet homepage](https://www.pushbullet.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions should use live connector schemas before constructing payloads; state-changing actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
