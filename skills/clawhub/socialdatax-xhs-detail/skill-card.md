## Description:

用于小红书数据分析、小红书笔记详情、笔记数据、互动指标、内容调研和内容分析。覆盖 Xiaohongshu / XHS / RedNote note details，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content researchers, analysts, and developers use this skill to retrieve Xiaohongshu / XHS / RedNote note details and engagement metrics for content research and analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API key configuration may expose credentials or place them in an unintended environment.

Mitigation: Use a dedicated SocialDataX key with supported secret storage, and keep local key configuration out of version control.

Risk: The external CLI behavior is not verified by the bundled instruction file.

Mitigation: Review and pin a CLI version before use, and choose media download destinations deliberately.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON note details with factual fields such as content, author, publish time, engagement counts, and media summaries when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available fields depend on the returned note data.]

## Skill Version(s):

0.1.18 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
