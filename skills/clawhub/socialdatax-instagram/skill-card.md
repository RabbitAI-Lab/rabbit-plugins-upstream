## Description:

为 Instagram 内容研究提供内容搜索、帖子详情、评论分析、创作者资料和创作者帖子列表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and social-media researchers can search Instagram content and review posts, comments, creator profiles, and creator post lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted research inputs are received by SocialDataX and may contain sensitive information.

Mitigation: Exclude confidential material from queries and shared text; follow applicable privacy and data-handling rules.

Risk: The API key and third-party CLI dependency require careful handling.

Mitigation: Protect SOCIALDATAX_API_KEY as a secret, review package changes, and pin the CLI version where practical.

Risk: Large pagination requests can consume service credits.

Mitigation: Set appropriate page and item limits and avoid unbounded requests unless needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-instagram)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Pretty-printed JSON data and command-line instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Instagram research results; results depend on the query and API response.]

## Skill Version(s):

0.1.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
