## Description:

用于 X / Twitter 内容搜索、帖子详情、评论分析、创作者资料、帖子列表及博主发出的回复（含自回复）。覆盖 X post and creator research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to search X posts, inspect post details and discussions, and retrieve creator profiles, posts, and creator-authored replies. It supports read-only X/Twitter research through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill repeatedly runs an automatically installed, mutable latest CLI version, and the security review reports partial scan coverage.

Mitigation: Pin the CLI to a reviewed release, check its integrity, and review unresolved related material before installation.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-x-twitter)

## Skill Output:

**Output Type(s):** [JSON, Text, Analysis]

**Output Format:** [Structured X/Twitter data in JSON, with concise research summaries or analysis when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results vary by the requested post, discussion, search, or creator query.]

## Skill Version(s):

0.1.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
