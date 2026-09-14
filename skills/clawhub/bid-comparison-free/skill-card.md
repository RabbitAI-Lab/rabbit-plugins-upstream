## Description:

把多家投标人的报价明细逐项摆在一起对齐，生成逐项对照、缺项与多项提示，以及各家合价合计排序。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, bid-review, and evaluation-support users can use this skill to mechanically align multiple bidders' quotation items, see missing or extra items, and compare total quoted amounts. It is an aid for review and does not decide award outcomes, identify collusion, or provide legal conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat mechanical comparison output as a procurement, legal, or winner-selection decision.

Mitigation: Use the output as review support only and require human procurement or evaluation review before taking action.

Risk: The free version omits checks such as arithmetic verification, quantity consistency, price-limit comparison, outlier detection, and unbalanced-bid analysis.

Mitigation: Review the listed withheld checks and run separate checks when those issues matter for the bid review.

Risk: Item-name normalization can align similar labels incorrectly or miss matches when bidder descriptions differ materially.

Mitigation: Inspect item-level matches, missing-item findings, and source bid records before relying on the comparison.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chenqg618/skills/bid-comparison-free)
- [Publisher Profile](https://clawhub.ai/user/chenqg618)
- [Free Web Version](https://www.tokendidi.cn/check)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON comparison results with item tables, missing-item findings, totals, rankings, and explanatory guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally over user-provided bid data; results are mechanical comparison aids and should be reviewed before procurement decisions.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
