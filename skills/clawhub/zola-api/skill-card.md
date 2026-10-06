## Description:

Guides agents in reading and updating Zola wedding-planning data through direct mobile API calls from a shell.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Zola account holders and developers use this skill to query or update wedding vendors, budgets, guests, RSVPs, registry, invitations, and website content without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A leaked refresh token could expose the Zola account.

Mitigation: Treat ZOLA_REFRESH_TOKEN as a password, keep it out of shell history and logs, and revoke or rotate it if exposed.

Risk: Direct API calls can change or delete live wedding data without adequate safeguards.

Mitigation: Require explicit confirmation of exact record names and IDs before guest, budget, registry, website, invitation, or delete operations.

Risk: Partial writes may overwrite unrelated fields or remove guest event invitations.

Mitigation: Read the current record first and preserve unchanged fields when updating it.

## Reference(s):

- [Mobile API endpoint recipes](references/mobile-api-endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Zola refresh token and authenticated access to the account.]

## Skill Version(s):

2.1.8 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
