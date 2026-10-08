## Description:

Helps agents query FreshBooks invoices, clients, estimates, payments, expenses, projects, and time entries from a shell using curl and rotating OAuth tokens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and finance operators use this skill to retrieve FreshBooks records from shell scripts without running an MCP server. Its request examples also support creating or updating records when the user approves those actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: POST and PUT requests can alter live accounting records, record payments, or trigger customer-facing actions.

Mitigation: Require explicit approval before non-GET requests; try write recipes in a sandbox or test account first, then re-read records to confirm changes.

Risk: Persistent OAuth token state can expose account access or become unusable if rotating refresh tokens are mishandled.

Mitigation: Keep the token state file private, use the bundled rotation helper, and do not share one state file between tools.

## Reference(s):

- [FreshBooks curl recipes](references/recipes.md)
- [FreshBooks token helper](references/fb-token.sh)
- [FreshBooks OAuth bootstrap](references/fb-bootstrap.mjs)
- [FreshBooks developer portal](https://my.freshbooks.com/#/developer)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/freshbooks-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [FreshBooks API responses are JSON.]

## Skill Version(s):

1.2.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
