## Description:

运费月结单逐项核对（逐行算术、合计勾稽、重复与空缺检测），每条结论引用原文行号。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashiering, warehouse, and operations staff use this skill to check monthly freight statements for arithmetic errors, total-row mismatches, duplicate waybills, and blank or placeholder fields before settlement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation points users toward an unpinned external installer and paid purchase flow for an optional full version.

Mitigation: Review the SkillPay source and verify the vendor and product before running the installer or authorizing any wallet or payment action.

Risk: The checker runs a local Node script over freight statement text.

Mitigation: Run it only in an environment where local script execution is acceptable, and review the line-cited findings before using them for settlement decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/freight-reconciliation-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay product shelf](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay installation guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance plus command-line text or JSON from the local Node checker.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input reports missing material instead of making a conclusion.]

## Skill Version(s):

1.1.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
