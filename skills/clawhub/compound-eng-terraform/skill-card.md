## Description:

Guides agents on Terraform and OpenTofu configuration, modules, testing, state management, and HCL review for IaC tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill to author, review, test, and troubleshoot Terraform/OpenTofu modules and configurations while preserving state and controlling apply-mode risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apply-mode Terraform tests and state operations can create, modify, or replace real infrastructure and may incur cost.

Mitigation: Review Terraform plans, avoid apply-mode tests unless intended, and require explicit confirmation before state-changing commands.

Risk: Formatting and validation workflows may rewrite local Terraform files or depend on local tool availability.

Mitigation: Run formatting deliberately, inspect diffs after rewrites, and treat missing local tools as setup blockers rather than bypassing validation.

## Reference(s):

- [Native test patterns](references/native-test-patterns.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline HCL and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Terraform/OpenTofu validation, formatting, testing, and state-management commands; review commands before execution.]

## Skill Version(s):

4.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
