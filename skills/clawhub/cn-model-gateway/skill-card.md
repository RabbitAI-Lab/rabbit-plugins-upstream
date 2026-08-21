## Description:

CN Model Gateway is a Python MCP server that routes agent requests to ten China-based model providers through JSON-RPC tools, resources, prompts, CLI commands, and framework adapters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect MCP-compatible and related agent frameworks to configured Chinese model providers, compare provider responses, describe images, inspect provider health, and review local usage statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, image inputs, and benchmark questions may be sent to configured third-party model providers.

Mitigation: Use the skill only with approved providers for the data involved, specify a single provider for sensitive work, and disable failover when provider routing must be controlled.

Risk: API keys and provider credentials are required for model access.

Mitigation: Prefer environment variables for API keys and protect any config.json files that contain credentials.

Risk: Multi-provider comparison and automatic failover can increase cost or route requests to a backup provider.

Mitigation: Review provider selection before use, monitor usage statistics, and disable failover or comparison when cost or routing constraints apply.

Risk: Local usage data is stored in the user's environment.

Mitigation: Protect the ~/.cn-model-gateway local database and apply normal endpoint security controls for workstations or shared systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/cn-model-gateway)
- [Skill definition](artifact/SKILL.md)
- [README](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON-RPC responses, Markdown guidance, Python code examples, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce model responses, provider status, usage statistics, benchmark summaries, image descriptions, and tool-call metadata.]

## Skill Version(s):

1.5.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
