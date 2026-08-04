## Description: <br>
Deploys a Huawei Cloud YOLO training platform with GPU ECS infrastructure using Terraform, Python helper scripts, and Playwright-based solution metadata extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to prepare, review, deploy, verify, and clean up a Huawei Cloud GPU environment for YOLO model training. <br>

### Deployment Geography for Use: <br>
Global, with infrastructure deployment constrained to Huawei Cloud cn-north-4 by the skill documentation. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can require broad Huawei Cloud deployment authority. <br>
Mitigation: Use a dedicated Huawei Cloud IAM user and project, grant only the permissions needed for the deployment, and avoid Tenant Administrator unless Huawei explicitly requires it. <br>
Risk: Downloaded Terraform templates may create, modify, or delete billable cloud resources. <br>
Mitigation: Verify the Terraform download separately, review the downloaded files, run terraform plan, and require explicit user confirmation before terraform apply or terraform destroy. <br>
Risk: Huawei Cloud AK/SK credentials and terraform.auto.tfvars.json are sensitive. <br>
Mitigation: Keep credentials out of chat and version control, prefer environment variables or local tfvars entry, and confirm sensitive values before deployment. <br>
Risk: SSH or the YOLO web UI could be exposed too broadly. <br>
Mitigation: Restrict SSH and TCP port 8001 ingress to a trusted CIDR and verify security group rules before accepting the deployment. <br>
Risk: Temporary agencies or deployed resources may remain after testing. <br>
Mitigation: Run the cleanup workflow, confirm terraform destroy succeeds, and remove temporary agencies or resources that are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-sac-yolo) <br>
- [Huawei Cloud YOLO solution](https://www.huaweicloud.com/solution/implementations/quickly-build-a-yolo-training-platform.html) <br>
- [Huawei Cloud YOLO IAM reference](https://support.huaweicloud.com/yolo-aislt/yolo_04.html) <br>
- [Huawei Cloud Terraform template](https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/quickly-build-a-yolo-training-platform/quickly-build-a-yolo-training-platform.tf) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Related Commands](references/related-commands.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Terraform workflow guidance and expects human confirmation before apply or destroy operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
