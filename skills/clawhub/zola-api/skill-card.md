## Description:

Query or update Zola wedding-planning data such as vendors, budget, guests, seating, RSVPs, registry, gift tracker, inquiries, and wedding website content from a shell with curl against mobile-api.zola.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to inspect or modify Zola wedding-planning account data directly through documented curl and jq recipes. It is most useful when the user wants API access without running the zola-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles a long-lived Zola refresh token that can grant account-level API access.

Mitigation: Treat the refresh token like a password, avoid sharing it in chats or shell history, and prefer secure secret storage.

Risk: The skill can perform raw write and delete operations against guest, budget, registry, event, RSVP, website, vendor, and invitation data.

Mitigation: Require explicit user confirmation before account-changing API calls and review request bodies before execution.

Risk: Some Zola write endpoints replace whole objects, so partial writes can overwrite unrelated account data.

Mitigation: Use the documented read-modify-write workflow and preserve existing fields when preparing PUT or POST bodies.

## Reference(s):

- [Zola mobile-api endpoints](references/mobile-api-endpoints.md)
- [Zola website](https://www.zola.com)
- [Zola mobile API](https://mobile-api.zola.com)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Zola refresh token and explicit user confirmation before account-changing API calls.]

## Skill Version(s):

1.12.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
