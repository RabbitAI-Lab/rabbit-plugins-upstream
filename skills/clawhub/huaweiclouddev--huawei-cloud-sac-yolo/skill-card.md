## Description:

Deploys a YOLO training platform on Huawei Cloud with GPU ECS infrastructure managed through Terraform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to provision, review, verify, and clean up a Huawei Cloud GPU environment for YOLO model training. It guides Terraform setup, variable review, deployment confirmation, security group configuration, and post-deploy validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can require broad Huawei Cloud administrative authority for provisioning and cleanup.

Mitigation: Use a least-privilege IAM user or custom policy where possible, review requested permissions before deployment, and pause on authorization failures until the user confirms permissions are granted.

Risk: Cloud access keys may be persisted in terraform.auto.tfvars.json during deployment preparation.

Mitigation: Keep terraform.auto.tfvars.json out of version control, restrict local file permissions, avoid long-lived AK/SK, and rotate or delete credentials after deployment.

Risk: Terraform apply or destroy can create, change, bill for, or remove cloud resources.

Mitigation: Require a reviewed terraform plan and explicit user confirmation before apply or destroy.

Risk: The YOLO UI requires an ingress rule on TCP port 8001 and could be exposed too broadly.

Mitigation: Use a restricted CIDR such as the user's own IP and avoid opening the rule to all addresses.

Risk: The workflow downloads a Terraform template from a remote URL.

Mitigation: Verify the Terraform download and review the plan before applying the downloaded template.

## Reference(s):

- [Huawei Cloud YOLO solution page](https://www.huaweicloud.com/solution/implementations/quickly-build-a-yolo-training-platform.html)
- [Huawei Cloud YOLO IAM policy reference](https://support.huaweicloud.com/yolo-aislt/yolo_04.html)
- [Terraform template download](https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/quickly-build-a-yolo-training-platform/quickly-build-a-yolo-training-platform.tf)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Related Commands](references/related-commands.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Terraform workflow guidance and expects JSON outputs from helper scripts and terraform output -json.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
