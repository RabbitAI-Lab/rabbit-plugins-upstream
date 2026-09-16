## Description:

MSG91 lets agents operate an OOMOL-connected MSG91 account for Flow SMS and OTP send, resend, and verification actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to send MSG91 Flow template SMS messages and manage OTP delivery or verification through an OOMOL-connected MSG91 account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that fetch and execute scripts.

Mitigation: Use installer recovery only when the oo CLI is missing, and independently verify the installer source before execution.

Risk: resend_otp can affect a recipient even though the source skill does not tag it as a write action.

Mitigation: Treat resend_otp as a write action and confirm the recipient, channel, and intended effect before use.

Risk: The skill operates through OOMOL-mediated MSG91 access.

Mitigation: Use it only when the user accepts OOMOL-connected MSG91 credential handling, and inspect the live connector schema before building payloads.

## Reference(s):

- [ClawHub MSG91 skill](https://clawhub.ai/oomol/skills/oo-msg91)
- [MSG91 homepage](https://msg91.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL MSG91 connection](https://console.oomol.com/app-connections?provider=msg91)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before action execution.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
