## Description:

农产品收购发票与进项抵扣核对表逐项核对，复算表内金额、核对合计、检查重复凭证和空缺负值，并在结论中引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and accounting staff use this skill during monthly closing, reconciliation, or inventory checks to review agricultural purchase invoice VAT deduction tables before continuing downstream tax or bookkeeping work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence reports a suspicious paid-upgrade flow that installs unpinned external code and can initiate a purchase.

Mitigation: Use only the bundled free local checker unless the package, publisher, payment flow, and resulting installation are separately reviewed and trusted; require the user to confirm any wallet or payment step.

Risk: The checker processes invoice data locally through a Node script, which may involve sensitive business or tax records.

Mitigation: Run it only in an environment approved for the source documents and review the generated findings before using them for tax, accounting, or compliance decisions.

Risk: The free version omits several checks and does not determine the correct tax policy treatment for rates, add-on deductions, or invoice compliance.

Mitigation: Treat results as table arithmetic and reconciliation support only; obtain appropriate tax review before relying on conclusions outside the documented free checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/agri-purchase-invoice-deduction-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Purchase and installation information](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [analysis, markdown, json, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON result with cited findings, executed checks, withheld checks, and status information.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; returns insufficient-input status instead of a finding when required table data is missing.]

## Skill Version(s):

1.0.3 (source: server-resolved release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
