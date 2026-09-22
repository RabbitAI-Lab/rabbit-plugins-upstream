## Description:

Deploys the Huawei Cloud Solution-as-Code Dify LLM application platform on ECS using Terraform, including solution metadata extraction, template normalization, variable review, deployment, verification, and cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to deploy and operate Dify on Huawei Cloud ECS through a Terraform/SAC workflow. It helps review pricing and variables, provision infrastructure, verify service access, and clean up resources.

### Deployment Geography for Use:

Huawei Cloud regions supported by the Terraform template, including cn-north-4, cn-southwest-2, cn-north-12, ap-southeast-3, cn-east-3, cn-north-9, cn-south-2, cn-south-1, tr-west-1, cn-south-4, ap-southeast-1, cn-north-2, cn-north-1, and cn-east-4.

## Known Risks and Mitigations:

Risk: The skill can create or delete paid Huawei Cloud resources.

Mitigation: Use a limited IAM user, review estimated price and terraform plan output, and require explicit confirmation before terraform apply or terraform destroy.

Risk: Cloud access keys may be stored in a local terraform.auto.tfvars.json file.

Mitigation: Prefer environment variables or a secret manager, never paste credentials into chat, keep tfvars local, and remove the credential file after successful destroy.

Risk: The Playwright CLI helper may fall back to npx when a local playwright-cli executable is unavailable.

Mitigation: Install and verify a vetted Playwright CLI directly before running extraction commands.

## Reference(s):

- [Huawei Cloud Dify SAC solution](https://www.huaweicloud.com/solution/implementations/building-a-dify-llm-application-development-platform.html)
- [Dify Terraform template](https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/flexus/dify-ecs.tf)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Related Commands](references/related-commands.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash and PowerShell commands plus JSON script outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes Terraform lifecycle commands, local tfvars configuration guidance, masked variable review output, and deployment verification steps.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
