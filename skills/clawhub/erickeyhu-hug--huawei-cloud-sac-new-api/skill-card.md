## Description:

Deploy NewAPI LLM Gateway on Huawei Cloud via Terraform for unified LLM API management, load balancing, key rotation, and usage statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to prepare, review, deploy, verify, and clean up a NewAPI LLM Gateway on Huawei Cloud using Terraform and helper scripts.

### Deployment Geography for Use:

Global; the deployment workflow itself is limited to Huawei Cloud region cn-north-4.

## Known Risks and Mitigations:

Risk: The skill prepares and runs Terraform against a Huawei Cloud account, which can create billable infrastructure.

Mitigation: Use a least-privilege IAM user, inspect Terraform plan output, and require explicit confirmation before apply.

Risk: The workflow uses Huawei Cloud AK/SK credentials and writes terraform.auto.tfvars.json.

Mitigation: Do not share credentials in chat, keep terraform.auto.tfvars.json out of version control and backups, and delete it after use.

Risk: Terraform destroy is a destructive action that can remove deployed resources.

Mitigation: Review destroy plans and require separate explicit confirmation before running destroy.

## Reference(s):

- [Huawei Cloud NewAPI LLM Gateway Solution](https://www.huaweicloud.com/solution/implementations/building-a-newapi-llm-gateway.html)
- [Terraform Template](https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/building-a-newapi-llm-gateway/building-a-newapi-llm-gateway.tf.json)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Related Commands](references/related-commands.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, json]

**Output Format:** [Markdown guidance with shell commands and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes Terraform workflow steps, masked variable inspection, deployment verification commands, and cleanup guidance.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
