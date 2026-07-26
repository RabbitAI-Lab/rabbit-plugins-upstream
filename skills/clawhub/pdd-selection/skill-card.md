## Description: <br>
拼多多商品搜索、详情查询和频道好货浏览三合一工具，支持百亿补贴/秒杀/销量榜等频道，返回优惠价格、优惠券和购买链接。夏日拼多多好物，精选高性价比商品 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cn-shopping](https://clawhub.ai/user/cn-shopping) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External shoppers use this skill to search Pinduoduo products, review item details, compare coupons and prices, and browse deal channels before opening purchase links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shopping searches and product identifiers are sent through the skill's cloud proxy. <br>
Mitigation: Install only if this routing is acceptable; avoid entering personal, account, payment, order, or logistics information. <br>
Risk: Returned product prices, coupons, sales counts, and purchase links can change or be incomplete. <br>
Mitigation: Confirm the final price, coupon terms, seller details, and checkout information on Pinduoduo before buying. <br>
Risk: The skill provides product information and links but does not place orders, check order status, or track logistics. <br>
Mitigation: Use official Pinduoduo account and order channels for checkout, payment, order status, and logistics. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cn-shopping/skills/pdd-selection) <br>
- [拼多多百亿补贴](https://clawhub.ai/cn-shopping/pdd-baiyi-proxy) <br>
- [拼多多实时热销榜](https://clawhub.ai/cn-shopping/pdd-hot-rank) <br>
- [购物比价助手](https://clawhub.ai/cn-shopping/best-price) <br>


## Skill Output: <br>
**Output Type(s):** [text] <br>
**Output Format:** [JSON envelope containing Chinese text summaries with product names, prices, coupons, sales notes, image URLs, goods_sign values, and product identifiers] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses are bounded by tool parameters such as page_size and limit; the artifact clamps those values between 10 and 100.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
