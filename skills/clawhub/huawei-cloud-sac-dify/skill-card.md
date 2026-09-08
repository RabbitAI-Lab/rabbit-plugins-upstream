## Description:

Deploys Dify, an open-source LLM app development platform, on Huawei Cloud ECS using Terraform and a Huawei Cloud Solution-as-Code template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to provision a Dify LLM application development platform on Huawei Cloud, review pricing and Terraform variables, verify deployment health, and clean up managed resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Huawei Cloud credentials can be exposed if AK/SK values are typed into chat, printed in clear text, committed, or left in terraform.auto.tfvars.json.

Mitigation: Use environment variables or a local tfvars file only, mask sensitive values during review, keep the tfvars file out of version control, restrict access to it, and delete it after successful destroy.

Risk: Terraform apply and destroy can create, modify, bill, or delete Huawei Cloud resources.

Mitigation: Require the user to review estimated price, Terraform variables, and terraform plan output, then obtain explicit confirmation before apply or destroy.

Risk: Overbroad or underconfigured cloud permissions can either expand blast radius or cause failed deployments.

Mitigation: Use least-privilege IAM users or an appropriate agency, compare failures against the documented IAM policy, and confirm with the user before retrying deployment actions.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Related Commands](references/related-commands.md)
- [Huawei Cloud Dify Solution Page](https://www.huaweicloud.com/solution/implementations/building-a-dify-llm-application-development-platform.html)
- [Huawei Cloud Dify Terraform Template](https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/flexus/dify-ecs.tf)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON-producing helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes Terraform variable review, masked sensitive values, deployment verification steps, and cleanup guidance.]

## Skill Version(s):

1.0.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
