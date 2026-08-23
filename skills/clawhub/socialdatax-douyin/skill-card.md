## Description:

用于抖音数据助手、抖音热榜、抖音数据分析、作品搜索、作品详情、评论分析、评论回复分析、达人数据、达人作品和达人短剧/合集。覆盖 Douyin hot search and work research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to run read-only SocialDataX queries for Douyin hot searches, content discovery, work details, comment and reply analysis, creator profiles, creator posts, and short-drama or collection data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocialDataX API key for read-only Douyin data queries.

Mitigation: Provide only SOCIALDATAX_API_KEY and avoid pasting unrelated credentials, account cookies, or private session data.

Risk: The skill relies on Node/npm to fetch and run the SocialDataX CLI package.

Mitigation: Run only the documented socialdatax-skills package in an approved environment before using it for Douyin research.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and parameter guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SOCIALDATAX_API_KEY and Node/npm to run read-only Douyin data queries.]

## Skill Version(s):

0.1.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
