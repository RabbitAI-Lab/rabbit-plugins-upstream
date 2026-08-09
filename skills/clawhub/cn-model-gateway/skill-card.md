## Description:

CN Model Gateway is a Python MCP and agent-framework gateway for routing text chat requests to configured Chinese model providers, with provider comparison, health checks, usage tracking, price tracking, and failover.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to expose multiple hosted Chinese text model APIs through MCP tools, resources, prompts, CLI commands, and common agent-framework adapters. It is intended for model selection, provider comparison, failover, and local usage or price monitoring when users supply their own provider API keys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and health checks may be sent to configured third-party model providers.

Mitigation: Use the skill only with providers approved for the data being processed, avoid sensitive prompts in compare or auto-failover mode, and disable failover when provider choice matters.

Risk: Provider API keys may be exposed if stored directly in configuration files.

Mitigation: Prefer the documented environment variables for API keys and keep configuration files containing credentials out of version control.

Risk: Local usage, benchmark, and price databases may reveal provider choices or usage history.

Mitigation: Review and protect the local ~/.cn-model-gateway databases according to the user's data-retention and access-control requirements.

Risk: Model calls can incur provider charges, especially when comparing multiple providers or using failover.

Mitigation: Monitor local usage statistics, configure provider-side budget alerts, and limit compare or benchmark runs in cost-sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/cn-model-gateway)
- [Artifact README](artifact/README.md)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Plain text and JSON-RPC tool/resource responses, with Markdown or code text returned by configured model providers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-configured provider API keys and network access; records local usage, benchmark, and price history in SQLite databases under the user's home directory.]

## Skill Version(s):

1.4.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
