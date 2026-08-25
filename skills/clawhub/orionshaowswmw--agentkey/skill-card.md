## Description:

Secure API key management and rotation for AI agents, including encrypted storage, rotation, auditing, and centralized management across multiple providers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to set up and manage API credentials used by agents, including local keystore handling, provider testing or rotation workflows, and AgentKey MCP configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles API keys and bearer-token configuration while connecting to the hosted AgentKey MCP service.

Mitigation: Use it only in environments where this external service is approved, prefer OAuth where supported, and protect local MCP configuration files containing bearer tokens.

Risk: Provider key tests or rotations can contact external provider APIs.

Mitigation: Run only the provider workflows the user explicitly selects, use least-privilege credentials, and avoid these workflows in strict no-egress environments.

Risk: Update checks, telemetry forwarding, persistence files, or upgrade commands may be inappropriate for restricted credential-handling environments.

Mitigation: Review the update and telemetry behavior before installation, disable or avoid it where policy requires, and require explicit approval before running upgrade commands.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/orionshaowswmw/skills/agentkey)
- [Setup details](references/setup.md)
- [Cost-aware batch execution](references/cost-aware.md)
- [Maintenance and telemetry behavior](references/maintenance.md)
- [AgentKey hosted MCP endpoint](https://api.agentkey.app/v1/mcp)
- [AgentKey console](https://console.agentkey.app/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool invocation guidance; secrets should not be printed or logged.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
