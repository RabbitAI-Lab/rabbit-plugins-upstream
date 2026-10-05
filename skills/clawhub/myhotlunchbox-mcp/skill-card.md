## Description:

Guides agents in using shell commands to read and manage a My Hot Lunchbox school-lunch account without the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

My Hot Lunchbox account holders and developers can use this skill to inspect students, lunch calendars, carts, orders, and payments from a shell when the MCP server is unavailable, and to prepare carefully reviewed account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials or account data may be exposed when running manual account commands.

Mitigation: Keep credentials in environment variables, avoid logging tokens or sensitive responses, and use only trusted machines.

Risk: Incorrect or incomplete write requests can change orders, profiles, and subscriptions unexpectedly.

Mitigation: Inspect the complete JSON body before posting and re-read the affected resource afterwards; prefer the MCP version's confirmation steps when available.

Risk: Speculative payment requests can charge a real card.

Mitigation: Check the priced total and obtain explicit confirmation before checkout; do not issue speculative payment calls.

Risk: Repeated failed sign-ins can restrict account access.

Mitigation: Do not retry an invalid-grant response; verify credentials before signing in again.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/myhotlunchbox-mcp)
- [Endpoint reference](references/endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text or Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can retrieve JSON account data or PDF reports; account-changing requests require review.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
