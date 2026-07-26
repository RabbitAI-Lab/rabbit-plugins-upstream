## Description: <br>
McDonald's assistant for querying and claiming coupons, checking campaign calendars, reviewing nutrition information, and finding stores through the mcp.mcd.cn service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hi-yu](https://clawhub.ai/user/hi-yu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to retrieve current McDonald's coupons, claim available coupons with approval, view promotional calendars, and present nutrition information for meal planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated requests use MCD_TOKEN and can expose account access if the token is shared or sent to an unexpected endpoint. <br>
Mitigation: Store MCD_TOKEN as a private secret, verify the mcp.mcd.cn endpoint before use, and avoid displaying the token in public logs or responses. <br>
Risk: Coupon-claiming actions can change the user's account state. <br>
Mitigation: Require explicit user approval before claiming coupons or making account-changing requests. <br>
Risk: Coupon, campaign, and nutrition data can change over time. <br>
Mitigation: Query the service for current data before presenting availability, expiration, or meal-planning guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hi-yu/skills/mcdonald) <br>
- [McDonald's MCP service](https://mcp.mcd.cn) <br>
- [Publisher profile](https://clawhub.ai/user/hi-yu) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API calls, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and structured coupon, campaign, and nutrition summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses MCD_TOKEN for authenticated requests and may return JSON-RPC text or structuredContent from the service.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
