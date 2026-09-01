## Description:

Z-API helps agents operate a user's OOMOL-connected Z-API account for WhatsApp instance status checks and user-confirmed text, image, or location messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Z-API through an OOMOL-connected account. It supports checking instance status and sending user-confirmed WhatsApp text, image, or location messages to contacts or groups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can send WhatsApp text, image, or location messages through the connected instance.

Mitigation: Confirm the exact recipient, content, and intended effect with the user before running send_text, send_image, or send_location.

Risk: The skill routes Z-API access through OOMOL as the intermediary for the user's connection.

Mitigation: Install or run the skill only when the user trusts OOMOL for the connected Z-API account.

## Reference(s):

- [Z-API homepage](https://www.z-api.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-z-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector payloads should be based on the live action schema; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
