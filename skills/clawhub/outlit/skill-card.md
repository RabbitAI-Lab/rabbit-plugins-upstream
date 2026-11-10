## Description:

Use when accessing Outlit customer intelligence through the `outlit` CLI, Outlit MCP tools, Pi tools, or @outlit/tools, including customer lookups, users, workspace users, timelines, facts, source evidence, semantic search, revenue, churn, SQL analytics, identity splits, merge suggestions, setup, integrations, or troubleshooting agent access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leo-paz](https://clawhub.ai/user/leo-paz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and customer-facing teams use Outlit to retrieve and analyze customer context for onboarding, adoption, retention, renewal, and expansion. The skill guides account research, evidence-backed summaries, customer analytics, and explicitly requested workspace setup or changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer command pipes an unpinned remote script into Bash.

Mitigation: Review the installer from a trusted source before running it, or use the documented npm or Homebrew package installation options.

Risk: Customer merge actions can change records beyond the intended match.

Mitigation: Only proceed when explicitly requested and the records are certainly the same customer; review the merge preview and affected records before execution.

## Reference(s):

- [Outlit website](https://outlit.ai)
- [Outlit documentation](https://docs.outlit.ai/)
- [Outlit documentation index](https://docs.outlit.ai/llms.txt)
- [Customer identity and merge workflow](references/identity.md)
- [SQL reference](references/sql-reference.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, SQL queries, Shell commands, Configuration instructions]

**Output Format:** [Markdown or text, with SQL and shell command examples when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include citations to customer records, sources, facts, timelines, and SQL results.]

## Skill Version(s):

1.0.12 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
