## Description:

用于小红书评论分析、小红书评论回复、用户反馈、口碑分析、痛点总结和内容讨论分析，覆盖 Xiaohongshu / XHS / RedNote 评论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要了解小红书受众反馈的用户，读取指定笔记的评论和回复，并整理讨论主题、情绪线索、异议、痛点、常见问题及回复建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed if stored in skill files or ordinary text.

Mitigation: Keep the API key in the client's secret store and out of skill files, chat, logs, and screenshots.

Risk: Share text may contain private information unrelated to the requested note.

Mitigation: Use the needed note ID or URL where possible and remove unrelated private information from share text.

Risk: Unbounded collection can consume service credits, and dependency or hosted-service behavior is outside this review.

Mitigation: Set collection limits and prefer a reviewed, pinned CLI version; this review does not establish the safety of future package releases or the hosted backend.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-comments)

## Skill Output:

**Output Type(s):** [JSON, text, analysis, guidance]

**Output Format:** [Structured JSON comment data with concise text or Markdown analysis and reply suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only comment retrieval; analysis should distinguish observed themes from inferred sentiment and state whether results cover one or multiple pages.]

## Skill Version(s):

0.1.21 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
