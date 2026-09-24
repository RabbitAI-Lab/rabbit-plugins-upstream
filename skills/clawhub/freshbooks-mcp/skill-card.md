## Description:

Query FreshBooks invoices, clients, estimates, payments, expenses, projects, and time tracking from a shell with curl and a rotating OAuth token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to prepare authenticated FreshBooks shell commands, bootstrap OAuth credentials, resolve FreshBooks account identifiers, and inspect or update accounting, project, payment, expense, and time-tracking data when the MCP server is not installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can produce authenticated FreshBooks write commands that affect live accounting records despite being framed primarily as a query helper.

Mitigation: Review every POST, PUT, email, payment, or delete-style command before execution, and re-read changed records to confirm the intended result.

Risk: FreshBooks client secrets, refresh tokens, and state files can grant broad account access if exposed.

Mitigation: Store credentials outside logs and shell traces, protect the token state file, and avoid sharing the same rotating-token state file between tools.

Risk: FreshBooks refresh tokens rotate on use, so two writers or a failed persistence step can invalidate access.

Mitigation: Use the provided token helper for refreshes, keep one writer per state file, and re-run the browser bootstrap if the refresh token has already been spent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/freshbooks-mcp)
- [FreshBooks developer portal](https://my.freshbooks.com/#/developer)
- [FreshBooks curl recipes](references/recipes.md)
- [FreshBooks OAuth bootstrap helper](references/fb-bootstrap.mjs)
- [FreshBooks rotating token helper](references/fb-token.sh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JavaScript helper usage, jq filters, and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce authenticated FreshBooks API calls; write examples can change live accounting records or send customer-facing email when executed.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
