## Description:

将一份境内债券募集说明书或发行方案整理为八项逐字条款卡，每项附原文和来源锚，缺项明确标记，估值与投资判断留待人工。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

债券研究人员和发行文件审阅者可用它从单只境内债券的募集说明书、发行方案或发行公告中提取八类条款，并保留逐字引文与来源定位。它不提供估值、收益率测算或投资建议。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Optional online parsing may expose confidential bond documents to an external processor whose handling and retention were not verified.

Mitigation: Use public or approved documents online; keep confidential material local unless the processor's handling and retention are acceptable.

Risk: An extracted clause may be incomplete or misread.

Mitigation: Check quotations and source anchors against the original prospectus, and leave missing or judgment-based items explicitly unresolved.

## Reference(s):

- [债券文件层级与三要素记法](references/bond-layers.md)
- [ClawHub release](https://clawhub.ai/huhoo/skills/cue-bond-terms-cn)
- [Data access configuration](https://cuecue.cn/hub/mcp)
- [Document parsing configuration](https://cuecue.cn/hub/omni-reader)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown bond card with verbatim quotations and source anchors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Eight fixed items; missing information is explicitly marked; valuation, yield calculations, ratings judgments, and investment recommendations remain for human review.]

## Skill Version(s):

0.1.1 (source: frontmatter, changelog released 2026-11-04, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
