## Description:

MyOTP.App lets an agent operate a connected MyOTP.App account to generate, verify, extend, and check OTP messages and retrieve transaction reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to let agents work with MyOTP.App through an OOMOL-connected account. It supports OTP delivery by SMS or WhatsApp, OTP verification, expiry extension, status checks, and paginated transaction reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger security-sensitive OTP actions, including generation, extension, and verification, through the connected MyOTP.App account.

Mitigation: Require explicit user confirmation for OTP-generation, extension, and verification payloads before running the action.

Risk: The skill under-labels security-sensitive OTP actions even though they can change authentication state.

Mitigation: Review the action schema and intended effect before execution, and treat OTP-changing operations as sensitive writes.

## Reference(s):

- [MyOTP.App homepage](https://myotp.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-myotp-app)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI connector schema and run actions with JSON payloads.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
