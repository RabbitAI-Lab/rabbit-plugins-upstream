## Description: <br>
One-click deployment tool for Hermes on Huawei Cloud Flexus L instances, including instance creation, ModelArts model configuration, robot channel configuration, and gateway management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operations engineers use this skill to deploy and configure the Hermes AI Agent platform on Huawei Cloud Flexus L instances. It supports manual and scripted workflows for provisioning, ModelArts setup, Feishu or WeCom channel configuration, gateway restart, execution-result queries, and UniAgent status checks. <br>

### Deployment Geography for Use: <br>
Huawei Cloud deployment regions documented by the skill: cn-north-4, cn-east-3, cn-south-1, and cn-southwest-2. <br>

## Known Risks and Mitigations: <br>
Risk: Powerful Huawei Cloud credentials can create or modify infrastructure and COC scripts. <br>
Mitigation: Use temporary, least-privilege credentials and review the IAM policy requirements before running deployment or configuration actions. <br>
Risk: Deployment can create paid prepaid monthly resources with auto-pay and auto-renew enabled. <br>
Mitigation: Confirm budget, billing behavior, target region, and cleanup plans before creating instances. <br>
Risk: Model, channel, and gateway actions can execute remote scripts as root on target hosts. <br>
Mitigation: Review remote script contents and host file permissions, then verify UniAgent and gateway state in a controlled environment before production use. <br>
Risk: Huawei Cloud AK/SK, security tokens, model API keys, and bot secrets are sensitive. <br>
Mitigation: Prefer environment variables or interactive secret entry, avoid command-line secrets where possible, and do not log or paste credential values. <br>


## Reference(s): <br>
- [IAM Permission Policy Reference](artifact/references/iam-policies.md) <br>
- [Skill Verification Method](artifact/references/verification-method.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-flexus-l-server-hermes-deployment) <br>
- [Publisher Profile](https://clawhub.ai/user/erickeyhu-hug) <br>
- [Huawei Cloud PyPI Index](https://repo.huaweicloud.com/repository/pypi/simple) <br>
- [ModelArts MaaS API Base](https://api.modelarts-maas.com/v2) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses interactive prompts or command-line arguments for Huawei Cloud credentials, target resources, model settings, channel settings, and COC execution parameters.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and scripts/pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
