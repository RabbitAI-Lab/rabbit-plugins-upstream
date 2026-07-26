## Description: <br>
Real-time crypto risk intelligence; before and as things break. Two tools: Flare (15-min precursor detection, immediate alarms) and Core (60-min state synthesis, context assessment). Free access to the last analysis. No API key required. Upgrade to x402 for custom analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bilalmotiwala](https://clawhub.ai/user/bilalmotiwala) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use BlackClaw to fetch public BlackSwan crypto market-risk summaries, checking immediate Flare alerts and broader Core market context before presenting risk briefings. The returned assessments should be treated as informational context rather than automatic trading or financial advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts BlackSwan's external service to retrieve crypto market-risk information. <br>
Mitigation: Install and use it only when external calls to BlackSwan are acceptable for the agent's environment. <br>
Risk: Crypto risk assessments may be misused as automatic trading or financial advice. <br>
Mitigation: Present the assessments as informational context and require human review before financial decisions. <br>


## Reference(s): <br>
- [BlackClaw on ClawHub](https://clawhub.ai/bilalmotiwala/skills/blackswan) <br>
- [BlackSwan MCP service](https://mcp.blackswan.wtf) <br>
- [Flare endpoint](https://mcp.blackswan.wtf/api/flare) <br>
- [Core endpoint](https://mcp.blackswan.wtf/api/core) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API calls, JSON] <br>
**Output Format:** [Markdown guidance with curl command examples and JSON response field descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and contacts BlackSwan's external service for the latest public risk summaries.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
