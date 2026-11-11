## Description:

Use when accessing Outlit customer intelligence through the `outlit` CLI, Outlit MCP tools, Pi tools, or @outlit/tools, including customer lookups, users, workspace users, timelines, facts, source evidence, semantic search, revenue, churn, SQL analytics, identity splits, merge suggestions, setup, integrations, or troubleshooting agent access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leo-paz](https://clawhub.ai/user/leo-paz)

### License/Terms of Use:

MIT-0

## Use Case:

Customer success teams and developers use this skill to retrieve and analyze customer context from an Outlit workspace, trace findings to source evidence, and manage workspace capabilities when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marked the release suspicious and recommends DO_NOT_INSTALL, citing an unverified remote installer and customer-record merge capability.

Mitigation: Follow the scanner recommendation until the installer and merge capability have been reviewed. Before any merge, verify the records are the same customer, review the preview, and require explicit authorization and the needed permission.

## Reference(s):

- [Outlit documentation](https://docs.outlit.ai/)
- [Outlit documentation index](https://docs.outlit.ai/llms.txt)
- [Identity and merge workflow](references/identity.md)
- [SQL reference](references/sql-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Shell commands, Configuration instructions]

**Output Format:** [Text or Markdown with customer research, source citations, analytics guidance, and command or configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include customer data summaries and read-only SQL guidance; workspace changes require explicit user authorization.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
