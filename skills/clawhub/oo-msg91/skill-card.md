## Description: <br>
MSG91 (msg91.com). Use this skill for ANY MSG91 request -- reading, creating, and updating data. Whenever a task involves MSG91, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to work with MSG91 through an OOMOL-connected account, including sending approved Flow SMS messages and managing OTP send, resend, and verification workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The resend_otp action can send messages through the user's MSG91 account even though the skill text does not label it as a write action. <br>
Mitigation: Review the action and payload before allowing OTP resend, send OTP, or SMS send actions to run. <br>
Risk: The skill depends on the OOMOL oo CLI and a connected MSG91 account. <br>
Mitigation: Install the oo CLI only from OOMOL when that provider is trusted, and connect MSG91 only when the user intends to grant account access. <br>


## Reference(s): <br>
- [MSG91 Homepage](https://msg91.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live OOMOL connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
