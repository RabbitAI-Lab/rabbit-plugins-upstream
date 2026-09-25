## Description:

Query FreshBooks invoices, clients, estimates, payments, expenses, projects, and time tracking from a shell with curl and a rotating OAuth token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to query FreshBooks data and prepare curl-based API workflows without running the FreshBooks MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores OAuth tokens and can access real FreshBooks business data.

Mitigation: Protect the local token state file and secrets file, and prefer a test account or read-only workflows where possible.

Risk: Some commands can change live accounting records, including invoices, estimates, payments, and time entries.

Mitigation: Require explicit user approval before running any POST, PUT, DELETE, email, payment, invoice, estimate, or time-entry command.

Risk: FreshBooks refresh tokens rotate and can be invalidated if multiple tools share the same token state.

Mitigation: Use a dedicated state file for this skill and avoid pointing multiple tools at the same rotating-token store.

## Reference(s):

- [FreshBooks Developer Portal](https://my.freshbooks.com/#/developer)
- [FreshBooks curl recipes](references/recipes.md)
- [FreshBooks OAuth bootstrap helper](references/fb-bootstrap.mjs)
- [FreshBooks token helper](references/fb-token.sh)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/freshbooks-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces curl commands and helper usage patterns for FreshBooks API calls.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
