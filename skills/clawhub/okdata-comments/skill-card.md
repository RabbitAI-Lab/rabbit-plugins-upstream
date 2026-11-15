## Description:

Read what people say about a product, brand or topic in comments and posts on Douyin, Xiaohongshu (RedNote), Bilibili, Weibo, TikTok, X (Twitter) and YouTube with the okdata API, then sum up praise, complaints, questions and buying signals with quotes and links. Use when the user asks about word of mouth, reviews, sentiment, user feedback, complaints, or what commenters think of a video, note or launch. 口碑分析：评论区和帖子里大家怎么说，夸什么、骂什么、问什么，附原话和链接。

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

Brand teams, marketers, product managers, and researchers use this skill to review public comments and posts about a product, brand, or topic. It groups sampled feedback into praise, complaints, questions, and buying signals, then provides themes, quotes, counts, and links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to okdata, and liker or retweeter endpoints can return account identity details.

Mitigation: Tell users before searching, avoid sensitive queries, and do not compile or profile identities; include only the identity detail needed to support a public quote.

Risk: The security assessment reports medium confidence and partial coverage because some local references could not be resolved.

Mitigation: Review the skill's linked API information and unresolved references before relying on it for sensitive research.

## Reference(s):

- [ClawHub release](https://clawhub.ai/conn-ho/skills/okdata-comments)
- [okdata API documentation](https://okdata.online/apis/)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown report with category counts, feedback themes, quotes, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sample-based findings with source and date context; reports actual API costs when available.]

## Skill Version(s):

0.1.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
