## Description:

Read HoneyBook client-portal data, including contracts, invoices, proposals, payment methods, and workspace status, from a shell with the fpx CLI and direct curl calls to api.honeybook.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve HoneyBook client-portal data from an authenticated browser session without running the HoneyBook MCP server. It provides setup guidance and ready-to-run shell commands for reading workspace files, file details, workspaces, and saved payment methods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles live HoneyBook session credentials and authenticated API headers.

Mitigation: Run it only on trusted machines, keep captured tokens out of logs and shell history, avoid world-readable session files, and delete temporary session or response files promptly.

Risk: The documented message-sending flow can email a vendor for real.

Mitigation: Use the read-only request examples unless you explicitly intend to send a message; prefer a previewing workflow before any email action.

Risk: HoneyBook responses may contain sensitive client, contract, invoice, payment-method, or vendor-internal data.

Mitigation: Query only data the authenticated user is authorized to access and project large responses down to the fields needed for the task.

## Reference(s):

- [HoneyBook request examples](references/requests.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash and jq code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may produce JSON responses from HoneyBook APIs when run by an authorized user.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
