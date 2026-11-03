## Description:

用于 X / Twitter 内容搜索、帖子详情、评论分析、创作者资料、帖子列表及博主发出的回复（含自回复）。覆盖 X post and creator research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

People researching X/Twitter content can use this skill to search posts, inspect post details and discussions, look up creator profiles and posts, and find replies authored by a creator. It is intended for read-only social media research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries, URLs, and identifiers are sent to SocialDataX and may consume paid credits.

Mitigation: Avoid sensitive search inputs and check the relevant account and credit terms before making requests.

Risk: An exposed API key or local credential file could grant access to the service account.

Mitigation: Keep the key in supported secret storage and exclude local credential files from version control.

Risk: The downloaded npm implementation was not included in the supplied artifact or audited in the security evidence.

Mitigation: Prefer a reviewed, pinned CLI version and limit its local access.

## Reference(s):

- [SocialDataX API access and product page](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-x-twitter)

## Skill Output:

**Output Type(s):** [API Calls, Research results, JSON, Guidance]

**Output Format:** [Structured X/Twitter data returned through SocialDataX, with usage guidance in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only post, comment, reply, and creator data; API calls may consume paid credits.]

## Skill Version(s):

0.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
