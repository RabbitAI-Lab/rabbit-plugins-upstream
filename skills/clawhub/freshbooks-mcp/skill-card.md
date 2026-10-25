## Description:

Helps agents access FreshBooks invoices, clients, estimates, payments, expenses, projects, and time tracking from a shell using curl and rotating OAuth tokens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve FreshBooks accounting and project data without running the MCP server. Its shell helper can also submit changes to live accounting records when explicitly authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The request helper supports writes that can change live FreshBooks accounting data.

Mitigation: Review and explicitly approve every POST, PUT, or delete-style command before execution; re-read affected records to confirm changes.

Risk: OAuth credentials and token state can expose account access if printed, logged, or shared.

Mitigation: Protect the token state file and bootstrap output, and avoid running credential-bearing commands in shared logs or CI.

Risk: Reusing a rotating refresh-token state file across tools can invalidate account access.

Mitigation: Keep a separate token state file for this helper and do not run concurrent tools against it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/freshbooks-mcp)
- [FreshBooks developer portal](https://my.freshbooks.com/#/developer)
- [FreshBooks curl recipes](references/recipes.md)
- [OAuth bootstrap helper](references/fb-bootstrap.mjs)
- [Token and API request helper](references/fb-token.sh)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell examples and FreshBooks data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may retrieve sensitive account data or modify live records.]

## Skill Version(s):

1.2.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
