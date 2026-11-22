## Description:

Use when accessing Outlit customer intelligence through the `outlit` CLI, Outlit MCP tools, Pi tools, or @outlit/tools, including customer lookups, users, workspace users, timelines, facts, source evidence, semantic search, revenue, churn, SQL analytics, identity splits, merge suggestions, setup, integrations, or troubleshooting agent access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leo-paz](https://clawhub.ai/user/leo-paz)

### License/Terms of Use:

MIT-0

## Use Case:

Customer success, sales, and product teams use Outlit-enabled agents to investigate customer activity and account health, answer questions with source evidence, and run custom analytics. Developers and workspace admins can also use it to configure integrations and manage customer or workspace settings when explicitly asked.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious with medium confidence, citing its recommendation to run an unverified remote installer and reports of customer-merge capability beyond the described purpose. The scan was partial, so its evidence is incomplete.

Mitigation: Follow ClawScan's guidance to avoid installation until the remote installer is verified and the merge capability is clearly understood. Execute a merge only with explicit authorization and certainty that both records are the same customer, after reviewing the preview.

## Reference(s):

- [Outlit documentation](https://docs.outlit.ai/)
- [Outlit documentation index](https://docs.outlit.ai/llms.txt)
- [Outlit product site](https://outlit.ai)
- [ClawHub skill page](https://clawhub.ai/leo-paz/skills/outlit)
- [Identity and merge workflow](references/identity.md)
- [SQL reference](references/sql-reference.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, SQL queries, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown or plain text, with JSON, SQL, or shell examples when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers may cite customer records and source evidence; available detail depends on connected tools, workspace data, and permissions.]

## Skill Version(s):

1.0.15 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
