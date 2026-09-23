## Description:

One integration, one wallet relationship. Thousands of callable tools, paid per call in USDC via x402. Charge on success only — errors and verification failures settle nothing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noahmchugh](https://clawhub.ai/user/noahmchugh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to find, price, create, and call remote catalog tools through a paid MCP integration with hash-chained receipts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inputs to catalog tools and create_and_call may be sent to remote infrastructure or downstream tools.

Mitigation: Avoid secrets, credentials, private documents, internal endpoints, and regulated data unless the destination has been separately approved.

Risk: Paid calls can spend USDC when remote tool execution succeeds.

Mitigation: Use get_quote and payment controls before call_tool or create_and_call, and review spend reports and receipts.

Risk: Dynamic tool creation and arbitrary remote tool execution can produce behavior outside the local skill artifact.

Mitigation: Review requested outcomes, inputs, callback URLs, and returned tool details before relying on results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/noahmchugh/skills/stinkyboy)
- [stinkyboy full specification](https://stinkyboy.co/llms-full.txt)
- [stinkyboy catalog](https://stinkyboy.co/catalog)
- [stinkyboy MCP endpoint](https://mcp.stinkyboy.co/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown or text guidance with tool call parameters and remote tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include price quotes, spend reports, receipts, tool details, and outputs from downstream catalog tools.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
