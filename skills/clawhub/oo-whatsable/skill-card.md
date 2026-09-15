## Description:

WhatsAble enables an agent to operate WhatsAble through an OOMOL-connected account, inspect live action schemas, and send WhatsApp text messages with optional attachment URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to send WhatsApp messages through WhatsAble from an OOMOL-connected account. The skill guides agents to inspect live schemas, construct JSON payloads, handle setup errors, and confirm state-changing message sends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup instructions could execute arbitrary code if the installer source is compromised or spoofed.

Mitigation: Review the installer path before use and prefer official installation documentation with version pinning or verification.

Risk: The send_message action changes WhatsAble state by sending a WhatsApp message.

Mitigation: Confirm the exact recipient, message content, and attachment URL with the user before running the action.

## Reference(s):

- [ClawHub WhatsAble Skill](https://clawhub.ai/oomol/skills/oo-whatsable)
- [WhatsAble Homepage](https://whatsable.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
