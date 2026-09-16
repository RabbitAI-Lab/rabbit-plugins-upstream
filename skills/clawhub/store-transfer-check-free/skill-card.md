## Description:

门店调拨与库存核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and store operations staff use this skill during month-end close, reconciliation, or stock checks to verify chain-store transfer and inventory tables. It recalculates row arithmetic, total rows, duplicate transfer numbers, blank placeholders, and selected negative quantities, then reports findings with source-line evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a paid-upgrade prompt that asks users to install unpinned payment tooling and initiate a purchase flow.

Mitigation: Use the free local checker without running the payment installer; only start any purchase workflow after independently verifying the source and explicitly approving each install and payment step.

Risk: The free checker omits several inventory checks, including in-transit bounds, negative ending inventory, and cross-store transfer variance checks.

Mitigation: Treat results as limited to the listed free checks and review the withheld and out-of-scope checks before relying on the output for operational decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/store-transfer-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Paid upgrade purchase instructions referenced by the skill](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf referenced by the skill](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, category, source line, message, executed checks, withheld checks, local-execution status, and network-use status.]

## Skill Version(s):

1.0.4 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
