## Description:

Deploys the Dify-based FlexusAgent AI Agent development platform on Huawei Cloud Flexus L instances, with workflows for deployment, admin password management, MaaS model configuration, and workflow import.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to provision a Huawei Cloud Flexus L instance, deploy FlexusAgent, reset the Dify administrator password, configure Huawei Cloud MaaS models, and import preset Dify workflows.

### Deployment Geography for Use:

Huawei Cloud regions cn-north-4, cn-east-3, cn-south-1, and cn-southwest-2.

## Known Risks and Mitigations:

Risk: The skill requires cloud-provisioning authority and COC remote execution permissions.

Mitigation: Use least-privilege temporary Huawei credentials, confirm cost-incurring actions explicitly, and review IAM scope before installation.

Risk: The skill handles Huawei Cloud credentials and FlexusAgent administrator passwords.

Mitigation: Prefer environment-provided temporary credentials, avoid command-line secrets where possible, mask sensitive values, and rotate any credential or password that appears in logs or chat.

Risk: Admin and MaaS credentials may be sent to an HTTP Web UI endpoint after deployment.

Mitigation: Do not rely on HTTP for sensitive administration; place the service behind a trusted secure channel before entering administrator or MaaS credentials.

Risk: Password reset and workflow import rely on externally downloaded shell scripts.

Mitigation: Review or replace the external curl-to-bash scripts before running password reset or workflow import operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-flexus-l-server-flexusagent-deployment)
- [IAM permission policy reference](references/iam-policies.md)
- [Skill verification method](references/verification-method.md)
- [Flexus L instance purchase guide](https://support.huaweicloud.com/api-flexusl/create_instance_0001.html)
- [Flexus L instance specifications](https://support.huaweicloud.com/productdesc-flexusl/pd_01_0003.html)
- [FlexusAgent workflow template index](https://flexus-config-cn-north-4-product.obs.cn-north-4.myhuaweicloud.com/stable/dify/dify-templates/national/index.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, configuration values, status summaries, and verification steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce cloud resource identifiers, Web UI URLs, operation status, and masked credential handling guidance.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
