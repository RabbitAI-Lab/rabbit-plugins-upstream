## Description: <br>
麦当劳助手 - 查询/领取优惠券、活动日历、餐品营养信息、门店查询 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hi-yu](https://clawhub.ai/user/hi-yu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to query McDonald's coupons, claimed coupons, campaign timing, nutrition information, and store-related service data through the configured MCP service. It can also claim available coupons when the user clearly asks for that account-changing action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a user-provided MCD_TOKEN to access the MCP service. <br>
Mitigation: Keep MCD_TOKEN private, avoid exposing it in shared logs or public prompts, and rotate it if it is disclosed. <br>
Risk: Changing MCD_MCP_URL can route requests and bearer tokens to an untrusted endpoint. <br>
Mitigation: Leave MCD_MCP_URL at the documented default unless the alternate endpoint has been intentionally verified. <br>
Risk: The auto-bind-coupons tool can change the user's account state by claiming coupons. <br>
Mitigation: Run coupon-claiming actions only after a clear user request and distinguish them from read-only coupon queries. <br>
Risk: Coupon, campaign, and nutrition results may change over time or be limited by rate limits and token validity. <br>
Mitigation: Treat MCP responses as current service data, surface token or rate-limit errors to the user, and re-query when timing matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hi-yu/skills/mcd) <br>
- [Publisher profile](https://clawhub.ai/user/hi-yu) <br>
- [McDonald's MCP service](https://mcp.mcd.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and tabular or list-style responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include coupon names, discounts, validity periods, usage conditions, campaign timing, nutrition tables, and MCP error messages.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
