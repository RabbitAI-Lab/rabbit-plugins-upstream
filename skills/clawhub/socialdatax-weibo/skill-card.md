## Description:

用于微博数据助手、微博热搜、微博内容研究、帖子详情、评论分析、评论回复观察、转赞互动、创作者资料和创作者内容列表。覆盖 Weibo post research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve read-only Weibo hot-search, post, comment, reply, engagement, creator profile, and creator content data through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs the socialdatax-skills npm package and uses SOCIALDATAX_API_KEY.

Mitigation: Install and run it only when SocialDataX and the npm package are trusted, and keep the API key in the environment rather than in skill files.

Risk: Runtime failures may come from missing Node.js/npm, network access, package installation, permissions, parameters, links, IDs, or API-key/account status.

Mitigation: Check the local runtime, dependency, network, authorization, API key, and command parameters before retrying; avoid repeated retries for insufficient-balance errors.

Risk: The skill returns Weibo data but does not perform account-control actions.

Mitigation: Use it for read-only lookup and analysis; do not extend it to login, post, like, comment, or change accounts without a separate review.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo)
- [ClawHub publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and read-only Weibo data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY plus Node.js/npm access for the socialdatax-skills package.]

## Skill Version(s):

0.1.18 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
