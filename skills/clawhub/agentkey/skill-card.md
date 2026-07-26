## Description: <br>
AgentKey helps agents retrieve live external data through hosted MCP tools for web search, URL scraping, social media, market prices, on-chain data, business data, weather, maps, travel, and other third-party APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chainbase](https://clawhub.ai/user/chainbase) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use AgentKey to connect an agent to a hosted MCP server for real-time lookup, provider discovery, and cost-aware execution of external data calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill routes broad live lookup requests to AgentKey's hosted MCP service, which may send relevant prompts or query details to an external provider. <br>
Mitigation: Install only when AgentKey is an acceptable default external data provider, and review data-sharing expectations before enabling it. <br>
Risk: API-key fallback authentication can expose a bearer token if stored or shared carelessly. <br>
Mitigation: Prefer OAuth registration; if an API key is required, store it as a secret and rotate it if exposed. <br>
Risk: The maintenance flow includes update checks, silent telemetry forwarding, and optional self-update behavior. <br>
Mitigation: Review telemetry and update settings before enabling persistent update options, and use the documented opt-out or confirmation controls where appropriate. <br>
Risk: External API responses may contain untrusted instructions, links, or code. <br>
Mitigation: Treat returned content as display-only data and do not execute instructions, code, or URLs found in responses. <br>


## Reference(s): <br>
- [AgentKey homepage](https://agentkey.app) <br>
- [ClawHub Agentkey listing](https://clawhub.ai/chainbase/skills/agentkey) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to call AgentKey MCP tools; batch execution should include balance checks, cost estimates, and user confirmation.] <br>

## Skill Version(s): <br>
1.12.1 (source: server release evidence, SKILL.md frontmatter, version.txt) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
