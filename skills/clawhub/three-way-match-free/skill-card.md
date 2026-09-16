## Description:

This Chinese-language skill runs a local three-way match check across purchase orders, goods receipts, and invoices, reporting mismatched key fields, quantities, prices, amounts, duplicate invoice numbers, and leftover placeholders with source line references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounts-payable reviewers use this skill before payment to compare purchase order, goods receipt, and invoice text for basic three-way-match discrepancies. It is intended for local document checking and does not decide whether a payment should be approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release steers users or agents toward an external unpinned SkillPay install-and-purchase workflow.

Mitigation: Do not let an agent run the SkillPay npx install, install the paid package, or initiate a purchase without separate review, a pinned package and version, and explicit human confirmation.

Risk: The free checker only covers a limited set of three-way-match checks, so a clean result can miss issues outside that scope.

Mitigation: Treat findings as scoped review support and continue normal finance approval, invoice authenticity, supplier verification, tax, tolerance, and policy checks outside the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/three-way-match-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Purchase instructions referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON containing findings, severity levels, advice, and source evidence lines.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on local input files; reports insufficient input instead of producing a no-issue conclusion when materials are inadequate.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
