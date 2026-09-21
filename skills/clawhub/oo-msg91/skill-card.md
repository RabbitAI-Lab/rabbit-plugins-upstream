## Description:

MSG91 (msg91.com). Use this skill for ANY MSG91 request: reading, creating, and updating data through the MSG91 connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to operate MSG91 through an OOMOL-connected account, including sending Flow SMS messages and generating, resending, or verifying OTP codes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Prefer a verified installation path for the oo CLI and review installer contents before execution.

Risk: SMS and OTP send or resend actions can affect users and account billing.

Mitigation: Confirm the exact payload and intended effect before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-msg91)
- [MSG91 homepage](https://msg91.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI MSG91 connector actions and returns response data with execution metadata when run.]

## Skill Version(s):

1.0.4 (source: evidence.json release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
