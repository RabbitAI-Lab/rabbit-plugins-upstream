## Description: <br>
淘宝好券精选频道商品查询，天猫品牌店占比98%+，优惠券覆盖率90%+，涵盖洗护美容、咖啡零食等品类，价格多在5-50元，领券购物更省钱。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cn-shopping](https://clawhub.ai/user/cn-shopping) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External shopping users use this skill to browse Taobao and Tmall coupon products, sort listings by sales, price, or recommendation heat, inspect coupon details, and access purchase links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Coupon lookup requests are sent through the publisher's cloud proxy, which is part of the trust boundary for this skill. <br>
Mitigation: Install only if proxy-mediated Taobao coupon lookup is acceptable, and avoid sending sensitive personal or account information through prompts or tool parameters. <br>
Risk: Coupon prices, availability, purchase links, and thresholds may change after lookup. <br>
Mitigation: Confirm final price, coupon eligibility, and seller information on the destination Taobao or Tmall page before purchasing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cn-shopping/skills/taobao-haoquan) <br>
- [Publisher profile](https://clawhub.ai/user/cn-shopping) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [JSON string containing human-readable product listings, product details, or channel statistics] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only coupon lookup output may include product titles, prices, coupon details, image URLs, item IDs, shop names, and purchase links.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
