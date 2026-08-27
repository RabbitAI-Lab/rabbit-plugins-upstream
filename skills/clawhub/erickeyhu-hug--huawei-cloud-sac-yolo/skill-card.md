## Description:

Deploys a YOLO training platform on Huawei Cloud GPU ECS with Terraform for building or managing YOLO GPU training environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to prepare, deploy, verify, and clean up a GPU-backed Huawei Cloud YOLO training platform using Terraform and helper scripts.

### Deployment Geography for Use:

Huawei Cloud cn-north-4 region

## Known Risks and Mitigations:

Risk: The skill can guide real Huawei Cloud infrastructure creation and charges.

Mitigation: Use a test account or tightly scoped IAM user and review Terraform plans, resource scope, and estimated cost before any apply operation.

Risk: Cloud AK/SK credentials may be persisted locally in terraform.auto.tfvars.json.

Mitigation: Do not share credentials in chat, keep terraform.auto.tfvars.json out of version control, and rotate any AK/SK written to disk.

Risk: Deployment and cleanup require broad cloud permissions and can change or destroy infrastructure.

Mitigation: Require explicit user confirmation before terraform apply or destroy and prefer least-privilege IAM policies where possible.

Risk: The deployed YOLO UI and SSH endpoint can be exposed over public networking if access rules are too broad.

Mitigation: Restrict SSH and TCP port 8001 ingress to the user's IP or VPN and avoid opening access to all addresses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-sac-yolo)
- [Huawei Cloud YOLO solution page](https://www.huaweicloud.com/solution/implementations/quickly-build-a-yolo-training-platform.html)
- [Huawei Cloud YOLO IAM policy reference](https://support.huaweicloud.com/yolo-aislt/yolo_04.html)
- [Terraform template source](https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/quickly-build-a-yolo-training-platform/quickly-build-a-yolo-training-platform.tf)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Related Commands](references/related-commands.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, code]

**Output Format:** [Markdown guidance with inline shell commands and JSON script outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides Terraform workflows, writes local Terraform variable files, and expects user review before apply or destroy operations.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
