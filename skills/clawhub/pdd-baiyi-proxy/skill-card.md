## Description: <br>
拼多多百亿补贴 helps agents browse Pinduoduo subsidy product listings with keyword search, price filters, brand-store filtering, pagination, and deal-score sorting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cn-shopping](https://clawhub.ai/user/cn-shopping) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External shoppers and shopping assistants use this skill to find and compare Pinduoduo subsidy-channel products by keyword, category, budget, brand-store status, and sales or price ordering. It returns product-listing guidance and purchase links, but it does not place orders, monitor price history, or issue price-drop alerts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shopping queries and filter values are sent to the publisher's cloud proxy. <br>
Mitigation: Install only if this data sharing is acceptable, and avoid entering sensitive personal information because the skill is designed only for product browsing. <br>
Risk: Returned product links, prices, and listing details may be incomplete or not independently verified. <br>
Mitigation: Review listings before relying on them for purchasing decisions and confirm prices or offers on the merchant site. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cn-shopping/skills/pdd-baiyi-proxy) <br>
- [拼多多实时热销榜](https://clawhub.ai/cn-shopping/pdd-hot-rank) <br>
- [拼多多精选](https://clawhub.ai/cn-shopping/pdd-selection) <br>
- [购物比价助手](https://clawhub.ai/cn-shopping/best-price) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [JSON string containing formatted product-listing text with names, prices, coupons, sales notes, category, goods_sign, image URLs, and source notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results are product-browsing responses generated from shopping filters and cloud-proxy results; returned prices and links should not be treated as independently verified.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
