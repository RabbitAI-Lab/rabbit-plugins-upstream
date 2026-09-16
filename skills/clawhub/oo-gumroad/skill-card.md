## Description:

Gumroad (gumroad.com). Use this skill for ANY Gumroad request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Gumroad account data and perform account operations through an OOMOL-connected Gumroad connector, including product, sale, subscriber, shipment, refund, and receipt workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a live Gumroad account, including shipment updates, refunds, and receipt resends.

Mitigation: Require explicit confirmation of the sale, amount, recipient, payload, and expected effect before any refund, shipment update, or receipt resend.

Risk: The security summary states that refund and receipt-resend actions are under-labeled as safe.

Mitigation: Treat refund and receipt-resend actions as state-changing operations even when the artifact does not tag them as write or destructive.

Risk: The security guidance flags remote installer commands as risky when run blindly.

Mitigation: Review the official installer first or use a safer pinned installation path when available.

## Reference(s):

- [ClawHub Gumroad Skill](https://clawhub.ai/oomol/skills/oo-gumroad)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Gumroad Homepage](https://gumroad.com)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions and returns Gumroad connector responses as JSON when commands are executed.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
