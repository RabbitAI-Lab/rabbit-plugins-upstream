## Description:

Deploys the NewAPI LLM Gateway on Huawei Cloud via Terraform for unified multi-model API gateway management, load balancing, and key rotation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to prepare, deploy, verify, and clean up a Huawei Cloud Terraform deployment of the NewAPI LLM Gateway. It guides solution information extraction, template normalization, variable review, Terraform execution, service verification, and cleanup.

### Deployment Geography for Use:

Global; the deployment target is limited by the artifact to Huawei Cloud cn-north-4.

## Known Risks and Mitigations:

Risk: Huawei Cloud access keys and Terraform variable files can expose cloud credentials if copied into chat, logs, or version control.

Mitigation: Use a least-privilege IAM user, keep AK/SK out of chat, do not display terraform.auto.tfvars.json, and remove that file after cleanup.

Risk: Terraform apply or destroy can create billable infrastructure or remove deployed resources.

Mitigation: Review terraform plan output and require explicit user confirmation before apply or destroy.

Risk: The deployment opens SSH and NewAPI web access paths that may be reachable from the public internet.

Mitigation: Restrict SSH and port 3000 exposure, verify security group rules, and confirm the running service only after the intended access controls are in place.

Risk: The skill downloads and normalizes a remote Terraform template before deployment.

Mitigation: Verify the downloaded template source and review generated Terraform configuration before applying changes.

## Reference(s):

- [Huawei Cloud Building a NewAPI LLM Gateway solution](https://www.huaweicloud.com/solution/implementations/building-a-newapi-llm-gateway.html)
- [Huawei Cloud Solution-as-Code Terraform template](https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/building-a-newapi-llm-gateway/building-a-newapi-llm-gateway.tf.json)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Related Commands](references/related-commands.md)
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-sac-new-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON output descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes sensitive-value masking expectations and requires user confirmation before Terraform apply or destroy.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
