## Description:

Verify wallets, tokens, smart contracts, AI agents and web applications before trusting them, paying per call in USDC over x402

This skill is ready for commercial/non-commercial use.

## Publisher:

[cybercentry](https://clawhub.ai/user/cybercentry)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to check wallets, tokens, Solidity code, web applications, media, private-data claims, cryptography choices, and agent configurations before trusting them or connecting funds and tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted addresses, URLs, source code, media, or other inputs are sent to Cybercentry's remote service for analysis.

Mitigation: Only submit content the user is comfortable sharing with the remote service.

Risk: Paid verification tools cost $1.00 per call in USDC.

Mitigation: Require explicit user confirmation of the tool, exact input, and $1.00 charge before any paid call.

Risk: Verification results inform decisions but do not guarantee that a target is safe.

Mitigation: Report which checks ran and present clean results as no finding from those checks, not as proof of safety.

Risk: A submitted third-party URL may be hostile.

Mitigation: Report scanned third-party URLs as plain text instead of rendering them as clickable links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cybercentry/skills/cybercentry-verification)
- [Cybercentry MCP server](https://centry.cybercentry.co.uk/api/mcp)
- [Cybercentry OpenAPI contract](https://centry.cybercentry.co.uk/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with MCP or HTTP request details and verification results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Remote service responses may include asynchronous job IDs, poll URLs, risk levels, proof IDs, or explanatory security findings.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
