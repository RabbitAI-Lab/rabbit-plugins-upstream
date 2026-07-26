## Description: <br>
京东秒杀频道限时好货查询，仅筛选京东自营商品，好评≥98%品质精选，支持品类搜索、价格筛选、折扣力度排序，并通过腾讯云代理转发商品数据查询。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cn-shopping](https://clawhub.ai/user/cn-shopping) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Shopping users and agents use this skill to query time-limited JD seckill listings, filter for JD self-operated products by keyword and maximum price, and sort results by score, price, or discount. It returns product information and purchase links, but does not place orders or manage reminders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search keywords and filter values are sent to the publisher's Tencent Cloud proxy to retrieve product data. <br>
Mitigation: Avoid personal or sensitive information in shopping keywords and use the skill only when proxy-mediated product lookup is acceptable. <br>
Risk: Publisher-managed proxy configuration and token handling may affect access scope and operational exposure. <br>
Mitigation: The publisher should keep proxy access narrowly scoped to product lookup, protect or rotate proxy credentials, and continue disclosing the proxy path to users. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cn-shopping/skills/jd-seckill) <br>
- [Publisher profile](https://clawhub.ai/user/cn-shopping) <br>
- [京东自营9.9包邮](https://clawhub.ai/cn-shopping/jd-99-baoyou) <br>
- [京东自营超级补贴](https://clawhub.ai/cn-shopping/jd-super-deals) <br>
- [购物比价助手](https://clawhub.ai/cn-shopping/best-price) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [JSON string containing a human-readable summary and a product listing payload] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Paginated results, usually up to 50 items per page; items may include product names, prices, discount percentage, shop and category fields, image URLs, and purchase URLs.] <br>

## Skill Version(s): <br>
0.4.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
