## Description:

Terraform and OpenTofu configuration, modules, testing, state management, and HCL review for agents working with Terraform, OpenTofu, HCL, tfvars, tftest, state migration, or IaC patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill for Terraform/OpenTofu module authoring, HCL review, testing, state-management guidance, and safe IaC workflow checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Terraform or OpenTofu changes can alter live infrastructure, create cost, or destroy resources if applied without review.

Mitigation: Review generated HCL, plans, and module changes before applying them, and require explicit user confirmation before any real apply operation.

Risk: State operations such as import, force-unlock, refresh-only apply, or replace can affect existing infrastructure state.

Mitigation: Treat state-changing commands as user-directed work, confirm the target workspace and resource address, and verify no competing operation is running before lock or state changes.

Risk: Terraform state, plan files, and provider configuration can contain sensitive values.

Mitigation: Keep state remote and encrypted, do not commit state or plan files, and use role assumption, OIDC, or secrets managers rather than hardcoded credentials.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline HCL and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance should be reviewed before applying infrastructure changes.]

## Skill Version(s):

4.5.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
