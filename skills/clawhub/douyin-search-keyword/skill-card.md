## Description:

提供抖音公开内容的只读搜索与数据查询，支持视频和图文、用户、作品、评论及热榜，并为选题、竞品分析、舆情观察和线索研究提供结构化数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

External content, marketing, and research teams can use the skill to search public Douyin videos, posts, creators, comments, and trending topics. It returns structured data to support content planning, competitor review, sentiment monitoring, and demand research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was benign but partial: 26 of 47 components were fully inspected, so some behavior remains unassessed.

Mitigation: Review the skill and its stated capabilities before installation; the scan does not establish that every component is safe.

Risk: User-provided keywords and links are sent to the Guaikei API, and some results may be saved in the skill's logs directory.

Mitigation: Avoid sending sensitive search terms or links, and review log files before sharing them.

## Reference(s):

- [Options and command reference](artifact/references/options.md)
- [Demand mining guide](artifact/references/demand-mining.md)
- [Customer acquisition guide](artifact/references/customer-acquisition.md)
- [Changelog](artifact/references/changelog.md)
- [Guaikei service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Markdown]

**Output Format:** [Structured JSON data and concise Markdown summaries or tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries use public Douyin data; result files may be saved in the skill's logs directory.]

## Skill Version(s):

1.4.3 (source: frontmatter, package.json, changelog, released 2026-11-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
