## Description:

小红书电商数据采集（商品搜索/店铺商品列表/商品详情）。当用户需要按关键词搜索小红书的在售商品、拉取某个小红书店铺的全部商品、或获取某个小红书商品的详情（价格、销量、店铺、图片）时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT-0

## Use Case:

开发者可用此技能从小红书商城按关键词搜索商品、查看店铺在售商品并提取单品价格、店铺指标和图片，用于选品分析、竞品比价与店铺监控。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Collection requests consume platform points, and continuing pagination can incur charges even when a page is empty.

Mitigation: Check the free balance and current interface price first; stop when a page returns fewer than 20 items.

Risk: The CLI stores the API key in a local config file and sends it to the configured data platform.

Mitigation: Protect the local config file and verify the platform URL before providing credentials.

Risk: The scanner reports a benign but partially complete review, and its guidance calls out broad capabilities and unclear tool scope.

Mitigation: Review the requested collection commands and destination for each task, and inspect unresolved references before deployment.

## Reference(s):

- [xhs-shop-data on ClawHub](https://clawhub.ai/cuiyunhai/skills/xhs-shop-data)
- [Data API platform](https://zlh.aidata366.com)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON product data and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be saved as JSON files; search responses may be large.]

## Skill Version(s):

1.0.4 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
