## Description:

zola-api helps agents query and update Zola wedding-planning data from a shell using curl against mobile-api.zola.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to retrieve or change Zola vendors, budgets, guest lists, seating, events, RSVPs, registry, and website data without running the Zola MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a long-lived Zola refresh token and session tokens that can access live wedding data.

Mitigation: Treat tokens like passwords, keep them out of shared chats and logs, and revoke or rotate credentials if exposed.

Risk: The recipes include POST, PUT, and DELETE operations that can change or remove live Zola account data.

Mitigation: Manually review mutation commands before running them and resolve account, registry, wedding, and record IDs from the current context first.

Risk: Some Zola write endpoints replace whole objects, so partial request bodies can erase unrelated fields.

Mitigation: Use the documented read-modify-write patterns and preserve existing fields such as event invitations and website customization values.

## Reference(s):

- [Zola mobile-api endpoints](references/mobile-api-endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl and jq shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Zola refresh token supplied outside the skill output.]

## Skill Version(s):

1.12.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
