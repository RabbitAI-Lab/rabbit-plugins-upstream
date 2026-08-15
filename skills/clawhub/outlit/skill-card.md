## Description:

Use when accessing Outlit customer intelligence through the `outlit` CLI, Outlit MCP tools, Pi tools, or @outlit/tools, including customer lookups, users, workspace users, timelines, facts, source evidence, semantic search, revenue, churn, SQL analytics, setup, integrations, or troubleshooting agent access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leo-paz](https://clawhub.ai/user/leo-paz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and customer-facing teams use this skill to query Outlit-connected customer intelligence, inspect timelines and source evidence, run read-only SQL analytics, and guide setup or troubleshooting for agent access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help agents query Outlit-connected customer and revenue data.

Mitigation: Install it only for agents authorized to access that data and keep OUTLIT_API_KEY scoped and protected.

Risk: The skill includes a remote shell install shortcut.

Mitigation: Prefer the npm or Homebrew install path, or review the installer before using the shell shortcut.

Risk: Integration setup can involve third-party credentials and secrets.

Mitigation: Review credential prompts and configuration before submitting secrets.

Risk: Customer ownership and access actions can change collaboration permissions.

Mitigation: Use ownership or access changes only after an explicit user request and confirm the intended customer and permission change.

## Reference(s):

- [Outlit homepage](https://outlit.ai)
- [Outlit documentation](https://docs.outlit.ai/)
- [Outlit CLI overview](https://docs.outlit.ai/cli/overview)
- [Outlit CLI commands](https://docs.outlit.ai/cli/commands)
- [Outlit CLI integrations](https://docs.outlit.ai/cli/integrations)
- [Outlit AI agent setup](https://docs.outlit.ai/cli/ai-agents)
- [Outlit agent skills](https://docs.outlit.ai/ai-integrations/skills)
- [Outlit MCP integration](https://docs.outlit.ai/ai-integrations/mcp)
- [Outlit Pi agents](https://docs.outlit.ai/ai-integrations/pi)
- [Outlit public tools API](https://docs.outlit.ai/api-reference/tools)
- [Outlit customer context graph](https://docs.outlit.ai/concepts/customer-context-graph)
- [SQL Reference](references/sql-reference.md)
- [ClawHub skill page](https://clawhub.ai/leo-paz/skills/outlit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, SQL guidance]

**Output Format:** [Markdown guidance with inline shell commands, SQL snippets, and JSON-oriented CLI/tool call usage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should distinguish evidence from interpretation and cite the evidence kind when using customer, user, workspace-user, timeline, fact, search, source, or SQL results.]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
