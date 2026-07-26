## Description: <br>
Local Falcon gives AI agents expert guidance on AI visibility, local SEO, Google Business Profile optimization, geo-grid rank tracking, and optional Local Falcon MCP workflows for data-driven analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wearelocalfalcon](https://clawhub.ai/user/wearelocalfalcon) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External marketers, agencies, enterprise local SEO teams, SMB owners, and developers use this skill to interpret local visibility signals, plan AI search and map-pack optimization, and guide Local Falcon MCP-backed analysis when account tools are connected. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional MCP workflow can access Local Falcon account data. <br>
Mitigation: Confirm with the user before reading account data and use only the connected Local Falcon MCP tools needed for the requested analysis. <br>
Risk: Running scans, enabling AI Analysis, or starting campaigns can consume account credits or change monitoring state. <br>
Mitigation: Require explicit user confirmation before running credit-consuming scans, creating or running campaigns, enabling AI Analysis, or changing Falcon Guard monitoring. <br>
Risk: The optional MCP server requires a Local Falcon API key. <br>
Mitigation: Keep the API key in the MCP environment configuration and avoid exposing it in prompts, logs, or generated output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wearelocalfalcon/skills/local-visibility-skill) <br>
- [Local Falcon platform](https://www.localfalcon.com) <br>
- [Local Falcon documentation](https://docs.localfalcon.com) <br>
- [Local Falcon MCP package](https://www.npmjs.com/package/@local-falcon/mcp) <br>
- [Local Falcon visibility skill package](https://www.npmjs.com/package/@local-falcon/local-visibility-skill) <br>
- [Metrics glossary](references/metrics-glossary.md) <br>
- [AI platforms deep dive](references/ai-platforms.md) <br>
- [MCP workflows](references/mcp-workflows.md) <br>
- [Prompt templates](references/prompt-templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown text with occasional shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May provide data-driven recommendations when Local Falcon MCP tools are connected; otherwise provides best-practice guidance.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
