## Description: <br>
Searches JD's 9.9 free-shipping channel for self-operated products, with filters for category keywords, maximum price, review rate, sorting, and pagination. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cn-shopping](https://clawhub.ai/user/cn-shopping) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External shoppers and shopping assistants use this skill to find low-cost JD self-operated products with free shipping, filter by category or price, and return product summaries and purchase links for comparison before buying. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shopping search terms and filter settings are sent to the publisher's Tencent cloud proxy to fetch JD product data. <br>
Mitigation: Use only non-sensitive shopping queries and install the skill only when the publisher's proxy handling is acceptable for the deployment. <br>
Risk: The artifact includes an embedded proxy token for the Tencent cloud proxy. <br>
Mitigation: The publisher should rotate the embedded token and prefer environment-provided proxy credentials for releases. <br>
Risk: The skill returns product information and purchase links but cannot complete purchases, set price alerts, or provide historical price checks. <br>
Mitigation: Verify item details, price, availability, and seller terms on JD before purchase or downstream recommendation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cn-shopping/skills/jd-99-baoyou) <br>
- [Publisher profile](https://clawhub.ai/user/cn-shopping) <br>
- [京东自营秒杀](https://clawhub.ai/cn-shopping/jd-seckill) <br>
- [京东自营超级补贴](https://clawhub.ai/cn-shopping/jd-super-deals) <br>
- [购物比价助手](https://clawhub.ai/cn-shopping/best-price) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, markdown] <br>
**Output Format:** [JSON string with a summary field and a content field containing a JSON array of product records.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Product records can include names, prices, coupon prices, discount percentage, shop and brand names, category fields, order counts, review rates, image URLs, and buy URLs.] <br>

## Skill Version(s): <br>
0.4.2 (source: server release evidence; artifact frontmatter reports 0.4.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
