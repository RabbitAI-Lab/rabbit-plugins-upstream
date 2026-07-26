## Description: <br>
京东历史最低价商品查询，展示正处于历史低价的自营商品，好评≥97%品质精选，支持品类搜索、价格筛选、降价幅度排序，抄底捡漏必备。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cn-shopping](https://clawhub.ai/user/cn-shopping) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External shoppers use this skill to find JD self-operated products that are currently presented as historical-low-price deals, with filtering by keyword, price, rating threshold, and sort order. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: JD shopping search terms and filters are sent to the skill publisher's Tencent Cloud proxy. <br>
Mitigation: Avoid entering personal information in keywords or filters, and install only if this data flow is acceptable. <br>
Risk: Returned buying links are external shopping links. <br>
Mitigation: Review product pages, sellers, prices, and account prompts before opening links or purchasing. <br>
Risk: Historical-low-price status and product availability can change after a query. <br>
Mitigation: Recheck the current price and item details on JD before making a purchase decision. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cn-shopping/skills/jd-lowest-price) <br>
- [Publisher profile](https://clawhub.ai/user/cn-shopping) <br>
- [京东自营超级补贴](https://clawhub.ai/cn-shopping/jd-super-deals) <br>
- [京东自营9.9包邮](https://clawhub.ai/cn-shopping/jd-99-baoyou) <br>
- [购物比价助手](https://clawhub.ai/cn-shopping/best-price) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, markdown, guidance] <br>
**Output Format:** [JSON string with a human-readable summary and a structured product list that agents can present as text or Markdown.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Product entries may include names, prices, discount percentage, shop and category data, image URLs, and external buying links.] <br>

## Skill Version(s): <br>
1.2.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
