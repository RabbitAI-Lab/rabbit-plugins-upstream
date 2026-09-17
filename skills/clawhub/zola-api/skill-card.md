## Description:

Query or update Zola wedding-planning data from a shell with curl against mobile-api.zola.com, without running the zola-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical operators use this skill to inspect or maintain Zola wedding-planning records from scripts, terminals, or machines where the MCP server is not installed. It supports read and write workflows for vendors, budget, guests, seating, events and RSVPs, registry, gift tracking, inquiries, wedding website content, and invitations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles a long-lived Zola account refresh token and short-lived session token.

Mitigation: Treat ZOLA_REFRESH_TOKEN and SESSION_TOKEN as account secrets and avoid placing them in shell history, logs, screenshots, repositories, or shared terminals.

Risk: Ready-to-run commands can read, modify, or delete sensitive wedding-planning data.

Mitigation: Manually confirm the account, IDs, request body, and before-and-after data before any write or delete operation; prefer read-only use when possible.

Risk: Some Zola write endpoints replace whole objects and can wipe unrelated fields when given partial bodies.

Mitigation: Use the documented read-modify-write pattern and preserve existing fields unless the change intentionally replaces them.

## Reference(s):

- [Zola mobile-api endpoints](references/mobile-api-endpoints.md)
- [Zola website](https://www.zola.com)
- [Zola mobile API](https://mobile-api.zola.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands generally expect curl, jq, ZOLA_REFRESH_TOKEN, SESSION_TOKEN, DEVICE_SESSION_ID, and resolved Zola account IDs.]

## Skill Version(s):

1.12.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
