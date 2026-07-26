## Description: <br>
美团优惠券 helps agents search national, multi-city coupons for chain brands and category keywords, then return coupon listings sorted by sales. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cn-shopping](https://clawhub.ai/user/cn-shopping) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and shopping-focused agents use this skill to search Meituan-style coupons by brand or category keyword and summarize nationally usable offers, including prices, sales labels, images, pagination, and purchase links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Coupon search keywords are sent to the skill publisher's external proxy. <br>
Mitigation: Use non-sensitive brand or category keywords and avoid entering private personal information. <br>
Risk: The skill may return generated shopping or referral links. <br>
Mitigation: Review the destination and offer terms before making a purchase. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cn-shopping/skills/brand-coupons) <br>
- [Publisher profile](https://clawhub.ai/user/cn-shopping) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown-formatted coupon results with prices, images, pagination hints, and referral links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts a keyword and optional page number; returns up to 30 nationally usable coupon entries per page.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
