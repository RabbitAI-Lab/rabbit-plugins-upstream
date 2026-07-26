## Description: <br>
McDonald's China assistant for querying and claiming coupons, viewing campaign calendars, checking menu nutrition, and finding stores. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hi-yu](https://clawhub.ai/user/hi-yu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to call the McDonald's China MCP service for current coupons, promotions, nutrition data, time context, and store lookup. The skill can also claim coupons on the user's account when authorized. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can claim McDonald's coupons on the user's account without a clear confirmation step. <br>
Mitigation: Only use the skill with a trusted MCD_TOKEN and instruct the agent to ask for explicit confirmation before any coupon-claiming action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hi-yu/skills/mcdonald-cn) <br>
- [McDonald's China MCP service](https://mcp.mcd.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline bash commands and structured JSON response guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses MCD_TOKEN and optional MCD_MCP_URL to call a JSON-RPC MCP service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
