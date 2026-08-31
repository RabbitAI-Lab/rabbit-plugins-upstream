## Description:

Twilio lets agents operate an OOMOL-connected Twilio account to read account, call, message, and usage data and to send outbound messages or calls through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Twilio account, call, message, and usage records and to create outbound SMS/MMS messages or voice calls through an OOMOL-connected credential.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outbound SMS/MMS messages and voice calls can affect recipients and billing.

Mitigation: Review the exact action payload and expected effect with the user before approving write actions.

Risk: The skill depends on an active OOMOL/Twilio account connection.

Mitigation: Install only when OOMOL-connected Twilio access is intended, and revoke the connection when it is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-twilio)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Twilio Homepage](https://www.twilio.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON payloads/results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action payloads and asks for user confirmation before write or destructive actions.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
