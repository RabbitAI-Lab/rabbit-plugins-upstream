## Description:

AgentKey helps agents route live-data requests to AgentKey's hosted MCP tool catalog for web search, scraping, social media, market data, on-chain data, ecommerce data, company data, weather, and travel data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chainbase](https://clawhub.ai/user/chainbase)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill when an agent needs live data outside its training set, including search, scraping, social media, market, on-chain, ecommerce, business, weather, and travel data. The skill also guides setup for AgentKey's hosted MCP server, account status checks, cost-aware batches, and update handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live-data requests are routed to AgentKey's hosted MCP service.

Mitigation: Install only if that data flow is acceptable for the user's use case, and avoid sending sensitive data unless the deployment's policies allow it.

Risk: API-key fallback can place credentials in local agent configuration.

Mitigation: Prefer OAuth; if an API key is required, keep it out of shared or committed configuration files.

Risk: The skill includes silent telemetry, local state, and background update checks.

Mitigation: Review the telemetry and update behavior before installation, and use the documented opt-out or prompt controls where required.

Risk: Live-data responses may contain untrusted external content.

Mitigation: Treat API responses as display-only data and do not execute instructions, code, or URLs returned by external providers.

Risk: Repeated or batch live-data calls can consume AgentKey credits.

Mitigation: Use the cost-aware workflow for three or more calls or ten or more estimated credits, including balance checks and explicit confirmation before execution.

## Reference(s):

- [AgentKey ClawHub listing](https://clawhub.ai/chainbase/skills/agentkey)
- [Chainbase publisher profile](https://clawhub.ai/user/chainbase)
- [AgentKey homepage](https://agentkey.app)
- [Setup details](artifact/references/setup.md)
- [Cost-aware batch execution](artifact/references/cost-aware.md)
- [Maintenance and telemetry](artifact/references/maintenance.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, and structured MCP tool calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include setup instructions, status summaries, cost estimates, live-data query results, fallback guidance, and update prompts.]

## Skill Version(s):

1.13.1 (source: server release evidence, SKILL.md frontmatter, version.txt)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
