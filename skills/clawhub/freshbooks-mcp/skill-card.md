## Description:

Query FreshBooks invoices, clients, estimates, payments, expenses, projects, and time tracking from a shell with curl and a rotating OAuth token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to get FreshBooks data or prepare FreshBooks API calls from a shell when they do not want to run an MCP server. It provides OAuth setup guidance, reusable curl helpers, jq recipes, and request examples for common accounting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad live FreshBooks accounting read/write authority can affect production invoices, clients, payments, estimates, expenses, projects, and time entries.

Mitigation: Require explicit human confirmation before running POST, PUT, email, payment, estimate, or soft-delete commands against production data.

Risk: FreshBooks OAuth refresh tokens are sensitive, single-use, and rotate; losing or sharing the active state can lock out the integration.

Mitigation: Keep tokens out of logs and shared terminals, store the state file with restricted permissions, and avoid pointing multiple tools at the same rotating token state.

Risk: Some recipe paths are marked unverified and successful HTTP responses may not prove a write persisted.

Mitigation: Prefer a test account for new write flows, confirm endpoint behavior before production use, and re-read changed records after writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/freshbooks-mcp)
- [FreshBooks developer portal](https://my.freshbooks.com/#/developer)
- [FreshBooks curl recipes](references/recipes.md)
- [FreshBooks OAuth bootstrap helper](references/fb-bootstrap.mjs)
- [FreshBooks token helper](references/fb-token.sh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, jq filters, and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided FreshBooks OAuth credentials and may generate commands that read or modify live accounting data.]

## Skill Version(s):

0.5.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
