## Description: <br>
拼多多实时热销榜好货推荐，覆盖41个品类共707件商品，按销量智能排序，支持关键词搜索、价格筛选、品牌店筛选。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cn-shopping](https://clawhub.ai/user/cn-shopping) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and shopping assistants use this skill to browse Pinduoduo hot-selling products, search by keyword or category, filter by price or brand-store status, and compare ranked product options before purchase. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search keywords and filters are sent to a configured cloud proxy. <br>
Mitigation: Avoid sensitive personal information in search terms and use the default endpoint unless you intentionally trust a replacement proxy. <br>
Risk: The skill provides shopping information and purchase links but does not complete purchases, track historical prices, or provide price-drop alerts. <br>
Mitigation: Treat results as shopping discovery output and verify product details, current pricing, and seller terms before buying. <br>


## Reference(s): <br>
- [拼多多实时热销榜 ClawHub page](https://clawhub.ai/cn-shopping/skills/pdd-hot-rank) <br>
- [拼多多百亿补贴](https://clawhub.ai/cn-shopping/pdd-baiyi-proxy) <br>
- [拼多多精选](https://clawhub.ai/cn-shopping/pdd-selection) <br>
- [购物比价助手](https://clawhub.ai/cn-shopping/best-price) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown] <br>
**Output Format:** [JSON object containing a Markdown-ready content string] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Product listings may include prices, sales indicators, merchant and category names, goods_sign identifiers, image URLs, and purchase links.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
