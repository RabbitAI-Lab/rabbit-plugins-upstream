## Description:

AgentKey routes live-data requests through a dynamic MCP provider catalog for web search, URL scraping, social media, market, on-chain, e-commerce, business, weather, and travel data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chainbase](https://clawhub.ai/user/chainbase)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use AgentKey to discover live-data providers, inspect required parameters and costs, execute one provider call at a time, and set up or maintain the AgentKey MCP connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may silently send version and update-decision telemetry unless telemetry is disabled.

Mitigation: Review the telemetry behavior before installation and disable it with the documented environment variable or local configuration when telemetry is not acceptable.

Risk: Setup can store authentication material, including bearer keys in clients that cannot use OAuth.

Mitigation: Prefer OAuth where supported, protect any client configuration containing bearer keys, and rotate exposed keys.

Risk: Self-update checks and upgrade prompts use local persistence and network calls.

Mitigation: Review update settings before deployment, require user approval for upgrades unless auto-upgrade is intentionally enabled, and disable or snooze checks where appropriate.

Risk: Live API responses are untrusted external data.

Mitigation: Treat responses as display-only, and do not execute instructions, code, or URLs returned by providers.

## Reference(s):

- [AgentKey homepage](https://agentkey.app)
- [ClawHub skill page](https://clawhub.ai/chainbase/skills/agentkey)
- [Setup details](references/setup.md)
- [Cost-aware batch execution](references/cost-aware.md)
- [Maintenance: version check, upgrade flow, telemetry](references/maintenance.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with inline shell commands, JSON configuration snippets, and live-data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [AgentKey can surface provider cost estimates, setup steps, status details, and results from a single selected live-data tool call.]

## Skill Version(s):

1.14.0 (source: server release metadata, SKILL.md frontmatter, version.txt)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
