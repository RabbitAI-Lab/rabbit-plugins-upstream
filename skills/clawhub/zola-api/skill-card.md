## Description:

Guides agents in reading and updating Zola wedding-planning data through direct mobile API calls with curl, without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Zola account holders and developers use this skill to inspect or update wedding vendors, budgets, guests, events, registry items, invitations, and website content through direct API requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A long-lived account refresh token or session token could be exposed in shell history, logs, or shared error output.

Mitigation: Treat tokens like passwords; avoid pasting them into logged shells and never share unredacted token-bearing output.

Risk: Direct write, delete, booking, registry, budget, guest, invitation, or website changes may modify live account data unexpectedly.

Mitigation: Read current state, review a proposed diff, and obtain explicit user confirmation before each change.

Risk: Replacing an entire record with a partial update can erase unrelated fields.

Mitigation: Read the complete current record and preserve unchanged fields when constructing updates.

## Reference(s):

- [Zola API skill release](https://clawhub.ai/chrischall/skills/zola-api)
- [Mobile API endpoint recipes](references/mobile-api-endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Text guidance]

**Output Format:** [Markdown with curl and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses may contain private wedding and account data.]

## Skill Version(s):

2.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
