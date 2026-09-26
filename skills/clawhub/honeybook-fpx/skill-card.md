## Description:

Guides authorized HoneyBook users in capturing an active portal session and reading client records through shell commands without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized HoneyBook clients and developers use the skill to retrieve contracts, invoices, proposals, payment methods, and workspace details from a signed-in client portal without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Captured session credentials and returned client records can expose sensitive HoneyBook data if left in files or used on shared machines.

Mitigation: Use only an authorized signed-in session; restrict access to credentials and API outputs, avoid shared machines, and promptly remove temporary files.

Risk: The message-sending guidance can trigger real outbound communications despite the skill's read-focused description.

Mitigation: Do not follow message-sending steps unless you intend to contact the vendor; review the recipient and content before sending.

## Reference(s):

- [HoneyBook FPX release](https://clawhub.ai/chrischall/skills/honeybook-fpx)
- [Request examples](references/requests.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return sensitive HoneyBook client records; no fixed output length.]

## Skill Version(s):

1.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
