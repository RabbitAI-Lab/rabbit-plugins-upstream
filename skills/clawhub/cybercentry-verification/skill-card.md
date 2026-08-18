## Description:

Verify wallets, tokens, smart contracts, AI agents and web applications before trusting them, paying per call in USDC over x402.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cybercentry](https://clawhub.ai/user/cybercentry)

### License/Terms of Use:

MIT

## Use Case:

Developers, security reviewers, and agent operators use this skill to request Cybercentry checks before interacting with wallets, tokens, smart contracts, dApps, AI agents, or media. It guides agents to prefer free catalogue and exploit lookups, confirm paid USDC calls, and report verification results without treating them as guarantees.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted addresses, URLs, source code, media, or configuration details are sent to Cybercentry for analysis.

Mitigation: Install and use only when the user is comfortable sharing the exact submitted items with Cybercentry.

Risk: Paid tools cost $1.00 per call in USDC.

Mitigation: Confirm the named tool, exact input, and price before each paid call; prefer free list_services and recent_exploits results when they answer the request.

Risk: A clean verification result is not a guarantee that an asset or application is safe.

Mitigation: Report which checks ran and frame the result as decision support rather than approval or transaction blocking.

## Reference(s):

- [Cybercentry service homepage](https://centry.cybercentry.co.uk)
- [Cybercentry MCP endpoint](https://centry.cybercentry.co.uk/api/mcp)
- [Cybercentry OpenAPI contract](https://centry.cybercentry.co.uk/openapi.json)
- [ClawHub skill listing](https://clawhub.ai/cybercentry/skills/cybercentry-verification)

## Skill Output:

**Output Type(s):** [Guidance, Text, API calls, Shell commands, Configuration]

**Output Format:** [Markdown or plain text with inline commands and service results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include asynchronous job IDs, poll URLs, risk levels, proof or record URLs, and payment confirmation details returned by Cybercentry services.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
