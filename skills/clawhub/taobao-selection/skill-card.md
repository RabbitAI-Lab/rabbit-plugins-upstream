## Description: <br>
淘宝天猫好货搜索比价领券，标品按到手价排序找最低价，非标品按销量排序找口碑好货，自动筛选包邮+消保+高评分商品，返回优惠券和购买链接。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cn-shopping](https://clawhub.ai/user/cn-shopping) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to search Taobao and Tmall products, compare standard items by final price, find lifestyle goods by sales, filter by budget or Tmall status, and receive coupon and purchase links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms, price filters, paging choices, and Tmall filters are sent to a publisher-operated proxy service. <br>
Mitigation: Use the skill only when that proxy data sharing is acceptable for the shopping query, and avoid submitting sensitive personal information as search text. <br>
Risk: The artifact supports overriding the proxy endpoint and includes a fallback proxy token. <br>
Mitigation: Do not override PROXY_URL unless the endpoint is trusted, and prefer a managed PROXY_TOKEN over relying on the fallback token. <br>


## Reference(s): <br>
- [ClawHub listing for 淘宝精选](https://clawhub.ai/cn-shopping/skills/taobao-selection) <br>
- [淘宝天天特卖](https://clawhub.ai/cn-shopping/taobao-tiantian) <br>
- [淘宝好券精选](https://clawhub.ai/cn-shopping/taobao-haoquan) <br>
- [购物比价助手](https://clawhub.ai/cn-shopping/best-price) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown] <br>
**Output Format:** [JSON object containing human-readable shopping results text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results include product title, shop type, price, coupon details when available, sales, shop, category, and purchase link.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
