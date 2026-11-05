## Description:

把一份 A 股股权激励计划草案或相关公告整理为八项逐字条款卡，每项附原句与来源锚点，并标明缺失信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要阅读 A 股股权激励计划草案或公告的投资者与分析人员，把单份文件整理为八项逐字条款卡，并保留引文与来源定位。它用于条款提取和缺项标记，不给出参与建议、收益测算或名单核验。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: External parsing may transmit document content to a provider, creating privacy and retention concerns.

Mitigation: Use local processing of supplied text where suitable; before external parsing, confirm the document may be transmitted and check the provider's retention terms. Use public, approved, or redacted material.

Risk: Optional credentials and companion skills add trust and destination considerations.

Mitigation: Verify credential destinations and review companion skills and installer versions before enabling the external path.

Risk: The advertised safety checker can miss prohibited advice, so a passing result may not catch every unsafe statement.

Mitigation: Manually review the generated card and check quotations against the source; keep calculations, recommendations, and eligibility judgments for human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huhoo/skills/cue-equity-incentive-plan-cn)
- [Equity incentive terms reference](artifact/references/eip-terms.md)
- [Cue MCP configuration](https://cuecue.cn/hub/mcp)
- [Cue Omni Reader configuration](https://cuecue.cn/hub/omni-reader)
- [Cue API key information](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown eight-item clause card with verbatim quotations, source anchors, missing-item list, and human-review items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records one plan at a time; preserves source wording and numbers. Financial calculations, advice, eligibility judgments, and list verification remain for human review.]

## Skill Version(s):

0.1.0 (source: frontmatter, changelog dated 2026-11-04)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
