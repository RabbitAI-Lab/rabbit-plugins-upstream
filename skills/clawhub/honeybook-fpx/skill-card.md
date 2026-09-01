## Description:

Read HoneyBook client-portal data (contracts, invoices, proposals, payment methods, workspace status) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the honeybook-mcp server; capture a vendor session once via the signed-in browser tab, then curl api.honeybook.com directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve authorized HoneyBook client-portal records from shell workflows without running a HoneyBook MCP server. It helps inspect contracts, invoices, proposals, payment methods, and workspace status through captured browser-session credentials and direct read-only API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill captures live HoneyBook session credentials and can access sensitive account, client, contract, invoice, proposal, and payment-method data.

Mitigation: Use it only for accounts and vendors you are authorized to access, avoid shared machines, and never log or commit session tokens or API responses.

Risk: The examples write captured sessions and API responses to /tmp paths, which can expose sensitive data on some systems.

Mitigation: Use secure temporary files or direct pipes instead, restrict file permissions, and delete captured session and response files immediately after use.

Risk: The listed workspace-file command does not fetch later result pages when HoneyBook indicates more pages are available.

Mitigation: Check the response pagination fields and add explicit page traversal before relying on the result set as complete.

## Reference(s):

- [HoneyBook request examples](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook-fpx)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command patterns and request examples for reading JSON responses from HoneyBook APIs.]

## Skill Version(s):

0.8.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
