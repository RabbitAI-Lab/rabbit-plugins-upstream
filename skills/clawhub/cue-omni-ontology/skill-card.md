## Description:

从用户指定的公开文档建立可追溯业务知识包，并生成可回查的证据简报、跨期变化与冲突列表；结论须人工核对证据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT

## Use Case:

面向分析师、研究人员和开发者，用于整理公开报告或公告中的业务实体、指标与原文证据，跟踪资料更新，并生成可复核的变化简报。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Evidence checks may accept unsupported figures or attach page citations to unsupported text.

Mitigation: Independently check each figure, unit, page citation, and claim against the original public document.

Risk: The behavior of the external parsing channel is outside this inspection.

Mitigation: Use the official public setup documentation, a trusted Bridge command, and reviewed parser installation versions; inspect returned source material before relying on it.

## Reference(s):

- [Knowledge input and package contract](references/knowledge-contract.md)
- [Verification record and limitations](references/verification.md)
- [Bounded audio and video workflow](references/av-backtest.md)
- [Official cue-omni-reader](https://github.com/sensedeal/cue-skills/tree/main/cue-omni-reader)
- [cue-omni-reader setup documentation](https://github.com/sensedeal/cue-skills/blob/main/cue-omni-reader/references/setup.md)
- [Omni Reader configuration](https://cuecue.cn/hub/omni-reader)

## Skill Output:

**Output Type(s):** [Markdown, HTML, JSON, Guidance]

**Output Format:** [Evidence brief with expandable source excerpts and a reusable JSON knowledge package; optional searchable HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves scope distinctions and unresolved conflicts; evidence requires human review.]

## Skill Version(s):

0.3.16 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
