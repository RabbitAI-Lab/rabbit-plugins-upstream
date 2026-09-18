## Description:

Read HoneyBook client-portal data from a shell using the fpx CLI and curl, including contracts, invoices, proposals, payment methods, and workspace status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve HoneyBook portal data through shell workflows when the HoneyBook MCP server is unavailable or unnecessary. It helps agents produce setup guidance, authenticated curl commands, and focused data-retrieval steps for authorized HoneyBook client-portal sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent browser-session access and long-lived HoneyBook credentials can expose sensitive client-portal data.

Mitigation: Use the skill only in an isolated environment with a trusted, pinned fpx version, restrict browser-extension access to the minimum HoneyBook sites needed, keep tokens out of shared temporary files, and delete captured data immediately.

Risk: The documented message-send flow can email a vendor for real despite the skill's primarily read-oriented posture.

Mitigation: Do not use the message-send flow unless the user explicitly approves the exact recipient and message before execution.

Risk: Direct API reads may return contracts, invoices, proposals, payment methods, and other sensitive HoneyBook records.

Mitigation: Limit use to authorized vendor sessions and project or filter responses before displaying or storing raw data.

## Reference(s):

- [HoneyBook request examples](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON-processing examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes HoneyBook API request patterns, session-capture setup, response filtering examples, and error-handling guidance.]

## Skill Version(s):

0.10.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
