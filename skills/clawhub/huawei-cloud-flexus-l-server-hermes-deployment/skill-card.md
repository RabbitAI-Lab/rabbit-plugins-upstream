## Description: <br>
One-click deployment tool for Hermes on Huawei Cloud Flexus L instances, with ModelArts large model configuration and Feishu or WeCom channel configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to deploy Hermes on Huawei Cloud Flexus L instances, configure ModelArts model access, manage bot channels, restart the Hermes gateway, and check UniAgent or COC execution status. <br>

### Deployment Geography for Use: <br>
Huawei Cloud regions supported by the skill: cn-north-4, cn-east-3, cn-south-1, and cn-southwest-2. <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses powerful Huawei Cloud credentials and can create cloud resources or execute COC scripts on target instances. <br>
Mitigation: Review before installing, use dedicated least-privilege temporary credentials, and inspect COC script behavior before allowing non-interactive execution on production instances. <br>
Risk: Deployment can incur cost because the artifact creates Flexus L resources and includes auto-pay and auto-renew behavior. <br>
Mitigation: Use a test account or budget controls first, confirm billing settings before deployment, and closely monitor or disable auto-pay and auto-renew resources after use. <br>
Risk: Credentials and bot secrets are sensitive, and examples include command-line parameters for AK/SK, ModelArts API keys, and channel secrets. <br>
Mitigation: Prefer environment-based secret handling where possible, avoid exposing secrets in chat or shell history, and rotate credentials after testing. <br>


## Reference(s): <br>
- [IAM policy reference](references/iam-policies.md) <br>
- [Verification method](references/verification-method.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and JSON-shaped command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Huawei Cloud credentials, Python 3, uv, and supported Huawei Cloud regions.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
