## Description:

OpenclawCash crypto wallet API for AI agents (also called openclawcash). Use when an agent needs to send native or token transfers, check balances, list wallets, or interact with EVM and Solana wallets programmatically via OpenclawCash.

This skill is ready for commercial/non-commercial use.

## Publisher:

[macd2](https://clawhub.ai/user/macd2)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to connect agents to OpenClawCash-managed EVM and Solana wallets for balance checks, wallet policy review, token transfers, swaps, checkout escrow, and venue operations. It is intended for environments where the user deliberately grants an agent financial authority through a scoped OpenClawCash API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can move funds or make persistent account changes when an API key has sufficient authority.

Mitigation: Use per-action confirmation where possible, keep API keys tightly scoped, and review wallet policies before transfer, swap, venue, webhook, or user-tag actions.

Risk: Session-level approval can allow repeated write actions without a fresh prompt.

Mitigation: Use broad approval only for a clearly bounded session and return to confirm-each-write mode when scope, wallet, amount, token, destination, or chain is unclear.

Risk: Wallet import may expose sensitive private-key material to the agent workflow.

Mitigation: Avoid wallet import unless necessary; if used, prefer hidden prompt or stdin and ensure dashboard import permission is intentionally enabled.

Risk: Running an unreviewed MCP package or fallback script can expand the trusted execution surface.

Mitigation: Pin or review the MCP package and inspect the bundled shell scripts before granting wallet API credentials.

## Reference(s):

- [OpenClawCash Agent API](https://openclawcash.com)
- [API Endpoint Details](references/api-endpoints.md)
- [ClawHub OpenClawCash Skill Listing](https://clawhub.ai/macd2/skills/open-claw-cash)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an OpenClawCash API key for authenticated wallet operations.]

## Skill Version(s):

1.28.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
