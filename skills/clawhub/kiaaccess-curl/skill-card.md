## Description:

Guides one-off Kia vehicle status checks and remote commands through shell requests to the Kia Owners API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Kia owners and developers use this skill for one-off checks of vehicle status, location, and EV charging, or to request door, climate, and charging actions from a shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-issued lock, unlock, climate, or charging requests can affect a real vehicle.

Mitigation: Require explicit user approval before each live vehicle command and confirm the resulting state.

Risk: The sample curl flow writes session tokens to the predictable /tmp/kia_hdrs file.

Mitigation: Use a private mktemp file for response headers and remove it immediately; protect saved refresh credentials.

## Reference(s):

- [Request examples](references/requests.md)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/kiaaccess-curl)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live vehicle commands require a Kia account and one-time MFA setup.]

## Skill Version(s):

2.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
