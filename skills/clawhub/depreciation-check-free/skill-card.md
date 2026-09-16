## Description:

Checks fixed-asset ledgers for depreciation arithmetic, totals, duplicate asset IDs, and blank placeholders, with findings tied to source line references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, accounting, cashier, and inventory staff use this skill during recurring close, payroll, reconciliation, or inventory checkpoints to verify fixed-asset depreciation tables before continuing downstream work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation and normal output steer users toward an unpinned external installer and purchase workflow.

Mitigation: Use the free checker locally; do not copy the upgrade prompt or run the npx @latest installer unless you independently trust SkillPay/Alipay and deliberately choose to start a purchase or install workflow.

Risk: The free edition withholds some depreciation checks, so users may overread the result as a complete accounting review.

Mitigation: Treat results as a local arithmetic and table-integrity check only, and review the listed checks not run before relying on the output.

Risk: The checker does not make accounting, audit, tax, impairment, useful-life, residual-rate, or physical-existence judgments.

Mitigation: Have qualified personnel review policy-dependent accounting conclusions and asset-existence questions outside this skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/depreciation-check-free)
- [Source skill instructions](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON check results with cited source lines.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally over a provided fixed-asset ledger; insufficient input reports missing materials instead of issuing a conclusion.]

## Skill Version(s):

1.0.8 (source: server evidence release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
