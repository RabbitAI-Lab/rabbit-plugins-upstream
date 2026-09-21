## Description:

MyOTP.App helps agents operate MyOTP.App through the OOMOL oo CLI connector for OTP generation, verification, status checks, expiry extension, and transaction reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to manage MyOTP.App OTP workflows from an agent, including generating OTPs, verifying codes, checking status, extending expiry, and retrieving transaction reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can install the oo CLI by executing a remote script without verification.

Mitigation: Review the installer source or install oo from an official, verifiable package before running it.

Risk: OTP generation and expiry extension change MyOTP.App state.

Mitigation: Confirm the exact action payload and expected effect with the user before executing write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-myotp-app)
- [MyOTP.App Homepage](https://myotp.app)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
