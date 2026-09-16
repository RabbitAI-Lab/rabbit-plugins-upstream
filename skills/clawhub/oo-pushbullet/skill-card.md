## Description:

Pushbullet (pushbullet.com). Use this skill for ANY Pushbullet request: reading, creating, updating, and deleting data through the OOMOL Pushbullet connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Pushbullet from an agent through the OOMOL CLI, including reading profile, chat, device, and push data and creating or updating pushes, chats, and devices. It also documents confirmation expectations for write and destructive Pushbullet actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence flags the skill as suspicious because fallback setup instructs users to execute an unverified remote installer.

Mitigation: Review the OOMOL CLI installation path before use, install oo from a verified versioned source where possible, and validate checksums or signatures when available.

Risk: Write and destructive Pushbullet actions can change or delete account data.

Mitigation: Confirm the exact target, action, and payload with the user before approving write or delete actions.

## Reference(s):

- [Pushbullet homepage](https://www.pushbullet.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke live OOMOL connector schemas and Pushbullet connector actions through the oo CLI.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
