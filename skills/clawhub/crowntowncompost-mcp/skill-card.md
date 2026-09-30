## Description:

Guides agents in accessing Crown Town Compost pickup history, invoices, service dates, and account features through the customer portal using shell commands instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Crown Town Compost customers and their authorized agents can retrieve pickup and billing information or manage service requests from a shell without installing the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal actions can change service and account settings despite the skill's data-access framing.

Mitigation: Review the skill before installing and require explicit human approval before skips, account updates, support messages, missed-pickup reports, or cancellation requests.

Risk: Credentials, session cookies, and exported invoices can expose private account or billing information.

Mitigation: Protect credentials and the cookie jar; delete the cookie jar and billing exports when finished.

Risk: Partial account updates can turn off notification preferences, and a redirect does not prove a change persisted.

Mitigation: Read existing settings before updates, preserve all fields, and re-read the portal after any change.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/crowntowncompost-mcp)
- [Crown Town Compost portal endpoint reference](references/endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and portal-response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide retrieval of account data and consequential service or account changes.]

## Skill Version(s):

1.1.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
