## Description:

CodeRabbit (coderabbit.ai). Use this skill for ANY CodeRabbit request -- reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to manage CodeRabbit organizations through OOMOL's oo CLI, including users, roles, seats, audit logs, and review metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bulk role or seat actions can change CodeRabbit account access.

Mitigation: Require explicit user confirmation for change_roles and manage_seats with the exact payload and expected effect before execution.

Risk: Role deletion can remove custom access configuration.

Mitigation: Get explicit approval for delete_role after verifying the target role and that it is not assigned to users.

Risk: Remote oo CLI installer commands introduce supply-chain exposure if run without review.

Mitigation: Only run installer commands when oo is missing and the user confirms the install source or path.

## Reference(s):

- [CodeRabbit homepage](https://www.coderabbit.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before command execution; state-changing actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
