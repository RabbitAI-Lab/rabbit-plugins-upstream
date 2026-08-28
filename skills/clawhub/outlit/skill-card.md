## Description:

Outlit helps agents access customer intelligence through the Outlit CLI, MCP tools, Pi tools, and @outlit/tools for customer lookups, timelines, facts, evidence, semantic search, revenue, churn, SQL analytics, setup, integrations, and access troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leo-paz](https://clawhub.ai/user/leo-paz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, customer-success teams, and agents use this skill to retrieve source-backed customer context, troubleshoot Outlit access, and run read-only analytics across Outlit workspace data. The skill also guides explicit user-requested setup and configuration actions for integrations, access, activation, destinations, settings, and features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide access to Outlit workspace customer data.

Mitigation: Install it only when the agent should use Outlit data, review API key or OAuth grants, and prefer read-only access when possible.

Risk: Some guided operations can change owners, access, integrations, destinations, activation, settings, or features.

Mitigation: Require explicit user confirmation before any workspace mutation or setup action.

Risk: SQL analytics can produce misleading results if schema, time range, or limits are omitted.

Mitigation: Inspect schema first, keep SQL read-only, add time filters for activity queries, and use LIMIT.

Risk: Integration setup can involve provider credentials.

Mitigation: Do not ask users to paste provider secrets into chat, model-visible tool calls, command arguments, logs, shell history, or process listings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/leo-paz/skills/outlit)
- [Outlit homepage](https://outlit.ai)
- [Outlit docs](https://docs.outlit.ai/)
- [CLI overview](https://docs.outlit.ai/cli/overview)
- [AI agent setup](https://docs.outlit.ai/cli/ai-agents)
- [MCP integration](https://docs.outlit.ai/ai-integrations/mcp)
- [Public tools API](https://docs.outlit.ai/api-reference/tools)
- [Customer context graph](https://docs.outlit.ai/concepts/customer-context-graph)
- [SQL Reference](references/sql-reference.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, SQL, API/tool calls]

**Output Format:** [Markdown guidance with command examples, SQL snippets, and tool-selection recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires appropriate Outlit CLI, MCP, Pi, or @outlit/tools access and an OUTLIT_API_KEY or OAuth session for workspace data.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
