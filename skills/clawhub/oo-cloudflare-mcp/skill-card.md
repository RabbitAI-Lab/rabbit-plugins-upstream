## Description:

Cloudflare MCP helps agents search Cloudflare developer documentation, discover API endpoints, and run Cloudflare MCP actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to search Cloudflare documentation, discover Cloudflare API endpoints, inspect live connector schemas, and run Cloudflare MCP actions through the oo CLI without handling raw Cloudflare tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The execute action may call Cloudflare API endpoints that change resources when the live schema and payload are not clearly read-only.

Mitigation: Inspect the live action schema before constructing payloads, confirm the exact effect with the user for write or destructive actions, and use Cloudflare account scopes that match the task.

Risk: The skill operates through an OOMOL-connected Cloudflare account with server-side credential handling.

Mitigation: Install and use it only for accounts where OOMOL-mediated Cloudflare MCP actions are acceptable, and review production or administrative account access before use.

## Reference(s):

- [Cloudflare MCP homepage](https://github.com/cloudflare/mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cloudflare-mcp)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema inspection before constructing payloads.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
