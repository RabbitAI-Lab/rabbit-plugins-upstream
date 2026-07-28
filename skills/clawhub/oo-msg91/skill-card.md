## Description: <br>
MSG91 helps agents operate an OOMOL-connected MSG91 account for OTP workflows and Flow-template SMS messaging through the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to send, resend, and verify MSG91 OTP codes and send SMS messages through approved MSG91 Flow templates from an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OTP and SMS operations can affect an MSG91 account or end users, and the security summary notes that sensitive OTP actions are under-labeled as safe. <br>
Mitigation: Require explicit user confirmation before sending, resending, or verifying OTP/SMS actions, and inspect the live action schema before constructing payloads. <br>


## Reference(s): <br>
- [ClawHub MSG91 skill page](https://clawhub.ai/oomol/skills/oo-msg91) <br>
- [MSG91 homepage](https://msg91.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs MSG91 connector actions through an OOMOL-connected account; action schemas should be inspected before payload construction.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
