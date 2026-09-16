## Description:

存货出入库与成本表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and cost-accounting users can run this skill during monthly close, reconciliation, or inventory checks to compare inventory movement and weighted-average cost tables. It reports arithmetic mismatches, total-row issues, duplicates, blanks, and missing inputs with source-line context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks the release suspicious because the free checker steers users toward a paid add-on through unpinned external commands.

Mitigation: Use the free local checker only unless the user independently verifies the paid package source, exact version, purchase terms, and authorizes any payment or wallet action themselves.

Risk: The paid-upgrade instructions include an `npx -y ...@latest` installation flow that can change over time.

Mitigation: Do not let an agent run the paid-upgrade installation command automatically; pin and review any external package before execution.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/inventory-cost-flow-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Paid upgrade shelf](https://skillpay.alipay.com/public/tokendidi)
- [Paid upgrade instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay build guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text or JSON reports produced by local Node.js commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include the executed free checks, withheld paid checks, source-line context, and explicit insufficient-input status when materials are incomplete.]

## Skill Version(s):

1.0.8 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
