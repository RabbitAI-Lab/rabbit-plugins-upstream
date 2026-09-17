## Description:

委外加工结算核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Manufacturing finance, cashier, and reconciliation staff use this skill during monthly close, account reconciliation, and inventory checks to recalculate outsourced processing settlement tables. It checks row arithmetic, totals, duplicate rows, blanks, placeholders, and negative quantities or amounts while citing source rows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is flagged suspicious because it repeatedly redirects users toward an external paid install and purchase flow.

Mitigation: Treat the paid-upgrade section separately from the free checker; verify purchase links and wallet prompts independently before taking any payment action.

Risk: The bundled upgrade prompt asks an assistant to install an unpinned npx package and proceed through a purchase workflow.

Mitigation: Do not paste the bundled authorization prompt to an assistant as-is, and do not run the unpinned npx command without independent verification.

Risk: The checker reads user-provided settlement table data from a local file.

Mitigation: Use it only with data you are comfortable processing locally and review outputs against source rows before relying on conclusions.

Risk: The free release omits checks for loss-rate limits, contract-price mismatches, returned quantity greater than issued quantity, stock mismatches, and zero processing quantity with fees.

Mitigation: Do not treat a clean free-check result as full settlement approval; separately review the omitted checks when they matter.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/outsourced-processing-fee-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Paid upgrade purchase instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay build guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON with cited reconciliation findings and local Node.js commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports insufficient input without conclusions; JSON mode includes executed free checks, withheld checks, and result details.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
