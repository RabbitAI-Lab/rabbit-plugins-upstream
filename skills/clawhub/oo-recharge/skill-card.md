## Description:

Recharge (getrecharge.com). Use this skill for ANY Recharge request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to read Recharge store data through an OOMOL-connected account. It retrieves individual charges, customers, orders, products, and subscriptions, and lists those resources with pagination and common filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OOMOL intermediates Recharge data access for this skill.

Mitigation: Install and use the skill only when that intermediary access model is acceptable for the target Recharge account and data.

Risk: Fallback setup includes pipe-to-shell CLI installation commands.

Mitigation: Review OOMOL's official installation guide or install the oo CLI through a trusted method before running setup commands.

Risk: The connector may expose state-changing actions outside the listed read-oriented workflow.

Mitigation: Keep use to the documented read actions unless the user explicitly approves any state-changing connector action and payload.

## Reference(s):

- [ClawHub Recharge Skill](https://clawhub.ai/oomol/skills/oo-recharge)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Recharge Homepage](https://getrecharge.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
