## Description:

Generates Terraform infrastructure-as-code guidance and code for multi-cloud resource orchestration, modular environments, remote state management, and CI/CD integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, infrastructure engineers, and operations teams use this skill to draft Terraform modules, backend configuration, environment layouts, CI/CD snippets, and deployment guidance for cloud infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Terraform can guide cloud-changing execution if a user runs terraform apply without review.

Mitigation: Review generated Terraform and terraform plan output before apply, and use least-privilege cloud credentials.

Risk: Secret values may be exposed if stored in terraform.tfvars, outputs, logs, or version control.

Mitigation: Do not rely on tfvars to hide secrets; use environment variables, OIDC, Vault, or a secret manager, mark sensitive variables and outputs with sensitive = true, and keep secret-bearing files out of version control.

Risk: The security evidence flags incorrect advice about hiding secrets in tfvars files.

Mitigation: Treat secret-handling guidance as requiring manual review and prefer platform secret managers or ephemeral credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/terraform-iac-architect)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with Terraform HCL, shell commands, directory layouts, tables, and deployment notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs require human review before applying infrastructure changes.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and changelog mention 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
