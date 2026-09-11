## Description:

Use when accessing Outlit customer intelligence through the `outlit` CLI, Outlit MCP tools, Pi tools, or @outlit/tools, including customer lookups, users, workspace users, timelines, facts, source evidence, semantic search, revenue, churn, SQL analytics, identity splits, merge suggestions, setup, integrations, or troubleshooting agent access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leo-paz](https://clawhub.ai/user/leo-paz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and customer-facing teams use this skill to retrieve Outlit customer context for onboarding, adoption, retention, renewal, expansion, analytics, identity diagnostics, integrations, and workspace troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include an unverified remote installer piped into Bash.

Mitigation: Prefer the npm or Homebrew package-manager install options; use the curl-to-bash installer only when the publisher is trusted and remote-code execution is acceptable.

Risk: Outlit access can expose sensitive customer intelligence and, with explicit grants, modify workspace access, settings, integrations, destinations, activation, features, and customer identity state.

Mitigation: Review API key grants, use least-privileged credentials, and perform write operations only after explicit user authorization.

Risk: Customer merge execution is destructive and has no supported undo.

Mitigation: Diagnose and preview first, require certainty that records represent the same customer, require explicit execution authorization, and use the reviewed preview token and stable request ID.

Risk: Customer context can be sparse, stale, truncated, partial, or inconsistent.

Mitigation: Report data-quality limits with confidence, cite the evidence kind used, and avoid treating readiness or candidate identity signals as proof of complete data.

## Reference(s):

- [Outlit homepage](https://outlit.ai)
- [Outlit docs home](https://docs.outlit.ai/)
- [CLI overview](https://docs.outlit.ai/cli/overview)
- [CLI commands](https://docs.outlit.ai/cli/commands)
- [CLI integrations](https://docs.outlit.ai/cli/integrations)
- [AI agent setup](https://docs.outlit.ai/cli/ai-agents)
- [Agent skills](https://docs.outlit.ai/ai-integrations/skills)
- [MCP integration](https://docs.outlit.ai/ai-integrations/mcp)
- [Pi agents](https://docs.outlit.ai/ai-integrations/pi)
- [Public tools API](https://docs.outlit.ai/api-reference/tools)
- [API key validation](https://docs.outlit.ai/api-reference/validation)
- [Customer context graph](https://docs.outlit.ai/concepts/customer-context-graph)
- [Customer identity and merge workflow](references/identity.md)
- [SQL Reference](references/sql-reference.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, SQL queries, tool-use instructions]

**Output Format:** [Markdown guidance with inline shell commands, SQL examples, and JSON-oriented CLI instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing instructions for selecting Outlit interfaces, citing customer evidence, handling permissions, and avoiding unsafe write operations.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
