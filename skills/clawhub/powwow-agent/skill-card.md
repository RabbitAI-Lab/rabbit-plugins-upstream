## Description:

Helps OpenClaw users create and manage a chat-capable digital human on the PowPow map, including account access, badges, subscriptions, and visitor conversations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to place a digital human on the PowPow map, manage its account and badge status, and respond to visitors. An optional companion channel plugin handles ongoing conversations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account and webhook secrets may be exposed through local plaintext credentials, synced folders, or shared files.

Mitigation: Keep credentials.json out of shared, backed-up, and version-controlled folders; prefer environment or secret-manager handling where possible.

Risk: A leaked webhook token can authorize messages as the digital human.

Mitigation: Treat webhook tokens as secrets and avoid sharing credentials.json or terminal logs containing them.

## Reference(s):

- [PowPow Agent on ClawHub](https://clawhub.ai/durenzidu/skills/powwow-agent)
- [PowPow map](https://global.powpow.online/map)
- [PowPow channel plugin](https://clawhub.ai/durenzidu/plugins/openclaw-channel-powpow)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions]

**Output Format:** [Text with shell commands and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes account status, digital-human details, visitor messages, and setup guidance.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
