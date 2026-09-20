## Description:

Locally checks Chinese social-insurance and housing-fund declaration details for the free subset of row-level arithmetic, total cross-checks, duplicate entries, and blank placeholders, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, payroll, cashier, inventory, and operations staff use this skill during monthly closing, payroll, reconciliation, or stocktaking workflows to check copied social-insurance declaration tables for arithmetic consistency, total rollups, duplicates, and missing placeholders. It does not provide legal, tax, policy, eligibility, base-limit, or ratio-compliance validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the free checker output as legal, tax, policy, eligibility, base-limit, or ratio-compliance validation.

Mitigation: Present the output as arithmetic and table-quality checking only, and route legal, tax, policy, eligibility, base-limit, and ratio-compliance decisions to authoritative review.

Risk: A summary phrase may overstate that ratio checks were performed even though the free version withholds those checks.

Mitigation: Use the executed-check and withheld-check lists in the report, and do not describe withheld ratio or base-limit checks as completed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/social-insurance-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON report from a local Node.js checker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports executed checks, withheld checks, source-line findings, missing-input guidance, and explicit no-conclusion behavior when the supplied table is insufficient.]

## Skill Version(s):

1.0.49 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
