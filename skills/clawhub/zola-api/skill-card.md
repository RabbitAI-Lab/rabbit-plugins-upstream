## Description:

Query or update Zola wedding-planning data such as vendors, budget, guests, seating, events, RSVPs, registry, gift tracker, inquiries, and wedding website content from a shell with curl against mobile-api.zola.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to query or update their own Zola wedding-planning data directly from a shell, especially when they need curl-based workflows or do not have the Zola MCP server installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential-backed API access can read, change, or delete live Zola account data.

Mitigation: Use the skill only for accounts you control, treat refresh and session tokens like passwords, and require explicit confirmation before POST, PUT, or DELETE commands.

Risk: Tokens or sensitive account data may appear in shell history, shared logs, or raw API error output.

Mitigation: Avoid pasting tokens or raw error bodies into shared channels, redact credentials before logging, and prefer environment variables over inline secrets.

Risk: Some Zola write endpoints replace whole objects, so partial updates can overwrite unrelated fields.

Mitigation: Use the documented read-modify-write workflow: fetch the current record, preserve unmodified fields, and submit the full required body.

## Reference(s):

- [Zola mobile-api endpoints](references/mobile-api-endpoints.md)
- [Zola mobile API](https://mobile-api.zola.com)
- [Zola](https://www.zola.com)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with curl and jq shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided Zola credentials and explicit care around mutating POST, PUT, and DELETE calls.]

## Skill Version(s):

1.8.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
