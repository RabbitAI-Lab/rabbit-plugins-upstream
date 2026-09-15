## Description:

Mocean enables agents to read Mocean account data and send SMS through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Mocean account information, check pricing and delivery status, look up phone-number carrier data, and send SMS messages after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup flow includes direct execution of remote installer scripts.

Mitigation: Review the official installation documentation, download installers separately when possible, and verify signatures or checksums before execution.

Risk: SMS sending is a billable write action that can contact external recipients.

Mitigation: Confirm the exact recipient, message content, payload, and expected effect with the user before running the send_sms action.

## Reference(s):

- [Mocean homepage](https://moceanapi.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mocean)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include connector command output wrapped as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
