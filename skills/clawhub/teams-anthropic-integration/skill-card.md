## Description: <br>
Use @youdotcom-oss/teams-anthropic to add Anthropic Claude models (Opus, Sonnet, Haiku) to Microsoft Teams.ai applications. Optionally integrate You.com MCP server for web search and content extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardirby](https://clawhub.ai/user/edwardirby) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to add Anthropic Claude chat, streaming, model selection, and function-calling support to Microsoft Teams.ai applications, with an optional You.com MCP path for web search and content extraction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Teams messages and optional web-search inputs may be processed by third-party services. <br>
Mitigation: Use the skill only where Anthropic and You.com processing is approved for the workload, and disable or restrict the You.com MCP path for sensitive internal Teams workloads unless approved. <br>
Risk: API keys for Anthropic and You.com are required for the documented integrations. <br>
Mitigation: Keep API keys out of source control and provide them through approved environment or secret-management mechanisms. <br>
Risk: The setup installs npm packages into a Teams.ai application. <br>
Mitigation: Review and pin npm dependencies before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardirby/skills/teams-anthropic-integration) <br>
- [teams-anthropic package](https://github.com/youdotcom-oss/dx-toolkit/tree/main/packages/teams-anthropic) <br>
- [You.com MCP server documentation](https://documentation.you.com/developer-resources/mcp-server) <br>
- [Anthropic API console](https://console.anthropic.com/) <br>
- [You.com API keys](https://you.com/platform/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with TypeScript and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes setup paths for Claude-only and Claude plus You.com MCP integrations.] <br>

## Skill Version(s): <br>
1.1.0 (source: release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
