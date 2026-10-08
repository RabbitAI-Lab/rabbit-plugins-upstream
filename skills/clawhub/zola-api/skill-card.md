## Description:

Guides agents to query and update Zola wedding-planning data through shell commands using the Zola mobile API without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers working with an authorized Zola account can retrieve wedding-planning information and prepare updates to vendors, budgets, guest lists, events, registry items, and website settings without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A long-lived Zola login token can expose private wedding account data if leaked.

Mitigation: Keep the refresh token in a secure secret store and redact tokens, guest data, and raw error bodies from logs and shared chats.

Risk: Commands can change or delete live wedding account data, including unrelated fields on full-record updates.

Mitigation: Start with read-only operations, confirm writes and deletes explicitly, verify record IDs, and preserve existing fields when updating records.

## Reference(s):

- [Zola API skill release](https://clawhub.ai/chrischall/skills/zola-api)
- [Mobile API endpoint recipes](references/mobile-api-endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands act on a live Zola account and require account credentials.]

## Skill Version(s):

2.1.9 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
