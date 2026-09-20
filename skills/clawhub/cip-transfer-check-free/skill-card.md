## Description:

Checks CIP-to-fixed-asset transfer ledgers for row-level arithmetic, total reconciliation, duplicate projects, blank or placeholder fields, and negative amounts, with findings tied to source rows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting staff use this skill during monthly close, reconciliation, or inventory checks to verify a CIP-to-fixed-asset transfer ledger for arithmetic consistency, total cross-checks, duplicate projects, blanks, placeholders, and negative amounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the free checker as a full accounting-control or audit review.

Mitigation: Use it only for the stated arithmetic and table-consistency checks, and independently review date order, accounting policy, ERP, and audit judgments.

Risk: The output disclaimer can imply date-order checks that the free version does not perform.

Mitigation: Review the reported checks_given and checks_withheld fields before relying on a result.

Risk: The skill runs a local Node script over accounting table text.

Mitigation: Install only if comfortable running local scripts and avoid providing unnecessary sensitive data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/cip-transfer-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON report from a local Node CLI, with cited findings and listed checks not run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns no conclusion when required ledger material is missing; free version reports the checks it performs and withholds.]

## Skill Version(s):

1.0.49 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
