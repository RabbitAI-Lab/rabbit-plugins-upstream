## Description:

SMS Alert helps an agent operate an OOMOL-connected SMS Alert account for SMS, OTP, template, sender ID, and credit balance workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage SMS Alert account workflows, including checking credits and templates, generating or validating OTPs, and sending direct SMS messages after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send SMS and OTP messages from a real SMS Alert account.

Mitigation: Require explicit user confirmation for recipients, message contents, and OTP actions before executing write operations.

Risk: First-time setup includes remote installer commands for the OOMOL CLI.

Mitigation: Run installer commands only after independently reviewing or verifying the OOMOL CLI source.

Risk: The security verdict is suspicious because setup and action guidance can expose users to unverified installer execution and unconfirmed SMS or OTP actions.

Mitigation: Review the skill before installation and enforce the documented confirmation checks for state-changing actions.

## Reference(s):

- [SMS Alert homepage](https://www.smsalert.co.in/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [SMS Alert skill on ClawHub](https://clawhub.ai/oomol/skills/oo-sms-alert)

## Skill Output:

**Output Type(s):** [Text, Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before constructing JSON payloads; write SMS actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
