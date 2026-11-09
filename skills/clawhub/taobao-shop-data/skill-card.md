## Description:

淘宝电商数据采集（商品详情/商品评论/店铺商品列表）。当用户需要获取淘宝商品的标题、价格、图片、规格与销量，采集淘宝商品评论，或拉取某个淘宝店铺的全部在售商品时使用。对接数据API中转平台，按次扣点，批量任务前可免费查询余额与单价。

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT

## Use Case:

External users can retrieve Taobao product details, product reviews, and a shop's listings for product research, review analysis, and shop monitoring. Batch requests can be planned against the platform's current per-call prices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API calls consume platform points, and paginated requests can add cost.

Mitigation: Check the current prices and balance before a batch, estimate its cost, and stop when results are empty or the balance is insufficient.

Risk: The security review was partial; the skill uses network access and writes responses to selected paths, while its tool scope is undeclared.

Mitigation: Confirm the required network and file access in the intended environment, protect the API key, and restrict access to saved responses.

## Reference(s):

- [淘宝电商数据采集 (ClawHub)](https://clawhub.ai/cuiyunhai/skills/taobao-shop-data)
- [数据 API 平台](https://zlh.aidata366.com)

## Skill Output:

**Output Type(s):** [API data, JSON files]

**Output Format:** [JSON API responses, optionally saved as .json files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paged results; API calls consume platform points.]

## Skill Version(s):

1.0.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
