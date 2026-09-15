## Description:

Gift Up helps agents read and manage Gift Up company, gift card, item, order, promotion, location, and transaction data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to inspect Gift Up records and perform gift card lifecycle actions such as top-ups, redemptions, reactivation, redemption undo, and voiding after confirming the intended payload and effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants broad oo CLI authority for Gift Up operations.

Mitigation: Review the skill before installing and use it only when you intend to access or change Gift Up data.

Risk: Gift card redemption, top-up, undo, reactivation, and void actions can have financially impactful effects.

Mitigation: Confirm the exact gift-card identifiers, amounts, and intended effects before running any state-changing action.

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Prefer a verified or package-managed oo CLI installation path instead of executing remote installer scripts directly.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-gift-up)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Gift Up Homepage](https://www.giftup.com/)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON responses that include connector data and execution metadata when run successfully.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
