## Description:

Operate Stripe through an OOMOL-connected account for customer, product, and price read, write, and delete actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect and manage Stripe customers, products, and prices through an already connected OOMOL account. Write and destructive actions require confirming the exact payload and effect before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change or delete Stripe customer, product, and price data.

Mitigation: Confirm every write or destructive action with the user, including the exact target, payload, and expected effect, before execution.

Risk: The skill includes remote oo CLI installer commands that were not independently verified by the security evidence.

Mitigation: Avoid running installer commands as written unless the oo CLI installer source and integrity have been independently verified.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-stripe)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Stripe](https://stripe.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run oo CLI connector actions that return JSON data; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
