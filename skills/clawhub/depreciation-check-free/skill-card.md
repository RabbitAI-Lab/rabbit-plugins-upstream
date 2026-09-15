## Description:

Locally checks fixed asset ledger depreciation arithmetic, totals, duplicate asset identifiers, and missing or placeholder values, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, warehouse, and operations staff use this skill during monthly close, payroll, reconciliation, or inventory checkpoints to recheck fixed asset depreciation ledgers. It helps identify arithmetic mismatches, total-row inconsistencies, duplicate asset identifiers, and blank or placeholder fields without sending materials off the local machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports a suspicious release because the artifact includes actionable instructions for an unpinned external installer and a paid product installation flow.

Mitigation: Use the free local checker only when intended; do not allow an agent to run the unpinned installer or continue a paid installation flow unless the Alipay SkillPay tooling and package version are separately trusted and the user explicitly approves payment.

Risk: The checker does not cover all fixed-asset accounting judgments or the paid full-version checks listed by the artifact.

Mitigation: Treat results as arithmetic and ledger consistency checks only, and separately review depreciation policy, residual value policy, impairment, capitalization, physical existence, and any withheld paid checks.

Risk: Input that lacks a recognizable fixed asset ledger header or asset rows can prevent checks from running.

Mitigation: Provide a ledger that includes the header row and asset detail rows, preferably copied from Excel as tab-separated text or wrapped in a JSON text field.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/depreciation-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay public shelf referenced by the artifact](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay installation guide referenced by the artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON from a local Node.js checker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient inputs return missing-material guidance instead of a clean result.]

## Skill Version(s):

1.0.4 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
