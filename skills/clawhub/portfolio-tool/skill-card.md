## Description: <br>
Portfolio Tool helps agents use the Portfolio_tool fund portfolio research service through MCP to query portfolios, sync fund NAV data, view tracking status, search funds, and manage anonymous accounts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dengkane](https://clawhub.ai/user/dengkane) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate a fund portfolio research workflow conversationally, including portfolio lookup, fund search, NAV synchronization, tracking review, and account recovery. It is useful when an agent needs structured MCP tools or a fallback CLI for the same portfolio service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates and reuses a stable device-derived identifier stored at ~/.portfolio/aid and sends it to the configured portfolio backend. <br>
Mitigation: Review this identity behavior before installation, use a trusted HTTPS backend, and rotate or override PORTFOLIO_AID when a different identity should be used. <br>
Risk: The fallback pf.py script is a broad backend client rather than a narrowly limited portfolio command. <br>
Mitigation: Review commands before execution, point PORTFOLIO_API only at trusted backends, and avoid sending sensitive data to untrusted endpoints. <br>
Risk: Account binding and login flows involve user passwords. <br>
Mitigation: Use a unique password for this service and avoid reusing credentials from important accounts. <br>


## Reference(s): <br>
- [Portfolio Tool ClawHub release](https://clawhub.ai/dengkane/skills/portfolio-tool) <br>
- [Streamable HTTP MCP endpoint](https://invest.geeyo.com/mcp/http) <br>
- [SSE MCP endpoint](https://invest.geeyo.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API responses and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call MCP tools or the bundled fallback CLI; portfolio write operations require a stable X-Anonymous-Id value.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
