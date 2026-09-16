## Description:

Use this skill to operate Vonage through an OOMOL-connected account for account balance checks, SMS delivery records, delivery history, and sending SMS messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Vonage account and SMS delivery data and to send text or Unicode SMS through the Vonage connector without handling raw credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute a remote oo CLI installer directly.

Mitigation: Review the installer source and prefer a pinned or otherwise verifiable oo CLI installation method before use.

Risk: The send_sms action changes external state by sending SMS messages.

Mitigation: Confirm the exact recipient, message content, encoding, and expected effect before allowing the write action to run.

## Reference(s):

- [ClawHub Vonage Skill](https://clawhub.ai/oomol/skills/oo-vonage)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Vonage Homepage](https://www.vonage.com/)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are JSON when oo CLI actions are executed with --json.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
