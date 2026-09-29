## Description:

Automates provisioning and management of AWS, Google Cloud Platform, and Azure infrastructure using infrastructure-as-code workflows with Terraform, Ansible, and CloudFormation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshine-del-ux](https://clawhub.ai/user/sunshine-del-ux)

### License/Terms of Use:

MIT

## Use Case:

Developers, DevOps engineers, and platform teams use this skill for cloud infrastructure automation guidance across AWS, Google Cloud Platform, and Azure. It helps agents draft infrastructure-as-code workflows, command examples, and configuration guidance for provisioning, configuration management, deployment pipelines, and common cloud templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production infrastructure commands could create, modify, or destroy cloud resources without adequate safeguards.

Mitigation: Require plans or dry runs, explicit human confirmation, state backups, target environment verification, and least-privilege cloud credentials before executing apply or destroy operations.

Risk: Sparse guidance may omit provider-specific safety checks for AWS, Google Cloud Platform, Azure, Terraform, Ansible, or CloudFormation workflows.

Mitigation: Have a qualified operator review generated commands and configurations against provider documentation, organization policy, and the intended environment before use.

## Reference(s):

- [Cloud Infra Automation on ClawHub](https://clawhub.ai/sunshine-del-ux/skills/cloud-infra-automation)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include infrastructure apply or destroy command examples; production use should require plan review, explicit confirmation, state backups, environment checks, and least-privilege cloud credentials.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
