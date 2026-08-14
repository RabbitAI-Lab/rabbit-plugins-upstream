## Description:

专利资产看板检索技能，封装多个智慧芽专利检索API能力，支持按申请人、关键词等维度检索专利，返回去重后的专利列表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and patent-analysis teams use this skill to query Zhihuiya patent APIs for applicant, patent-type, trend, inventor, overseas-layout, strategic-industry, and word-cloud data for patent asset dashboards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Zhihuiya/OpenAPI token for patent queries.

Mitigation: Use the ZHIHUIYA_API_TOKEN environment variable or a protected secret mechanism instead of passing tokens on the command line.

Risk: Patent counts can be inaccurate if collapse_order_authority is used inconsistently with the documented request bodies.

Mitigation: Review collapse parameter behavior before relying on returned counts for dashboards or reports.

## Reference(s):

- [API 调用说明](references/api_notes.md)
- [Zhihuiya Open Platform](https://open.zhihuiya.com/)
- [Patent Query Search API](https://connect.zhihuiya.com/search/patent/query-search-patent/v2)
- [Patent Trends Query API](https://connect.zhihuiya.com/insights-openapi/patent-trends-query)
- [Inventor Ranking API](https://connect.zhihuiya.com/insights/inventor-ranking)
- [Word Cloud Query API](https://connect.zhihuiya.com/insights/word-cloud-query)

## Skill Output:

**Output Type(s):** [API Calls, Code, Shell commands, Configuration instructions, Analysis]

**Output Format:** [Markdown guidance and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Zhihuiya/OpenAPI bearer token for live API queries.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
