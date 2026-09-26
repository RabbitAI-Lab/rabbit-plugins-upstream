## Description:

Guides agents in reading and updating Zola wedding-planning data through authenticated mobile API requests from a shell.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Zola account holders and developers use this skill to inspect or update wedding vendors, budgets, guests, events, registries, invitations, and website content without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A long-lived account token could expose the Zola account if shared or logged.

Mitigation: Keep the token private and out of shell history, shared logs, and public error reports.

Risk: Write or delete commands can change live wedding, guest, budget, registry, event, invitation, and website data.

Mitigation: Require explicit confirmation of the exact target and proposed changes before each write or delete.

Risk: Partial replacement requests can erase unrelated guest invitations or website settings.

Mitigation: Read the current record first and preserve unchanged fields in replacement requests.

## Reference(s):

- [Zola API endpoint recipes](references/mobile-api-endpoints.md)
- [zola-api ClawHub release](https://clawhub.ai/chrischall/skills/zola-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated requests can return JSON account data.]

## Skill Version(s):

2.1.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
