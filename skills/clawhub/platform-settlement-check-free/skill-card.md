## Description:

平台结算单逐项核对（逐行算术、合计勾稽、重复与空缺检测），每条结论引用原文行号，本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations users use this skill during monthly settlement, reconciliation, and inventory-close workflows to check ecommerce platform settlement sheets for arithmetic mismatches, total-row errors, duplicate order IDs, and missing or placeholder values.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional paid-upgrade path asks the agent to run an unpinned remote installer and continue into a purchase workflow.

Mitigation: Use the free local checker without running the upgrade installer unless a human independently verifies the package, version, source, filesystem changes, and payment terms.

Risk: The paid upgrade may involve wallet authorization or payment confirmation.

Mitigation: Require the user to personally approve any wallet or payment step; the agent should only present official links or QR codes and should not confirm payment on the user's behalf.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/platform-settlement-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)
- [Optional full-version purchase instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON settlement-check results with source line references and remediation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, category, line number, quoted row evidence, advice, executed checks, withheld checks, and insufficient-input status when required.]

## Skill Version(s):

1.0.7 (source: evidence.json release.version and artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
