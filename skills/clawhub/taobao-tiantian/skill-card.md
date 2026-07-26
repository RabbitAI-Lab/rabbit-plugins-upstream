## Description: <br>
淘宝天天特卖频道商品查询，100%天猫品牌店精选，涵盖家居日用、洗护清洁、零食粮油等全品类，价格多在5-30元，支持销量/价格/热度4种排序。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cn-shopping](https://clawhub.ai/user/cn-shopping) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Shopping-focused agents and users use this skill to browse Taobao Daily Deals, sort product listings by sales, price, or recommendation heat, inspect item details, and retrieve coupon and purchase links. It supports product discovery only and does not perform checkout, account, or payment actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Taobao shopping requests, product IDs, and sorting choices are sent through the publisher's cloud proxy. <br>
Mitigation: Use the skill only for product lookup; avoid entering personal, account, payment, or private browsing information. <br>
Risk: The skill returns product information and purchase links, so prices, coupons, availability, and destination pages can change outside the skill. <br>
Mitigation: Review item details and links on Taobao before relying on the information or making a purchase. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cn-shopping/skills/taobao-tiantian) <br>
- [Publisher profile](https://clawhub.ai/user/cn-shopping) <br>
- [淘宝好券精选](https://clawhub.ai/cn-shopping/taobao-haoquan) <br>
- [淘宝精选](https://clawhub.ai/cn-shopping/taobao-selection) <br>
- [购物比价助手](https://clawhub.ai/cn-shopping/best-price) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, links] <br>
**Output Format:** [JSON-wrapped text responses with product summaries, item IDs, image URLs, coupon information, and purchase links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include paginated product lists, single-item detail views, and channel statistics.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
