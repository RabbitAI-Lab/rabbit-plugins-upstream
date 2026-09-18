## Description:

发票作废与红冲台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashiering, and tax operations teams use this skill during monthly close, reconciliation, or ledger review to check invoice void and reversal ledgers for arithmetic mismatches, duplicate invoice numbers, missing required fields, negative amounts, and total-row inconsistencies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary says the free checker output and documentation steer users toward an agent-run paid install and purchase workflow.

Mitigation: Do not let an agent run SkillPay, npx, install, purchase, or wallet-related commands unless the package, version, merchant, product, and payment flow are separately verified in an isolated, explicit workflow.

Risk: The skill checks ledger arithmetic and internal consistency but does not decide whether an invoice should legally be voided or reversed.

Mitigation: Treat findings as reconciliation support and confirm tax treatment, filing decisions, and authority-specific requirements with the appropriate finance or tax reviewer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/tax-invoice-void-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)
- [Purchase and installation information for the optional paid version](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON containing executed checks, findings, summary, omitted checks, and input guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; insufficient input returns missing-field guidance instead of a ledger conclusion.]

## Skill Version(s):

1.0.5 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
