## Description:

将一份中国 A 股审计报告整理为逐项引用原文、锚点和来源的审计意见登记稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要核对中国 A 股审计报告的研究人员、分析师和审阅者，将单份报告整理为可回查的意见类型、意见基础、关键审计事项及其他相关段落。该登记稿不用于财报点评或投资判断。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: ClawScan marks the release suspicious because optional catalog access conflicts with the advertised offline workflow; its guidance also reports local usage markers, and the scan was partial.

Mitigation: Review when catalog access occurs before enabling that path. For a user-supplied, offline workflow, leave CUE_API_KEY unset; check for and remove ~/.cue-usage markers if they are not wanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huhoo/skills/cue-cn-audit-opinion-cn)
- [Publisher profile: huhoo](https://clawhub.ai/user/huhoo)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Six-section Markdown audit-opinion register with verbatim quotations, report anchors, source links, and retrieval dates; an unfilled draft outline may be produced when report text is unavailable.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers one audit report at a time; recorded wording is quoted from the report and missing material is identified for review.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
