## Description: <br>
Deploy NewAPI LLM Gateway on Huawei Cloud via Terraform for multi-model management, load balancing, and key rotation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to deploy, review, verify, and clean up a NewAPI LLM Gateway on Huawei Cloud using Terraform. <br>

### Deployment Geography for Use: <br>
Huawei Cloud cn-north-4 region only <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or destroy public Huawei Cloud infrastructure through Terraform. <br>
Mitigation: Use scoped IAM credentials, review the downloaded Terraform and every terraform plan, and require explicit confirmation before apply or destroy. <br>
Risk: Huawei Cloud AK/SK values and ECS passwords may be persisted locally in terraform.auto.tfvars.json. <br>
Mitigation: Do not expose or collect tfvars contents, keep the file out of version control and artifacts, delete it after cleanup, and rotate credentials if exposure is possible. <br>
Risk: The deployment can expose SSH and the NewAPI web port on a public elastic IP. <br>
Mitigation: Restrict SSH and port 3000 access to intended sources and verify security group rules before applying changes. <br>


## Reference(s): <br>
- [Huawei Cloud NewAPI LLM Gateway Solution](https://www.huaweicloud.com/solution/implementations/building-a-newapi-llm-gateway.html) <br>
- [Huawei Cloud Terraform Template](https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/building-a-newapi-llm-gateway/building-a-newapi-llm-gateway.tf.json) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Related Commands](references/related-commands.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration steps, and JSON output descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes Terraform workflow guidance, masked variable review, deployment verification, and cleanup steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
