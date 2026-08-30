## Description:

用于知乎数据助手、知乎热榜、内容搜索、回答文章视频详情、评论分析、创作者资料和文章列表。覆盖 Zhihu content research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run Zhihu hot-list, search, content-detail, comments, replies, creator-profile, and creator-post lookups through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to the user's SocialDataX API key for Zhihu data lookups.

Mitigation: Install only when that credential access is acceptable, and keep SOCIALDATAX_API_KEY scoped to the intended account.

Risk: The documented command uses an npm CLI with @latest, which can change behavior between runs.

Mitigation: Review updates or pin a package version when reproducible behavior is required.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-zhihu)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and API result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY and Node.js/npm; uses the socialdatax-skills npm CLI for read-only Zhihu lookups.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
