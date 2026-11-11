## Description:

淘宝电商数据采集（商品详情/商品评论/店铺商品列表）。当用户需要获取淘宝商品的标题、价格、图片、规格与销量，采集淘宝商品评论，或拉取某个淘宝店铺的全部在售商品时使用。对接AI数据平台，按次扣点，批量任务前可免费查询余额与单价。

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can retrieve Taobao product details, product reviews, and shop listings for product research, review insights, and shop monitoring. Check the current point balance and endpoint price before paid collection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid collection requests deduct platform points, and endpoint prices can change.

Mitigation: Check the free balance and current endpoint price before collection, and get user confirmation before running paid or batch requests.

Risk: Login credentials and collected data are written to local paths that may be configured by the environment or command options.

Mitigation: Use user-approved locations, protect the local credential file, and check the destination before saving response files.

## Reference(s):


## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Paginated JSON data with shell commands and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses can be saved to a user-selected file; comments and shop listings support pagination.]

## Skill Version(s):

1.0.6 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
