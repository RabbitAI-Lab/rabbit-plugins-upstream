## Description:

SumUp (sumup.com). Use this skill for ANY SumUp request - reading, creating, updating, and deleting data. Whenever a task involves SumUp, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate SumUp through an OOMOL-connected account. It supports checkout, customer, and payment-instrument workflows through live schema inspection and oo CLI connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote script execution for installing the required oo CLI.

Mitigation: Prefer a verified, versioned oo CLI installation method and review installer source before execution.

Risk: Write and destructive SumUp actions can create, update, or deactivate payment and customer records.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running state-changing commands.

Risk: The skill may operate on real SumUp payment and customer data.

Mitigation: Review before installation in environments that manage production payment or customer data.

## Reference(s):

- [SumUp homepage](https://www.sumup.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub SumUp skill page](https://clawhub.ai/oomol/skills/oo-sumup)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live action schemas should be inspected before constructing JSON payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
