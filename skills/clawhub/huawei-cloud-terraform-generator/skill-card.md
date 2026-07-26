## Description: <br>
Generate Huawei Cloud Terraform configurations and execute deployment with user-guided approval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to turn Huawei Cloud infrastructure goals into Terraform configurations, validate plans, estimate cost, and apply deployments after explicit user approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated Terraform can create real Huawei Cloud resources and cause cost, network exposure, or account changes. <br>
Mitigation: Review the Terraform plan, cost estimate, opened ports, and IAM or account changes before approving apply. <br>
Risk: Generated .tfvars files or placeholder values may contain sensitive deployment material. <br>
Mitigation: Do not commit real credentials or secrets, and replace placeholder sample passwords with properly managed values where needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-terraform-generator) <br>
- [Guardrails](artifact/reference/guardrails.md) <br>
- [Terraform Generation Guide](artifact/reference/terraform-generation-guide.md) <br>
- [Validation Workflow](artifact/reference/validation-workflow.md) <br>
- [Huawei Cloud Terraform Provider Mirror](https://mirrors.huaweicloud.com/terraform/) <br>
- [Huawei Cloud Pricing Calculator](https://www.huaweicloud.com/pricing.html#/calculator) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with Terraform/HCL files, inline shell commands, and deployment guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate Terraform project files such as providers.tf, variables.tf, main.tf, terraform.tfvars, and README.md.] <br>

## Skill Version(s): <br>
0.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
