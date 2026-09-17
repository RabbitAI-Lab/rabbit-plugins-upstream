## Description:

Query Credit Karma transactions from a shell with the fpx CLI and direct curl requests, using a signed-in browser session cookie for one-time capture and subsequent GraphQL transaction reads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically capable users use this skill to retrieve their own Credit Karma transaction data from a shell for scripts or local workflows when the MCP server is not installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive Credit Karma cookies and access or refresh tokens may be exposed through shell history, tracing, shared terminals, chats, logs, or world-readable temporary files.

Mitigation: Use the skill only on a trusted machine for your own account, keep tokens in shell variables when possible, disable shell tracing, avoid shared terminals and logs, and use private temporary directories with restrictive permissions.

Risk: Browser pairing or captured session material may remain valid after accidental exposure.

Mitigation: Revoke the browser pairing or session and re-authenticate if CKAT, CKTRKID, ACCESS, or REFRESH may have been exposed.

Risk: The transaction and refresh flows depend on Credit Karma web session behavior and internal endpoints that may change.

Mitigation: Review responses before trusting data, handle in-body authentication errors, and re-check the request hash or session capture flow when requests fail or schemas drift.

## Reference(s):

- [Credit Karma requests for fpx + curl](artifact/references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command-oriented instructions for cookie capture, transaction pagination, token refresh, and response projection.]

## Skill Version(s):

2.8.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
