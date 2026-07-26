## Description: <br>
My Mcdonald helps agents query and claim McDonald's coupons, view campaign calendars, retrieve nutrition information, and check current McDonald's activity through the McDonald's MCP service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pmwalkercao](https://clawhub.ai/user/pmwalkercao) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users ask an agent to retrieve current McDonald's offers, campaign timing, coupon status, and nutrition data, and to prepare coupon-claiming API calls when explicitly approved. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent uses an MCD_TOKEN bearer credential to call the McDonald's MCP service. <br>
Mitigation: Keep MCD_TOKEN private, avoid exposing it in chat transcripts or logs, and rotate it if it is shared accidentally. <br>
Risk: The skill includes a one-click coupon claiming action that can affect the user's account. <br>
Mitigation: Require explicit user approval before running auto-bind-coupons or any equivalent coupon-claiming command. <br>
Risk: Changing MCD_MCP_URL can redirect authenticated requests to an untrusted destination. <br>
Mitigation: Use the default service URL unless the replacement endpoint is trusted by the user. <br>


## Reference(s): <br>
- [McDonald's MCP service](https://mcp.mcd.cn) <br>
- [ClawHub skill listing](https://clawhub.ai/pmwalkercao/skills/mymcdonald) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with shell command examples and JSON API results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses an MCD_TOKEN bearer credential and may return text content or structured JSON from the McDonald's MCP service.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
