## Description: <br>
Deploys the AI Agent development platform Dify on a Huawei Cloud Flexus L instance, with deployment, password management, MaaS model configuration, and workflow import support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to deploy and operate a Dify-based FlexusAgent environment on Huawei Cloud Flexus L, then configure administrator access, MaaS model providers, and reusable workflows. <br>

### Deployment Geography for Use: <br>
China regions supported by the skill: cn-north-4, cn-east-3, cn-south-1, and cn-southwest-2. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create real Huawei Cloud resources that may incur costs and leave persistent infrastructure changes. <br>
Mitigation: Use it first in a test or tightly controlled Huawei Cloud account, require explicit deployment confirmation, and verify cleanup and billing impact after use. <br>
Risk: The skill handles access keys, security tokens, passwords, and signed request material that could be exposed through shared logs or transcripts. <br>
Mitigation: Use least-privilege temporary credentials, keep credentials out of conversations and command history, mask access details in outputs, and rotate any credential that may have been exposed. <br>
Risk: The security guidance flags mutable remote scripts on cloud instances as a production-use concern. <br>
Mitigation: Review or replace remote curl-to-bash scripts before production use and restrict execution to controlled infrastructure until reviewed. <br>


## Reference(s): <br>
- [IAM Permission Policy Reference](references/iam-policies.md) <br>
- [Skill Verification Method](references/verification-method.md) <br>
- [Huawei Cloud Flexus L Instance Purchase Guide](https://support.huaweicloud.com/api-flexusl/create_instance_0001.html) <br>
- [Huawei Cloud Flexus L Instance Specifications](https://support.huaweicloud.com/productdesc-flexusl/pd_01_0003.html) <br>
- [FlexusAgent Workflow Template Index](https://flexus-config-cn-north-4-product.obs.cn-north-4.myhuaweicloud.com/stable/dify/dify-templates/national/index.json) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance, API calls] <br>
**Output Format:** [Markdown with inline bash commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include cloud resource identifiers, Web UI URLs, administrator access details, and verification steps; sensitive values require masking.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, skill metadata, pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
