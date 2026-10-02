## Description:

Guides shell-based FreshBooks API access for invoices, clients, payments, expenses, projects, and time tracking using curl and rotating OAuth credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and FreshBooks users use this skill to query accounting and project data from a shell without running the FreshBooks MCP server, and to prepare API requests when changes are needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests can change live accounting records, including invoices, clients, and payments.

Mitigation: Review POST and PUT commands before execution, avoid casual use against production data, and re-read records to confirm changes.

Risk: OAuth tokens are printed during setup and grant the configured app's FreshBooks authority.

Mitigation: Keep tokens out of logs and shared messages, and restrict access to credential and token-state files.

Risk: FreshBooks refresh tokens rotate after one use; competing users of a token-state file can interrupt access.

Mitigation: Use the provided token helper with a dedicated state file and avoid concurrent access to that file.

## Reference(s):

- [FreshBooks MCP ClawHub release](https://clawhub.ai/chrischall/skills/freshbooks-mcp)
- [FreshBooks developer portal](https://my.freshbooks.com/#/developer)
- [FreshBooks curl recipes](references/recipes.md)
- [FreshBooks OAuth bootstrap helper](references/fb-bootstrap.mjs)
- [FreshBooks token and curl helper](references/fb-token.sh)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can query or change live FreshBooks accounting data.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
