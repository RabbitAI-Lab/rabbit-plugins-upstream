## Description:

Compare publicly visible Douyin product and shop pages through an existing browser and turn observed prices, labels, reviews, and product selling points into a structured research table.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

抖音商家、内容创作者和选品人员可用它对比公开商品与店铺信息，整理可见价格、评价信号和卖点，并形成内容切入建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser access can expose the skill to the selected signed-in browser session and its permissions.

Mitigation: Use a dedicated browser environment, verify its browserId, and review the browser tool's permissions before installation or use.

Risk: Prices, sales, and review signals may be absent or change over time, which can make comparisons incomplete or misleading.

Mitigation: Report only information visible on the product page at collection time, preserve source URLs, and mark unavailable fields unknown.

## Reference(s):

- [Easy WebBridge (GitHub)](https://github.com/xxjrq/easy-webbridge)
- [Easy WebBridge (Gitee mirror)](https://gitee.com/xxjrq/easy-webbridge)
- [EasyBR official download page](https://www.ebrower.com/down.html)
- [EasyBR v1.7.8 release](https://github.com/xxjrq/easybr/releases/tag/v1.7.8)

## Skill Output:

**Output Type(s):** [Analysis, Files, JSON, CSV, Markdown]

**Output Format:** [products.json, products.csv, and research.md]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records include source URLs and collection times; unavailable fields are marked unknown.]

## Skill Version(s):

1.0.2 (source: package.json, manifest.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
