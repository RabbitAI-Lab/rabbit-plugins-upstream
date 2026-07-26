## Description: <br>
Checks configured DeepSeek, Moonshot/Kimi, and Volcengine AI API account balances and summarizes the available credit for the user. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyya](https://clawhub.ai/user/kyya) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to check AI provider billing balances from their local environment before continuing API-dependent work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses configured provider API keys to read billing balance information. <br>
Mitigation: Configure only providers you use and prefer least-privilege or billing-read-only keys where each provider supports them. <br>
Risk: The optional Volcengine setup installs an unpinned Python SDK dependency. <br>
Mitigation: Review the setup script and pin or approve the Volcengine SDK version before installing it in managed environments. <br>


## Reference(s): <br>
- [Balance Checker on ClawHub](https://clawhub.ai/kyya/skills/balance-checker) <br>
- [DeepSeek User Balance API](https://api-docs.deepseek.com/zh-cn/api/get-user-balance) <br>
- [Moonshot User Balance API](https://platform.moonshot.cn/docs/api-reference#user-balance) <br>
- [Volcengine Billing API Documentation](https://www.volcengine.com/docs/6269/1593138) <br>
- [Volcengine IAM Key Management](https://console.volcengine.com/iam/keymanage/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Console text with Markdown documentation and shell/configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads provider credentials from environment variables or local OpenClaw configuration and prints balance summaries for configured providers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
