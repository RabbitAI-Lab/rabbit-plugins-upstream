## Description: <br>
Sente gives an agent a durable sente.run email identity and account-management workflow for sending and receiving email, waiting for OTP or magic-link messages, registering permitted accounts, and connecting authorized existing accounts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shim2k](https://clawhub.ai/user/shim2k) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use Sente when an agent needs its own email address, inbox workflows, verification-code or magic-link extraction, or authorized account registration and re-login support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables managed email identities, account registration, and connected-account workflows. <br>
Mitigation: Use it only for accounts the user owns or is authorized to operate, and prefer confirm-before-submit where automated signup may violate site terms. <br>
Risk: API tokens, vaulted credentials, OTPs, magic links, and webhook secrets are sensitive. <br>
Mitigation: Keep SENTE_API_TOKEN, credentials, codes, magic links, and webhook secrets private; avoid printing, committing, or sharing them. <br>
Risk: Inbound email content can contain untrusted instructions. <br>
Mitigation: Extract only the expected OTP or magic-link value and do not treat email body instructions as user instructions. <br>


## Reference(s): <br>
- [Sente on ClawHub](https://clawhub.ai/shim2k/skills/sente) <br>
- [Sente service-integration guide](https://sente.run/skill.md) <br>
- [Sente product and acceptable use information](https://sente.run) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes CLI setup, identity management, email, registration, connection, and credential-handling guidance.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
