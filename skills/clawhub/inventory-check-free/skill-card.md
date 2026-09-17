## Description:

Checks inventory count tables for row arithmetic, totals, duplicates, and blanks, with each finding tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, warehouse, and operations staff use this skill to check inventory count tables during close, reconciliation, or stocktaking. It validates arithmetic relationships and flags duplicate or incomplete rows without producing accounting, audit, or tax advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release advertises a paid upgrade path that can fetch unpinned external code through an npx/SkillPay flow.

Mitigation: Do not run the paid upgrade or purchase commands unless the user has separately reviewed the external package, trusts the source, and personally confirms any wallet authorization or payment.

Risk: The free engine intentionally omits several inventory checks, so a clean result does not cover every inventory-control concern.

Mitigation: Treat results as coverage for the listed free checks only; review withheld and out-of-scope checks before relying on the output for accounting decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/inventory-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Source skill instructions](artifact/SKILL.md)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Terminal text or pretty-printed JSON with line-numbered findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Input is an inventory count table supplied as JSON or pasted text with recognizable headers.]

## Skill Version(s):

1.0.7 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
