## Description:

Query or update Zola wedding-planning data from a shell with curl against mobile-api.zola.com without running the zola-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect or maintain authenticated Zola wedding-planning data directly through mobile-api.zola.com from a shell. It is useful when the MCP server is unavailable or when a script needs direct curl and jq recipes for Zola vendors, budget, guests, seating, events, RSVPs, registry, gift tracker, inquiries, or wedding website data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a long-lived Zola refresh token that can grant account access if exposed.

Mitigation: Treat ZOLA_REFRESH_TOKEN like a password; avoid putting it in chat, shell history, logs, or screenshots, and rotate it if exposure is suspected.

Risk: The skill includes live update, unbook, remove, and delete API commands for Zola account data.

Mitigation: Before any mutating command, require the agent to show the resolved account context, target IDs, and exact operation, then obtain explicit confirmation.

Risk: Raw non-2xx error bodies may contain sensitive request or session details.

Mitigation: Review error responses locally and redact secrets before sharing them outside the trusted execution environment.

## Reference(s):

- [Zola mobile-api endpoints](references/mobile-api-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zola-api)
- [Zola](https://www.zola.com)
- [Zola mobile API](https://mobile-api.zola.com)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated Zola refresh token and session-specific request headers.]

## Skill Version(s):

1.12.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
