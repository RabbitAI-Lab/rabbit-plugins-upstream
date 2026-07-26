## Description: <br>
Guides LinkFox users through API-key setup, SMS-based registration, authentication recovery, and credit recharge flows for LinkFox agent skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and LinkFox users use this skill to configure LinkFox API credentials, recover from authentication failures, register by SMS verification, choose recharge plans, and create payment orders when account credits are insufficient. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask for phone verification codes and create or store API credentials. <br>
Mitigation: Use it only in a private environment, avoid sharing full tokens or codes in chat or logs, and store credentials in the intended environment variables. <br>
Risk: The skill can initiate LinkFox payment order flows. <br>
Mitigation: Confirm the selected plan and payment method explicitly before running order-creation scripts or scanning a payment code. <br>
Risk: The security review notes under-disclosed and weakly scoped controls around sensitive account and billing actions. <br>
Mitigation: Review the skill before installation and verify the configured LinkFox API endpoints before allowing scripts to contact external services. <br>


## Reference(s): <br>
- [LinkFox onboarding API contract](references/api.md) <br>
- [LinkFox Agent console](https://agent.linkfox.com/) <br>
- [LinkFox API key help document](https://yxgb3sicy7.feishu.cn/wiki/IlkawdQP9ifKv9k22xcc7rjmnkb) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-onboarding) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON script outputs, payment links, and QR-code file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a local PNG QR-code path and an ASCII QR fallback for payment flows.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
