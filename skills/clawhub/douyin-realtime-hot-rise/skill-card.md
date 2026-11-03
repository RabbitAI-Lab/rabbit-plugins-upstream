## Description:

用于查询抖音实时上升热点、飙升话题和热度趋势。当用户想知道哪些话题正在升温、抖音上升榜有哪些热点、某个关键词的排名或热度如何变化，或要按关键词/分类筛选热点时使用。典型请求包括：“最近抖音什么话题在涨”、“查一下这个关键词的抖音上升趋势”、“接下来拍什么选题”。返回热点关键词、分类、当前排名、排名变化、热度值、趋势点和更新时间，为热点跟进与选题判断提供数据。本技能聚焦抖音上升榜及趋势数据；不用于单纯查看总榜、其他平台/全网趋势、达人搜索，或直接生成完整脚本和视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[allinherog-star](https://clawhub.ai/user/allinherog-star)

### License/Terms of Use:

MIT-0

## Use Case:

内容创作者、运营人员、电商与营销团队可按关键词、分类或排名变化查询抖音上升热点，查看热度与趋势数据，为选题和跟进时机提供参考。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured endpoint could redirect a request and expose the API key to another origin.

Mitigation: Before using a real API key, validate the HTTPS destination and ensure redirects cannot forward credentials across origins.

Risk: Query parameters are sent to AI Skills, and requests may consume account balance; live billing behavior was not tested.

Mitigation: Avoid sending sensitive search terms, and check expected usage and account balance before repeated queries.

## Reference(s):

- [Skill listing](https://clawhub.ai/allinherog-star/skills/douyin-realtime-hot-rise)
- [AI Skills service](https://ai-skills.ai)
- [Parameter schema](references/form-schema.json)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [JSON trend data with ranked topics, categories, rank changes, heat scores, trend points, and update times]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 50 topics per request; optionally filtered by keyword or category and ordered by rank or rank change. Results support topic selection but do not guarantee reach or engagement.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
