## Description: <br>
Step-by-step guide for integrating Moonshot AI (Kimi) and Kimi Code models into Clawdbot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[evgyur](https://clawhub.ai/user/evgyur) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to configure Clawdbot for Moonshot AI and Kimi Code models, including API keys, provider settings, model aliases, and connection checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys can be exposed through terminal history, shell output, configuration files, or logs. <br>
Mitigation: Store keys in a protected .env file or secret manager, avoid printing full keys, and revoke keys if they are exposed. <br>
Risk: The connection test sends prompts to Moonshot/Kimi endpoints using the configured credentials. <br>
Mitigation: Run the test script only with non-sensitive prompts and credentials that can be rotated. <br>
Risk: Configuring these providers routes Clawdbot model requests through Moonshot/Kimi services. <br>
Mitigation: Install and enable the skill only when that routing is intended and acceptable for the deployment. <br>


## Reference(s): <br>
- [Moonshot AI Documentation](https://platform.moonshot.cn/docs) <br>
- [Kimi Code API Documentation](https://api.kimi.com/coding/docs) <br>
- [Clawdbot Model Providers](https://docs.clawd.bot/concepts/model-providers) <br>
- [Configuration Examples](references/config-examples.md) <br>
- [Kimi Integration on ClawHub](https://clawhub.ai/evgyur/skills/kimi-integration) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with JSON, JSON5, bash, and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes environment variable names and provider endpoint examples; users supply their own API keys.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
