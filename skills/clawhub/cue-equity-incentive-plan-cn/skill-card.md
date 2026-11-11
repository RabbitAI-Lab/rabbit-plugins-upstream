## Description:

把一份 A 股股权激励计划草案或相关公告整理成八项带原句与来源锚的条款卡，并清楚标出缺失信息和需要人工判断的内容。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

面向阅读中国 A 股股权激励计划的投资者与研究人员，用于整理草案或公告中的八类条款，逐项保留原文与来源位置，并列出缺失项。它不提供参与建议、收益或稀释测算，也不核实名单。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Optional external attachment parsing may involve sending private plan documents to an external service.

Mitigation: For private documents, provide the text directly; before using attachment parsing, review retention terms and approve any nonpublic upload.

Risk: The optional API key could be exposed or sent to an unintended destination.

Mitigation: Keep the key out of chat and verify its destination before enabling the data service.

Risk: Extracted clause text may be incomplete or inaccurate.

Mitigation: Check quotations and extracted terms against the original plan document.

## Reference(s):

- [EIP clause reference](references/eip-terms.md)
- [ClawHub skill page](https://clawhub.ai/huhoo/skills/cue-equity-incentive-plan-cn)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown clause card with verbatim quotations, source anchors, missing-item notes, and human-review boundaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Eight clause items; missing information is marked 未检索到, and calculations and evaluative judgments remain [待人工].]

## Skill Version(s):

0.1.1 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
