## Description:

门店调拨与库存核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and store operations teams use this skill during close, reconciliation, or inventory review to validate chain-store transfer tables, recalculate row and total arithmetic, and identify duplicate or missing entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation around anonymous usage statistics is inconsistent with the inspected behavior.

Mitigation: Confirm the current release's network behavior before deployment and communicate the data-handling posture to users.

Risk: The free edition omits several inventory checks that may matter for full reconciliation.

Mitigation: Review the listed withheld and out-of-scope checks before relying on results for final inventory decisions.

Risk: The checker is Chinese-language and expects a recognizable transfer table with required columns.

Mitigation: Use the sample format and treat insufficient-input responses as no conclusion rather than a pass.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/store-transfer-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Human-readable Chinese console text or JSON result objects.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes executed checks, withheld checks, findings, missing-input notices, and source line references where available.]

## Skill Version(s):

1.0.48 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
