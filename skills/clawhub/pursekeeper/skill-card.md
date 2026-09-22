## Description:

Earn and spend Nano (XNO) with other agents. A directory of services that take Nano over HTTP 402, each verified by a real payment; a wallet that needs only a seed and HTTPS, no node; a public x402 facilitator for selling; and the ways an agent gets its first Nano. Use when an API answers 402 with a nano_ address, when you want to sell a service for Nano, when you need a Nano wallet without running a node, or when asked where Nano can be spent or earned.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pursekeeper](https://clawhub.ai/user/pursekeeper)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent operators, and external users use this skill to hold small Nano balances, pay HTTP 402 services, verify Nano payments, and publish or find Nano-paid agent services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper scripts can move Nano funds when explicitly run.

Mitigation: Use small balances, review the recipient, amount, endpoint, and request body before paying, and keep the NANO_MAX_PAY spending cap low unless a higher quote is intentional.

Risk: Anyone with the wallet seed can control the funds.

Mitigation: Keep NANO_SEED private, store it outside logs and source control, and avoid printing or transmitting it.

Risk: Nano sends are final once confirmed and cannot be reversed at the protocol level.

Mitigation: Confirm the price, payment scheme, destination address, and block hash before treating a payment as complete.

Risk: Listed sellers and third-party endpoints may change availability or receive request data.

Mitigation: Fetch live seller data before paying, check reachability, and avoid sending secrets or sensitive business data to third-party services.

## Reference(s):

- [pursekeeper homepage](https://pursekeeper.dev)
- [ClawHub skill listing](https://clawhub.ai/pursekeeper/skills/pursekeeper)
- [No-node Nano wallet guide](references/no-node.md)
- [Services that take Nano over HTTP 402](references/sellers.md)
- [Buying inference from NanoGPT with Nano](references/buy-from-nanogpt.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JavaScript helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Nano addresses, HTTP 402 payment details, signed payment block hashes, and endpoint-specific request examples.]

## Skill Version(s):

0.1.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
