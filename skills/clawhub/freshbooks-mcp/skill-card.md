## Description:

Guides shell-based FreshBooks API requests with OAuth token refresh for accounting and project data, including read and write operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and accounting teams use this skill to query FreshBooks invoices, clients, payments, expenses, projects, and time entries from a shell without running an MCP server. Its request helpers also permit changes to live accounting records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated requests can create or change live accounting records and email clients.

Mitigation: Use a least-privileged FreshBooks app and account; require human review before non-GET or client-emailing actions.

Risk: OAuth tokens and command output may expose sensitive accounting access or data.

Mitigation: Keep the token state file private and avoid logging tokens or command output.

Risk: Concurrent use or lost refresh-token state can interrupt account access.

Mitigation: Avoid sharing a token state file between tools and preserve each rotated token before reuse.

## Reference(s):

- [FreshBooks developer portal](https://my.freshbooks.com/#/developer)
- [FreshBooks curl recipes](references/recipes.md)
- [FreshBooks OAuth bootstrap helper](references/fb-bootstrap.mjs)
- [FreshBooks token and request helpers](references/fb-token.sh)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/freshbooks-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read or change live FreshBooks data.]

## Skill Version(s):

1.1.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
