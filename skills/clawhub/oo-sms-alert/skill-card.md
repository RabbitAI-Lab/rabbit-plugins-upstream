## Description:

SMS Alert helps agents operate SMS Alert through the OOMOL oo CLI and sms_alert connector for reading account data, generating or validating OTPs, and sending SMS messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect SMS Alert action schemas, check account resources, generate or validate OTPs, and send SMS messages through an OOMOL-connected SMS Alert account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One-line remote installer commands can execute downloaded code before the user has verified the source or integrity.

Mitigation: Use the documented install guide or manually inspect and verify installer content before running installation commands.

Risk: SMS-sending and OTP-generation actions can consume credits or send messages to recipients.

Mitigation: Confirm the exact recipient, payload, and expected effect with the user before running any message-sending or OTP-generation action.

Risk: The security scan reports that one SMS-sending action is not clearly gated as a write action.

Mitigation: Treat all actions that send messages or generate OTPs as write actions requiring explicit user confirmation.

## Reference(s):

- [SMS Alert homepage](https://www.smsalert.co.in/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [SMS Alert skill page](https://clawhub.ai/oomol/skills/oo-sms-alert)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are intended to inspect live connector schemas before running SMS Alert actions.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
