## Description:

Read HoneyBook client-portal data from a shell with fpx and curl by capturing an authorized browser session once and reusing it for API reads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators with authorized HoneyBook access use this skill to configure fpx, capture an existing HoneyBook portal session, and run curl or jq commands for contracts, invoices, proposals, payment methods, and workspace status without running the HoneyBook MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow captures and reuses live HoneyBook session credentials that can expose sensitive account, contract, invoice, and payment-method data.

Mitigation: Use the skill only with explicit authorization, keep captured tokens out of shared files, logs, and tickets, and prefer an official or scoped integration when available.

Risk: Temporary files containing session data or full API responses may persist sensitive information beyond the intended task.

Mitigation: Keep tokens in shell variables where practical, restrict any temporary file permissions, and remove session or response files after use.

## Reference(s):

- [HoneyBook request examples](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook-fpx)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command patterns and operational guidance; it does not itself execute HoneyBook requests.]

## Skill Version(s):

0.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
