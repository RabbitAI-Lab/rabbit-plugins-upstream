## Description:

Query and update Zola wedding-planning data from a shell with curl against mobile-api.zola.com instead of running the zola-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable Zola users use this skill to inspect or update wedding-planning data such as vendors, budget, guests, seating, RSVPs, registry, and website content through direct API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a long-lived Zola refresh token or usr cookie and a short-lived session token that grant access to account data.

Mitigation: Treat these tokens like passwords, keep them out of chats, logs, screenshots, and public error reports, and prefer environment variables or local shell state over pasted credentials.

Risk: The skill includes ready-to-run write and delete commands that can change vendors, budgets, guests, events, registry, and website content.

Mitigation: Start with read-only calls, manually verify account IDs and object IDs, back up current data when practical, and review each command before execution.

Risk: Some Zola write endpoints replace whole objects, so partial request bodies can erase unrelated fields.

Mitigation: Use the documented read-modify-write pattern and preserve unmodified fields, especially event invitations and website customization fields.

## Reference(s):

- [Zola mobile-api endpoints](references/mobile-api-endpoints.md)
- [Zola](https://www.zola.com)
- [Zola mobile API](https://mobile-api.zola.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may call live Zola APIs and can return account data or mutate account state.]

## Skill Version(s):

2.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
