## Description:

Use this skill to search and read Maxio Advanced Billing data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve Maxio Advanced Billing customers, products, and subscriptions through an OOMOL-connected oo CLI workflow. It supports read-oriented lookup, listing, filtering, pagination, and live schema inspection before running connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local oo CLI installation guidance includes pipe-to-shell commands.

Mitigation: Install the oo CLI only from a trusted source and version, and prefer verified release artifacts when available.

Risk: Dynamic connector execution could affect billing-account data if actions beyond the listed read-only operations are authorized.

Mitigation: Use the skill for the listed get and list Maxio actions by default, inspect the live action schema, and require explicit user authorization before any billing-account change.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-chargify)
- [Maxio Advanced Billing](https://www.maxio.com/product/advanced-billing)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
