## Description: <br>
Deploy YOLO training platform on Huawei Cloud with GPU ECS via Terraform. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to provision a Huawei Cloud GPU ECS environment for YOLO model training, review Terraform variables, verify deployment outputs, and clean up resources. <br>

### Deployment Geography for Use: <br>
Global, with deployment instructions currently scoped to Huawei Cloud region cn-north-4. <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uses real Huawei Cloud AK/SK credentials and writes deployment variables to terraform.auto.tfvars.json. <br>
Mitigation: Use a dedicated low-privilege IAM identity where possible, do not share credentials in chat, keep terraform.auto.tfvars.json out of version control, and remove it after deployment. <br>
Risk: Some deployment paths can require broad administrator-level cloud permissions or an all-resources RFS agency. <br>
Mitigation: Prefer the narrowest IAM policy that supports the deployment and grant Tenant Administrator or all-resource access only after explicit review. <br>
Risk: SSH and the YOLO web UI can expose the deployed ECS instance if ingress rules are too broad. <br>
Mitigation: Restrict SSH and TCP port 8001 ingress to the user's IP address or another approved CIDR. <br>
Risk: Terraform apply and destroy operations create or remove billable cloud infrastructure. <br>
Mitigation: Review pricing, variables, and terraform plan output before applying changes, and require explicit confirmation before apply or destroy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-sac-yolo) <br>
- [Huawei Cloud YOLO solution](https://www.huaweicloud.com/solution/implementations/quickly-build-a-yolo-training-platform.html) <br>
- [Huawei Cloud YOLO IAM requirements](https://support.huaweicloud.com/yolo-aislt/yolo_04.html) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Related Commands](references/related-commands.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands, JSON snippets, Terraform configuration steps, and verification commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces deployment and cleanup guidance for Huawei Cloud resources; modification operations require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
