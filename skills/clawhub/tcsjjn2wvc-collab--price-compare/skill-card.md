## Description: <br>
Compares product, takeaway, coupon, and red-packet prices across Meituan, JD, Taobao, Eleme, and related affiliate platforms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tcsjjn2wvc-collab](https://clawhub.ai/user/tcsjjn2wvc-collab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to compare item prices, takeaway offers, coupons, and red-packet links across Chinese e-commerce and food-delivery platforms, with command-line and WeChat mini-program integration paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports live-looking API, server, database, and admin credentials in the release. <br>
Mitigation: Remove bundled credentials, rotate any exposed secrets, replace them with placeholders, and require missing secrets to fail closed before installation or use. <br>
Risk: The security review reports that user activity is routed through a fixed backend. <br>
Mitigation: Document every backend and third-party data flow, let deployers configure their own backend, and avoid sending user activity to the bundled endpoint without review. <br>
Risk: Coupon claims, search history, and location or city-based lookup flows may involve user activity or location-adjacent data. <br>
Mitigation: Add explicit user consent and clear retention expectations for coupon claims, history access, and city-based or location-based queries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tcsjjn2wvc-collab/price-compare) <br>
- [Artifact API reference](references/api_docs.md) <br>
- [WeChat Mini Program OpenAPI documentation](https://developers.weixin.qq.com/miniprogram/dev/OpenApi/) <br>
- [Meituan Open Platform documentation](https://open.meituan.com/) <br>
- [JD Union documentation](https://union.jd.com/) <br>
- [Eleme Open Platform documentation](https://open.ele.me/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown tables, JSON result objects, Python and JavaScript code, shell command examples, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call external affiliate, delivery, e-commerce, and mini-program backends when configured.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
