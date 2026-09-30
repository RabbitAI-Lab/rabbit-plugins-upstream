## Description:

Helps agents query and update FreshBooks accounting and time-tracking data through shell commands using OAuth authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve FreshBooks invoices, clients, expenses, projects, and time entries or perform authorized accounting updates from a shell without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can create or change live invoices, clients, payments, estimates, emails, and time entries despite the query-focused description.

Mitigation: Review write commands before execution and use a least-privileged FreshBooks app and account where possible.

Risk: Local OAuth credentials and rotating refresh tokens can be exposed or invalidated by competing access to the same token state.

Mitigation: Keep tokens out of logs and command output, protect the local state file, and do not share it between tools.

## Reference(s):

- [FreshBooks developer portal](https://my.freshbooks.com/#/developer)
- [FreshBooks curl recipes](references/recipes.md)
- [OAuth bootstrap helper](references/fb-bootstrap.mjs)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/freshbooks-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.1.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
