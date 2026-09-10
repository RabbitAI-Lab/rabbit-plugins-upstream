## Description:

Use when accessing Outlit customer intelligence through the `outlit` CLI, Outlit MCP tools, Pi tools, or @outlit/tools, including customer lookups, users, workspace users, timelines, facts, source evidence, semantic search, revenue, churn, SQL analytics, identity splits, merge suggestions, setup, integrations, or troubleshooting agent access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leo-paz](https://clawhub.ai/user/leo-paz)

### License/Terms of Use:

MIT-0

## Use Case:

External customer-success, sales, support, and operations agents use this skill to retrieve and reason over Outlit customer profiles, timelines, facts, source evidence, search results, revenue signals, churn signals, SQL analytics, integrations, access settings, and identity-merge workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes a curl-to-Bash CLI install command.

Mitigation: Prefer the npm or Homebrew installation path from the release metadata, and install only when the Outlit distribution channel is trusted.

Risk: The skill can guide workspace-changing actions, including access updates, integration changes, activation settings, feature archival, and customer merges.

Mitigation: Require explicit user confirmation before write operations and use least-privilege Outlit API grants or OAuth permissions.

Risk: Customer merge execution is permanent and has no supported undo.

Mitigation: Preview merges first, confirm that records represent the same customer, require the reviewed preview token and stable request ID, and verify merge permission before execution.

Risk: Customer intelligence outputs may expose sensitive customer or workspace data.

Mitigation: Request only needed fields, cite evidence type, and report when data is sparse, stale, partial, truncated, or inconsistent.

## Reference(s):

- [ClawHub Outlit Skill Page](https://clawhub.ai/leo-paz/skills/outlit)
- [Outlit Homepage](https://outlit.ai)
- [Outlit Docs Home](https://docs.outlit.ai/)
- [Outlit CLI Overview](https://docs.outlit.ai/cli/overview)
- [Outlit CLI Commands](https://docs.outlit.ai/cli/commands)
- [Outlit CLI Integrations](https://docs.outlit.ai/cli/integrations)
- [Outlit AI Agent Setup](https://docs.outlit.ai/cli/ai-agents)
- [Outlit Agent Skills](https://docs.outlit.ai/ai-integrations/skills)
- [Outlit MCP Integration](https://docs.outlit.ai/ai-integrations/mcp)
- [Outlit Pi Agents](https://docs.outlit.ai/ai-integrations/pi)
- [Outlit Public Tools API](https://docs.outlit.ai/api-reference/tools)
- [Outlit API Key Validation](https://docs.outlit.ai/api-reference/validation)
- [Outlit Customer Context Graph](https://docs.outlit.ai/concepts/customer-context-graph)
- [Customer Identity and Merge Workflow](references/identity.md)
- [SQL Reference](references/sql-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown guidance with CLI commands, MCP or Pi tool recommendations, JSON-oriented setup notes, and SQL examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require an OUTLIT_API_KEY or OAuth-backed MCP access for live workspace data; agents should keep customer-data access least-privileged.]

## Skill Version(s):

1.0.9 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
