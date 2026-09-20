## Description:

Query or update Zola wedding-planning data, including vendors, budget, guests, seating, events, RSVPs, registry, gift tracker, inquiries, and wedding website content, from a shell with curl against mobile-api.zola.com instead of running the zola-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect or modify live Zola wedding-planning data directly through documented curl and jq workflows. It is useful when the Zola MCP server is unavailable or when a script needs direct mobile API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a long-lived Zola account refresh token and short-lived bearer session tokens.

Mitigation: Treat tokens like account passwords, keep them in environment variables or a secret store, and avoid pasting tokens into logs, chat, or public error reports.

Risk: The skill includes PUT, POST, and DELETE recipes that can modify or remove live wedding-planning records.

Mitigation: Require explicit user review before every write or delete command, especially for guests, budget, registry, invitations, website content, and vendor records.

Risk: Several Zola write endpoints replace full objects, so partial requests can wipe unrelated fields.

Mitigation: Use the documented read-modify-write flow: fetch the current record, preserve unchanged fields, patch only intended values, and review the full request body before execution.

Risk: Non-2xx API errors may expose raw response bodies that are not redacted by this skill.

Mitigation: Inspect errors locally and redact tokens, account identifiers, and personal wedding data before sharing diagnostics.

## Reference(s):

- [Zola mobile-api endpoints](references/mobile-api-endpoints.md)
- [Zola mobile API](https://mobile-api.zola.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, curl examples, jq filters, and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Zola refresh token and session headers; many examples operate on live account data.]

## Skill Version(s):

2.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
