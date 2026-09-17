## Description:

A free local checker for lesson-hour redemption tables that verifies row arithmetic, totals, duplicates, and missing values, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and operations staff use this skill during monthly settlement or reconciliation to check lesson-hour ledgers before downstream accounting or customer follow-up. It is intended for local review of provided table text, not for legal, tax, attendance, refund, or pricing-policy decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free checker points users toward an external unpinned install and paid purchase workflow that is outside this reviewed package.

Mitigation: Use the package only for the free local checker unless the user separately reviews and trusts SkillPay, the Alipay package, and the merchant/product; require explicit user confirmation for wallet authorization or payment.

Risk: The free package does not perform several lesson-hour checks reserved for the paid edition, so a clean result may still miss those categories.

Mitigation: Treat results as limited to the executed free checks and manually review omitted categories before making settlement, refund, or customer-facing decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/lesson-hour-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Console text or JSON result objects with source-line findings and missing-input guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a local Node.js runtime and user-provided lesson-hour table text; the free version omits the checks listed as outside this package.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
