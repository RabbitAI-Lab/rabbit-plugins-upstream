## Description:

当用户需要做抖音内容研究、抖音选题、热点观察、竞品内容对比、趋势判断或素材整理时使用。面向内容运营、品牌调研和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向内容运营、品牌调研人员和创作者，用于观察抖音热榜、研究关键词相关内容、比较竞品内容并整理趋势和选题线索。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to the SocialDataX service.

Mitigation: Avoid including confidential or sensitive queries.

Risk: The API key and searches are handled through a third-party service.

Mitigation: Protect SOCIALDATAX_API_KEY and use it only in the intended environment.

Risk: Broad requests can consume service credits, and unpinned package updates can change behavior.

Mitigation: Set page and item limits, and prefer a reviewed, pinned CLI release over @latest.

## Reference(s):

- [抖音内容研究 on ClawHub](https://clawhub.ai/devinchen2014/skills/douyin-content-research)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Markdown research summaries with rankings, content examples, source links or IDs, and follow-up angles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research results; may include content IDs, links, authors, metrics, publication times, and content types for traceability.]

## Skill Version(s):

0.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
