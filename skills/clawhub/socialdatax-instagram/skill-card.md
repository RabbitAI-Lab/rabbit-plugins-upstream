## Description:

用于 Instagram 数据助手、内容搜索、帖子详情、评论分析、创作者资料和创作者帖子列表。覆盖 Instagram content and creator research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要进行 Instagram 内容与创作者调研的用户，支持搜索帖子、查看帖子详情和评论、查询创作者资料及帖子列表。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes the mutable, unpinned socialdatax-skills CLI package in an environment where an API credential may be available.

Mitigation: Review whether you trust the current CLI release before running it, and use an environment containing only credentials intended for SocialDataX.

Risk: Search terms, supplied URLs, or shared text may be sent to SocialDataX.

Mitigation: Use the skill only with inputs you are comfortable sending to SocialDataX.

Risk: The security scan was partial because three local references could not be resolved.

Mitigation: Treat the scan as incomplete and review the unresolved references before relying on it as a complete security assessment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-instagram)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text]

**Output Format:** [Instagram post, comment, and creator data returned as JSON, with readable CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research results; output depends on the requested Instagram lookup.]

## Skill Version(s):

0.1.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
