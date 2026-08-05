## Description: <br>
Deploys NewAPI LLM Gateway on Huawei Cloud via Terraform for unified multi-model API management, load balancing, and key rotation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to deploy and verify a NewAPI LLM gateway on Huawei Cloud using Terraform, Python helper scripts, and Playwright-based solution-page extraction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uses Huawei Cloud credentials and can create paid cloud resources. <br>
Mitigation: Use a limited-permission IAM user, review Terraform plan output and estimated cost before apply, and require explicit confirmation for apply or destroy. <br>
Risk: The workflow stores cloud keys locally in terraform.auto.tfvars.json. <br>
Mitigation: Keep terraform.auto.tfvars.json out of version control, avoid displaying its contents, and delete it after cleanup. <br>
Risk: The workflow relies on mutable remote Terraform and bootstrap code. <br>
Mitigation: Review the downloaded Terraform template and bootstrap scripts before running terraform apply. <br>
Risk: The deployment exposes SSH and the NewAPI web port on a public Elastic IP. <br>
Mitigation: Restrict security group source ranges where supported and verify that no unnecessary ports are exposed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-sac-new-api) <br>
- [Huawei Cloud NewAPI LLM Gateway Solution](https://www.huaweicloud.com/solution/implementations/building-a-newapi-llm-gateway.html) <br>
- [Huawei Cloud Terraform Template](https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/building-a-newapi-llm-gateway/building-a-newapi-llm-gateway.tf.json) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Related Commands](references/related-commands.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files] <br>
**Output Format:** [Markdown guidance with bash commands, JSON outputs, and Terraform-generated files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The workflow can create Terraform working files and terraform.auto.tfvars.json; supported script output masks sensitive values.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
