## Description:

Checks stamp-duty taxable-base ledgers by recomputing row-level tax, checking totals, and flagging duplicate or missing fields, with each finding tied back to the source row.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill during month-end, reconciliation, inventory, or stamp-duty declaration preparation to check whether a provided stamp-duty taxable-base ledger is arithmetically consistent. It is scoped to the free local checks and does not decide taxability or the correct tax category for a contract.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional upgrade instructions may lead an agent to download unpinned code and begin a paid purchase or install flow.

Mitigation: Use the free local checker without the upgrade prompt unless the SkillPay source, package version, payment flow, and newly installed skill instructions have been independently verified in a constrained environment; require the user to personally confirm any wallet authorization or payment.

Risk: The free checker intentionally omits several checks and does not make taxability or tax-category determinations.

Mitigation: Review the reported checks_not_run and out-of-scope items before relying on the result, and route legal or tax-judgment questions to an appropriate tax professional.

Risk: Insufficient or malformed ledger input can prevent the checker from reaching a conclusion.

Mitigation: Provide the ledger with required headers and source rows, and treat insufficient-input responses as no conclusion rather than as a clean reconciliation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/stamp-duty-base-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay shelf mentioned by artifact](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [analysis, json, guidance, shell commands]

**Output Format:** [Human-readable console text or JSON containing scope, findings, summary, omitted checks, and guidance for insufficient input.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; no API key or network access is required for the bundled free checker.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
