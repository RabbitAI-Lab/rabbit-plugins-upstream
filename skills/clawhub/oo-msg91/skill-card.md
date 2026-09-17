## Description:

MSG91 (msg91.com). Use this skill for ANY MSG91 request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run MSG91 SMS and OTP actions through an OOMOL-connected account with the oo CLI. It supports resending, sending, and verifying OTPs, plus sending approved Flow template SMS messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded code.

Mitigation: Review the installer source and prefer a verified or package-manager installation of the oo CLI before use.

Risk: SMS and OTP write actions can affect recipients and account usage.

Mitigation: Confirm SMS or OTP payloads and intended effects with the user before execution.

## Reference(s):

- [MSG91 homepage](https://msg91.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL MSG91 connection](https://console.oomol.com/app-connections?provider=msg91)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before action execution and returns connector responses with data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
