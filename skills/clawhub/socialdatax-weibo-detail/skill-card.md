## Description:

用于微博数据分析、微博帖子详情、帖子数据、互动指标、内容调研和内容分析。覆盖 Weibo post details，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要查看微博帖文详情的用户和内容分析人员，用于读取单条微博的正文、作者、发布时间、互动指标及可用媒体信息。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocialDataX detail requests use SOCIALDATAX_API_KEY and may consume account credits.

Mitigation: Provide the key through the runtime environment, limit its exposure, and check expected credit use before making requests.

Risk: The CLI is installed from a third-party npm package, whose implementation is outside this review.

Mitigation: Use a reviewed, pinned package version instead of @latest, and choose the local destination explicitly before downloading media.

## Reference(s):

- [SocialDataX API access and management](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [JSON, Text, Files]

**Output Format:** [JSON post details with concise factual text; optional downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only post details; optional media is saved to a user-selected local path.]

## Skill Version(s):

0.1.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
