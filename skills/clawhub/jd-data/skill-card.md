## Description:

京东商品数据采集（商品详情 / 商品评论）。当用户需要采集京东商品详情、商品评论，或提到"京东商品详情/京东评论采集/商品评论分析/商品数据分析"时使用。对接数据API中转平台，按次扣点，批量任务前可免费查询余额与单价。

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product analysts use this skill to collect JD product details and customer comments for product research and review analysis. It supports individual requests and budget-checked batch collection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation phrases could trigger paid JD data collection for unrelated requests.

Mitigation: Limit use to explicit JD product detail or comment collection requests, and check the live balance and planned cost before batch jobs.

Risk: The security scan was partial because a referenced output path was missing, so it does not establish complete coverage.

Mitigation: Review the missing referenced output and scan the complete release before relying on scan results.

## Reference(s):

- [JD data service](https://zlh.aidata366.com)
- [JD product pages](https://item.jd.com/)

## Skill Output:

**Output Type(s):** [JSON data, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Structured JSON data with Markdown guidance and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Product details or paginated comments; large responses can be saved to files.]

## Skill Version(s):

1.6.3 (source: release evidence, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
