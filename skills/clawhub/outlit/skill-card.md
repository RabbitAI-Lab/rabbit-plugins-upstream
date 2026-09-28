## Description:

Guides agents in using Outlit tools and the CLI to investigate customer accounts, trace supporting evidence, run analytics, and manage explicitly requested workspace changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leo-paz](https://clawhub.ai/user/leo-paz)

### License/Terms of Use:

MIT-0

## Use Case:

Customer-success teams and their agents use Outlit to research accounts, identify retention or expansion signals, and explain findings with customer records and source evidence. Authorized users can also request workspace setup and account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running a downloaded installer directly in a shell could execute unreviewed code.

Mitigation: Prefer the documented npm or Homebrew installation options; use the shell installer only after independently verifying and trusting it.

Risk: Outlit credentials and customer data may be exposed if access is overly broad or secrets are shared in chat.

Mitigation: Use least-privilege credentials and do not paste API keys or integration secrets into chat.

Risk: Workspace access changes, integration setup, or customer merges can have significant consequences.

Mitigation: Review proposed changes and require explicit user authorization before applying them; preview and confirm customer merges.

## Reference(s):

- [Outlit documentation index](https://docs.outlit.ai/llms.txt)
- [Outlit documentation](https://docs.outlit.ai/)
- [Outlit homepage](https://outlit.ai)
- [Customer identity and merge workflow](references/identity.md)
- [SQL reference](references/sql-reference.md)
- [ClawHub skill listing](https://clawhub.ai/leo-paz/skills/outlit)

## Skill Output:

**Output Type(s):** [Text, Markdown, SQL queries, Shell commands, Configuration guidance]

**Output Format:** [Markdown responses with source references, commands, or SQL where relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Customer conclusions should distinguish observed evidence from interpretation.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
