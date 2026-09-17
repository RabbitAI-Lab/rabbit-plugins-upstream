## Description:

车辆保险与保费摊销核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations employees use this skill during monthly close, reconciliation, or inventory checks to review vehicle insurance premium amortization tables. It recalculates row-level amortization, balance roll-forwards, totals, duplicate rows, blank placeholders, and negative amounts within the free checker scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes an upgrade prompt with an unpinned external installer and paid purchase flow.

Mitigation: Independently verify the vendor, package, product, and payment flow before running any installer or purchase command, and require fresh user confirmation for wallet authorization or payment.

Risk: The free checker intentionally omits several checks that are reserved for the paid version.

Mitigation: Review the reported withheld checks before relying on the result, and treat the output as limited to the free checker scope.

Risk: The checker does not make accounting, insurance-contract, tax, or refund-policy judgments.

Mitigation: Use the output for table arithmetic and consistency review only, and refer policy or accounting treatment questions to qualified reviewers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/vehicle-insurance-amortization-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)
- [Upgrade purchase instructions referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay build guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Plain text or JSON audit findings with source-linked rows and scope notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; reports withheld checks and does not produce conclusions when input material is insufficient.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
