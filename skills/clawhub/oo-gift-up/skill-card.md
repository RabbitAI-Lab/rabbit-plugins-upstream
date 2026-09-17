## Description:

Operates Gift Up through an OOMOL-connected account using the oo CLI to read account data and run gift card, order, item, location, promotion, and transaction actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and developers managing Gift Up accounts use this skill to inspect live action schemas, read account data, and run confirmed gift card or order operations through the OOMOL oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Gift card mutations can change balances, redemption state, or card availability.

Mitigation: Confirm the exact gift card, action, amount or units, and expected effect with the user before running top-up, redemption, undo, reactivation, or void actions.

Risk: The skill includes remote installer pipe commands for the oo CLI.

Mitigation: Avoid running those installer commands unless the installer source and integrity have been independently verified; prefer reviewed installation procedures.

Risk: The skill can operate a connected Gift Up account through OOMOL-mediated access.

Mitigation: Install and use it only where OOMOL-mediated account access is acceptable, and verify the active account and connection before state-changing operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-gift-up)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Gift Up Homepage](https://www.giftup.com/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with inline shell commands, setup guidance, and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, OOMOL sign-in, and a connected Gift Up account before actions can run.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
