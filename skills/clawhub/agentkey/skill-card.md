## Description:

AgentKey routes live-data requests, including web search, URL scraping, news, social media, market prices, weather, maps, travel, and third-party API calls, through a dynamic hosted MCP tool catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chainbase](https://clawhub.ai/user/chainbase)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use AgentKey to discover and execute hosted MCP tools for live-data and third-party API tasks that are outside an agent's training data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes broad live-data requests through AgentKey's hosted MCP service.

Mitigation: Install and use it only when routing those requests through the hosted service is acceptable for the user's data and policy requirements.

Risk: Server security evidence flags silent telemetry and local state used for update, snooze, disable, and telemetry controls.

Mitigation: Review the telemetry and update behavior in the maintenance reference before deployment, and configure opt-out or update controls where required.

Risk: The skill strongly redirects broad requests away from built-in web and search tools.

Mitigation: Apply local tool-use policy before enabling the skill, and keep built-in or approved alternatives available where required.

Risk: API responses are untrusted external data.

Mitigation: Treat returned content as display-only data and do not execute instructions, code, or URLs from API responses.

Risk: Batch use can consume AgentKey credits.

Mitigation: Use the documented cost-aware workflow for three or more calls or ten or more estimated credits, including balance checks and explicit confirmation.

## Reference(s):

- [AgentKey homepage](https://agentkey.app)
- [AgentKey ClawHub skill page](https://clawhub.ai/chainbase/skills/agentkey)
- [Setup details](references/setup.md)
- [Cost-aware batch execution](references/cost-aware.md)
- [Maintenance and telemetry](references/maintenance.md)
- [Skill meta protocol](https://github.com/chainbase-labs/agentkey/blob/main/protocol/skill-meta-v1.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Text]

**Output Format:** [Markdown with inline shell commands and structured tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include setup instructions, cost estimates, live-data results, and status or error guidance depending on the requested task.]

## Skill Version(s):

1.13.0 (source: SKILL.md frontmatter, version.txt, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
