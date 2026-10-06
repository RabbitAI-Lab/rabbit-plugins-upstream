## Description:

Helps agents query FreshBooks invoices, clients, estimates, payments, expenses, projects, and time entries from a shell using curl and rotating OAuth credentials, without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve FreshBooks accounting and project data in shell workflows without installing the FreshBooks MCP server. Its commands can also change account data when given write options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth credentials and rotating refresh tokens may be exposed or lost if setup is logged, the token state file is shared, or concurrent tools reuse it.

Mitigation: Keep credentials and the token state file private, avoid setup in logged CI or shared terminals, and use a separate state file per tool.

Risk: The shell helper can perform live financial and accounting writes, including updates and deletes, despite its query-oriented description.

Mitigation: Use an app and account with only the necessary permissions; require explicit user approval before POST, PUT, DELETE, or vis_state changes, and re-read records to confirm writes.

## Reference(s):

- [FreshBooks developer portal](https://my.freshbooks.com/#/developer)
- [FreshBooks curl recipes](references/recipes.md)
- [FreshBooks token helper](references/fb-token.sh)
- [FreshBooks bootstrap helper](references/fb-bootstrap.mjs)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses FreshBooks OAuth credentials and requires a writable private token state file.]

## Skill Version(s):

1.1.5 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
