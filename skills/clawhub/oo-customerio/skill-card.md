## Description:

Customer.io helps agents read, create, update, and delete Customer.io data through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to manage Customer.io profiles and events through an OOMOL-connected Customer.io account. It supports customer identification and updates, event tracking, suppression and unsuppression, customer merges, and customer deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, suppress, unsuppress, merge, or delete Customer.io customer data.

Mitigation: Require explicit user approval for every state-changing action and confirm the exact payload and expected effect before execution.

Risk: The security review reports that the confirmation boundary for customer data changes may be insufficient.

Mitigation: Review before installing and use a sandbox or least-privileged Customer.io connection for testing and routine operation.

Risk: The setup instructions include pipe-to-shell installer commands.

Mitigation: Avoid the pipe-to-shell installer path unless the OOMOL CLI installer source and integrity have been independently verified.

## Reference(s):

- [Customer.io homepage](https://customer.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-customerio)

## Skill Output:

**Output Type(s):** [shell commands, json, guidance, configuration]

**Output Format:** [Markdown guidance with shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands operate through the OOMOL-connected Customer.io connector and may require user confirmation for state-changing actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
