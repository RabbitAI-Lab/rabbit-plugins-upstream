## Description: <br>
Meituan Coupon Bot helps users search Meituan dine-in and delivery coupons, compare offers, browse hot-sale lists, and receive direct purchase links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[josssong](https://clawhub.ai/user/josssong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to find Meituan coupons for dine-in and delivery food purchases, browse ranked offers, compare prices, and get purchase links for selected coupons. <br>

### Deployment Geography for Use: <br>
China; coupon search is scoped to supported Meituan city codes. <br>

## Known Risks and Mitigations: <br>
Risk: Coupon searches and optional location details are sent to Meituan's API. <br>
Mitigation: Install only where that data sharing is acceptable, and avoid providing precise location details unless needed. <br>
Risk: Returned purchase links may be affiliate or promotional links. <br>
Mitigation: Treat purchase links as promotional and review them before making a purchase. <br>
Risk: API credentials are embedded in the artifact configuration. <br>
Mitigation: Rotate the embedded credentials or move them to secure runtime configuration before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/josssong/skills/meituan-coupon-bot) <br>
- [Publisher profile](https://clawhub.ai/user/josssong) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown coupon-result cards with prices, sales data, images, and purchase links; helper commands return JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include affiliate or promotional purchase links and can use city, page, keyword, and scene parameters.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and scripts/package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
