## Description:

zola-api helps agents query or update Zola wedding-planning data from a shell using curl against mobile-api.zola.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to inspect or update Zola wedding-planning records, including vendors, budget, guests, seating, events, RSVPs, registry, gift tracker, inquiries, wedding website content, and invitations, directly from shell scripts instead of using the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for a long-lived Zola refresh token and uses session tokens for account access.

Mitigation: Treat ZOLA_REFRESH_TOKEN like a password, avoid pasting it into chats or logs, and avoid sharing raw error bodies that may contain token material.

Risk: Several provided POST, PUT, and DELETE commands can modify or remove live wedding-planning data.

Mitigation: Require explicit review before running mutating commands, especially for guests, registry, budget, website, invitations, vendors, and RSVP data.

Risk: Some Zola write endpoints replace full objects, so incomplete payloads can overwrite unrelated fields.

Mitigation: Use the documented read-modify-write flow and preserve existing fields unless the user intentionally changes them.

## Reference(s):

- [Zola mobile-api endpoints](references/mobile-api-endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with curl, jq, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require ZOLA_REFRESH_TOKEN, session headers, context IDs, and explicit review before write or delete operations.]

## Skill Version(s):

2.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
