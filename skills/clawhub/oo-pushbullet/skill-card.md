## Description:

Operate Pushbullet through OOMOL's oo CLI to read, create, update, and delete Pushbullet data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Pushbullet account from an agent, including sending pushes, listing chats/devices/pushes, and managing Pushbullet resources after confirmation for write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands for the OOMOL CLI.

Mitigation: Install the CLI only after independently trusting and verifying the installer source; do not run remote installer commands automatically.

Risk: Write and destructive Pushbullet actions can change or delete account data.

Mitigation: Confirm the exact payload, target, and effect before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Pushbullet skill page](https://clawhub.ai/oomol/skills/oo-pushbullet)
- [Pushbullet homepage](https://www.pushbullet.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands invoke the oo CLI and return connector JSON responses that include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: evidence.json release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
