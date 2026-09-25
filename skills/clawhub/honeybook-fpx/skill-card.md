## Description:

honeybook-fpx helps agents read HoneyBook client-portal data from shell workflows using fpx session capture and curl requests to HoneyBook APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical operators use this skill to retrieve HoneyBook contracts, invoices, proposals, payment methods, and workspace status without running the HoneyBook MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill captures and reuses live HoneyBook session credentials, including AUTH_TOKEN and TRUSTED_DEVICE values.

Mitigation: Use only on a trusted single-user machine, keep tokens out of shared paths, delete captured session files immediately, and treat all captured values like passwords.

Risk: Session exports and API responses may contain HoneyBook client, vendor, contract, invoice, payment, or workspace data.

Mitigation: Avoid writing captures or responses to shared temporary locations; project only the fields needed and remove local files after review.

Risk: The artifact describes a message-sending flow that emails a vendor for real.

Mitigation: Do not use the message-sending flow unless the user explicitly requests and confirms it; prefer a previewing workflow before sending.

## Reference(s):

- [HoneyBook requests for fpx + curl](artifact/references/requests.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command blocks and JSON API response handling notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance includes direct HoneyBook API calls and session-token handling instructions.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
