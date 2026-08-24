## Description:

Prepare the desk computer to work with Hyperliquid - install the SDKs, pick testnet or mainnet, verify connectivity, and (only when the user asks) provision a trade-only API wallet through the secure secret store and verify it is approved.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading-desk operators use this skill to prepare a Hyperliquid environment, install required SDKs, choose testnet or mainnet deliberately, verify connectivity, and set up a trade-only API wallet when trading is requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles a Hyperliquid trading API key.

Mitigation: Use the secure secret store, keep main-wallet keys and seed phrases off the desk computer, and avoid the file fallback unless no safer secret mechanism is available.

Risk: A trading API wallet can still place, modify, and cancel orders or otherwise affect funds within the user's account.

Mitigation: Use a trade-only API wallet, start on testnet, verify the key is approved for the intended account and network, and revoke or rotate the API wallet after setup changes or suspected misuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-setup)
- [Hyperliquid API](https://api.hyperliquid.xyz)
- [Hyperliquid testnet API](https://api.hyperliquid-testnet.xyz)
- [Hyperliquid app](https://app.hyperliquid.xyz)
- [Hyperliquid testnet app](https://app.hyperliquid-testnet.xyz)
- [Hyperliquid testnet faucet](https://app.hyperliquid-testnet.xyz/drip)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes read-only connectivity checks, environment variable setup, secure secret-store guidance, and API-wallet readiness checks.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
