## Description: <br>
Dknowc Gov Zhicha helps answer China-focused government-service, public-service, social-security, housing-fund, certificate, subsidy, policy-fit, process, materials, entry-point, and official-basis questions using Dknowc's trusted unified interface. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to register for Dknowc's trusted unified interface, configure a local API key, and answer China government-service or public-policy questions with executable steps, required materials, service channels, and cited source material. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: First-use registration sends a phone number and SMS verification code to Dknowc's external service. <br>
Mitigation: Use the skill only when that account-registration flow and data sharing are acceptable for the user or organization. <br>
Risk: The generated config.ini contains a local API key. <br>
Mitigation: Treat config.ini as a secret, do not commit or share the installed skill directory, and rotate or delete the key if the machine is shared or compromised. <br>
Risk: Government-service answers may vary by locality and depend on external service results. <br>
Mitigation: Provide the relevant province, city, or district when known and review cited source fields before acting on important service or policy guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-gov-zhicha-public) <br>
- [Dknowc trusted unified interface endpoint](https://open.dknowc.cn/chat/trusted/unification) <br>
- [Dknowc ClawHub channel registration](https://platform.dknowc.cn/auth/#/register?channel=2787E171-B0E5-4328-9946-47AC52434D1F&type=11) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration] <br>
**Output Format:** [Plain text or JSON, with optional shell commands and local configuration updates during registration.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Answers can include referenced source fields, online-service item lists, policy-file lists, and generated local config.ini credentials.] <br>

## Skill Version(s): <br>
1.0.6 (source: evidence release and _meta.json; changelog released 2026-07-14) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
