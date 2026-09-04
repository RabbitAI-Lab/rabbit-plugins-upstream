## Description:

Query FreshBooks invoices, clients, estimates, payments, expenses, projects, and time tracking from a shell with curl and a rotating OAuth token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to set up OAuth-backed shell access to FreshBooks and run curl and jq recipes for accounting, payments, projects, and time-tracking workflows without installing the FreshBooks MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can execute FreshBooks API writes for accounting records, payments, projects, and time entries.

Mitigation: Require explicit confirmation before running mutation recipes, prefer non-production data for testing, and re-read changed records to confirm the intended result.

Risk: OAuth client secrets, refresh tokens, and access tokens may be available to shell commands or appear in terminal output, logs, or shared sessions.

Mitigation: Load credentials from a private secrets file, keep token state files permission-restricted, and avoid copying token output into logs or shared terminals.

Risk: FreshBooks refresh tokens rotate on use, so competing tools or failed persistence can invalidate the active token.

Mitigation: Use a single token state file owner for this helper, avoid sharing state with the FreshBooks MCP server, and re-run the bootstrap flow if a refresh token has already been spent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/freshbooks-mcp)
- [FreshBooks developer registration](https://my.freshbooks.com/#/developer)
- [FreshBooks curl recipes](references/recipes.md)
- [FreshBooks OAuth bootstrap helper](references/fb-bootstrap.mjs)
- [FreshBooks token helper](references/fb-token.sh)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with shell commands, jq filters, and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces executable curl-based FreshBooks workflows and OAuth setup guidance; executed commands can perform live reads and writes against the connected FreshBooks account.]

## Skill Version(s):

0.5.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
