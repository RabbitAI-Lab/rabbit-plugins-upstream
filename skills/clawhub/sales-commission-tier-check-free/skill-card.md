## Description:

A free local checker that audits sales commission reconciliation tables for row arithmetic, totals, duplicate rows, blanks, and negative amounts with source-line evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and sales-operations teams use this skill during monthly closing or commission payout review to re-check sales commission reconciliation tables. It helps compare table arithmetic, totals, duplicate rows, blanks, and negative values before relying on the worksheet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free checker steers users toward an external install-and-purchase flow for the paid edition that uses unpinned remote code.

Mitigation: Install only after separately reviewing the SkillPay onboarding package, exact package version, merchant, product, and payment step; require the user to confirm wallet authorization or payment.

Risk: The free edition intentionally omits several paid-edition checks, so a clean result is not a complete commission-policy review.

Mitigation: Review the listed withheld checks and do not treat absence of findings as coverage beyond the executed free checks.

Risk: The checker depends on the input table having recognizable headers and sufficient rows; insufficient material can prevent a conclusion.

Mitigation: Provide the full sales commission reconciliation table with headers, and use the insufficient-input report to supply missing fields before relying on the result.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/sales-commission-tier-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [AI 核对工具铺](https://skillpay.alipay.com/public/tokendidi)
- [Full edition purchase instructions](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [text, json, guidance, shell commands]

**Output Format:** [Plain text or JSON audit results, with Markdown instructions and inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports executed checks, withheld checks, local execution status, findings, insufficient-input status, and source-line evidence when available.]

## Skill Version(s):

1.0.3 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
