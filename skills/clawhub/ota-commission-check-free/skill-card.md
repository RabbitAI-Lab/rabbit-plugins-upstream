## Description:

A free deterministic local checker for hotel OTA commission and net settlement tables that recalculates commissions, net settlements, totals, duplicate channels, and missing fields while citing source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Hotel, homestay, and finance operations users use this skill to review copied OTA channel settlement tables for arithmetic mismatches in commissions, net settlements, totals, duplicate channels, and missing fields before reconciliation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may misunderstand the data handling posture because some help text mentions anonymous usage statistics even though the security evidence reports no observed material leaving the machine.

Mitigation: Install only if comfortable running a local Node-based reconciliation helper on the settlement-table text provided, and review publisher wording around statistics before broad deployment.

Risk: A clean or passing result covers only the free arithmetic and table-quality checks, not withheld anomaly checks, contract compliance, tax treatment, or channel-specific settlement rules.

Mitigation: Use the output as a reconciliation aid for the listed checks and manually review withheld, out-of-scope, contractual, and tax-sensitive issues.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ota-commission-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable console text or JSON findings with source line numbers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are limited to the free checks declared by the bundled engine; insufficient input reports missing fields instead of drawing a conclusion.]

## Skill Version(s):

1.0.29 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
