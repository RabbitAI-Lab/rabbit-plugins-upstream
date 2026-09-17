## Description:

MyOTP.App helps agents operate MyOTP.App through the OOMOL-connected oo CLI for OTP generation, verification, status checks, expiry extensions, and transaction reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with an OOMOL-connected MyOTP.App account use this skill to inspect action schemas and run OTP lifecycle operations, including generation, delivery-status checks, verification, expiry extension, and transaction reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive OTP actions can generate, extend, or verify one-time passcodes through a connected account.

Mitigation: Require explicit user confirmation of the action, payload, destination, and expected effect before generating, extending, or verifying OTPs.

Risk: The artifact includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Install the oo CLI separately from an official, verifiable source and do not let an agent run remote installer commands automatically.

Risk: MyOTP.App actions are mediated through OOMOL-connected credentials.

Mitigation: Use the skill only when the user accepts OOMOL mediation and has reviewed the connected account scopes and billing impact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-myotp-app)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [MyOTP.App homepage](https://myotp.app)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live action schemas before execution and require confirmation before sensitive OTP state changes.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
