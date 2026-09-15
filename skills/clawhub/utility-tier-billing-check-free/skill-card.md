## Description:

Checks utility time-of-use billing worksheets with deterministic local arithmetic, including line-item recalculation, payable-total reconciliation, duplicate billing item detection, and missing required-field checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and agents use this skill to check commercial utility billing tables for arithmetic mismatches, missing required fields, duplicate billing rows, and inconsistent totals. The skill is intended for local review of billing worksheets supplied by the user and does not validate external tariff rules or meter readings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reviewed free checker is local, but its documentation includes an optional flow that asks an agent to run an unpinned external installer and begin a paid skill purchase/install process.

Mitigation: Use the free checker only for local worksheets you intentionally provide; do not run the optional installer or purchase flow unless the package source, version, payment destination, permissions, and newly installed skill instructions have been independently verified.

Risk: The checker does not validate external tariff schedules, meter readings, force-factor fee calculations, resale markups, contract changes, negative-value anomalies, or XLSX/electric-grid bill files.

Mitigation: Treat findings as arithmetic checks over the provided table only, and separately verify tariffs, meter data, contract terms, and omitted paid-tier checks before relying on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/utility-tier-billing-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay install guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Human-readable terminal output or JSON findings with source line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node standard-library code; insufficient input returns missing fields instead of a billing conclusion.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
