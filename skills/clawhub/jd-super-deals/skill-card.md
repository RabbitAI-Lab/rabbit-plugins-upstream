## Description: <br>
京东自营超级补贴 helps users query JD Super Subsidy self-operated products and filter or sort results by keyword, price, rating threshold, and subsidy strength. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cn-shopping](https://clawhub.ai/user/cn-shopping) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External shoppers use this skill to discover JD self-operated subsidized products, compare sale prices, and retrieve product image and purchase links without placing orders through the skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shopping search terms and filters are sent to the publisher's Tencent Cloud proxy. <br>
Mitigation: Use non-sensitive shopping queries and avoid entering private personal details as keywords. <br>
Risk: The artifact includes a default proxy token and configurable proxy URL. <br>
Mitigation: Review proxy configuration before deployment and override or rotate proxy credentials through environment variables when appropriate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cn-shopping/skills/jd-super-deals) <br>
- [京东自营新品首发](https://clawhub.ai/cn-shopping/jd-new-arrivals) <br>
- [京东自营历史最低价](https://clawhub.ai/cn-shopping/jd-lowest-price) <br>
- [购物比价助手](https://clawhub.ai/cn-shopping/best-price) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [JSON string containing product result data and a human-readable summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Product results may include product names, reference prices, coupon prices, discount percentages, shop and brand names, tags, image URLs, purchase URLs, categories, recent orders, and good-comment percentages.] <br>

## Skill Version(s): <br>
1.2.2 (source: server release evidence and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
