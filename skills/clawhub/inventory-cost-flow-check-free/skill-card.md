## Description:

存货出入库与成本表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and inventory staff use this skill during monthly close, reconciliation, or stocktaking to check inventory cost flow tables. It reviews arithmetic consistency, weighted-average outbound cost, totals, duplicate inventory rows, blanks, and required table fields, and it reports when input is insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free checker appears self-contained, but the skill also includes paid-upgrade instructions that ask an agent to run an unpinned external installer and follow newly installed instructions.

Mitigation: Use the included free checker only for local inventory table review. Do not run the paid-upgrade npx command or paste the purchase prompt into an agent unless the package, version, SkillPay/Alipay workflow, and payment step are independently verified; keep payment confirmation manual.

Risk: The free version intentionally omits several inventory-cost checks from the paid full version.

Mitigation: Treat results as limited to the listed free checks and review the withheld-checks list before relying on the output for close, reconciliation, or stocktaking decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/inventory-cost-flow-check-free)
- [SkillPay product shelf for optional full version](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Plain text or JSON reports with line-level findings and source citations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports executed checks, withheld checks, insufficient-input status, and whether network use occurred.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
