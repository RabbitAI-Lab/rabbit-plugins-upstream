## Description: <br>
购物比价助手 compares shopping queries across supported marketplace data sources, with current evidence showing implemented JD and Taobao/Tmall comparison while Pinduoduo coverage is overstated. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cn-shopping](https://clawhub.ai/user/cn-shopping) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External shoppers use this skill to compare candidate product prices, coupons, shop details, sales signals, and purchase links before deciding where to buy. Reviewers should account for the security evidence that Pinduoduo coverage is not supported by the implementation and that search terms are sent through cloud proxy services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Marketplace coverage may be misleading because security evidence says Pinduoduo support is overstated and the implementation is limited to JD and Taobao/Tmall comparison. <br>
Mitigation: Present the skill as JD and Taobao/Tmall price comparison unless updated evidence proves Pinduoduo support, and verify any claimed Pinduoduo result outside the skill. <br>
Risk: Shopping queries are sent to cloud proxy services and the package includes a shared proxy token. <br>
Mitigation: Avoid sensitive or personal search terms, review proxy handling before deployment, and replace bundled credentials with managed deployment secrets where possible. <br>
Risk: Prices, coupons, sales signals, and purchase links can be stale or mismatched across retailers. <br>
Mitigation: Verify product identity, final price, coupon eligibility, and seller details on the retailer page before purchase. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cn-shopping/skills/best-price) <br>
- [京东自营精选 companion skill](https://clawhub.ai/cn-shopping/jd-selection) <br>
- [淘宝精选 companion skill](https://clawhub.ai/cn-shopping/taobao-selection) <br>
- [拼多多精选 companion skill](https://clawhub.ai/cn-shopping/pdd-selection) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, guidance] <br>
**Output Format:** [Plain text comparison guidance, emitted by the CLI as JSON-wrapped content.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes product names, prices, coupon-adjusted prices, shop details, sales or rating signals, and purchase links when available.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
