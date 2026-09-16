## Description:

MyOTP.App helps an agent operate the MyOTP.App service through the OOMOL-connected oo CLI to inspect action schemas, generate and verify OTPs, check OTP status, extend OTP expiry, and retrieve transaction reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent perform MyOTP.App OTP workflows through an authenticated OOMOL connector, including schema inspection, OTP generation, verification, status checks, expiry extension, and transaction reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OTP-changing actions may be treated as safe reads because the skill does not label generate_otp, extend_otp, or verify_otp as write actions.

Mitigation: Require explicit user confirmation of the destination, channel, OTP identifier, payload, and expected effect before running those actions.

Risk: Remote installer commands can execute downloaded shell or PowerShell code directly.

Mitigation: Install the oo CLI only through a trusted, verified method and review installation commands before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-myotp-app)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [MyOTP.App Homepage](https://myotp.app)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
