## Description:

Provides a free local reconciliation check for restaurant daily sales reports, recomputing receivables, paid-in totals, total rows, duplicate rows, blanks, and negative amounts with source-row citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance staff, cashiers, and restaurant operators use this skill to reconcile restaurant daily sales submissions before closing, bookkeeping, or handoff. It checks row-level arithmetic, total-row consistency, duplicate business-day entries, missing placeholders, and negative values, while clearly listing checks that the free edition does not perform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill steers users from the local checker into an unpinned external installer and purchase flow.

Mitigation: Do not copy the upgrade prompt or run the npx installer unless the user intentionally wants the paid product, trusts the SkillPay workflow, and has verified the exact package and version.

Risk: The free edition withholds several reconciliation checks, so absence of findings is not evidence that withheld checks passed.

Mitigation: Review the listed included and withheld checks before relying on results, and treat omitted checks as not executed.

Risk: The checker and operational guidance are primarily Chinese-language, which can reduce reviewer confidence for teams that cannot review Chinese accounting terminology.

Mitigation: Use the skill only when reviewers can understand the Chinese-language input format, findings, withheld checks, and payment-flow warnings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/restaurant-daily-sales-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)
- [Optional paid-version purchase information](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay installer guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable console text or JSON report with cited reconciliation findings and withheld-check disclosure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard libraries; material-insufficient inputs return missing requirements instead of a pass/fail conclusion.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
