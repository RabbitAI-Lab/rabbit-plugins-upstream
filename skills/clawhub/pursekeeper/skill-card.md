## Description:

Earn and spend Nano (XNO) with other agents using a service directory, a wallet that does not require running a node, x402 payment guidance, and ways to get funded.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pursekeeper](https://clawhub.ai/user/pursekeeper)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to find services that accept Nano, make or accept HTTP 402 payments, manage a wallet without running a node, and learn how to get funded.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Redirects may expose service credentials, and uncertain payment outcomes may lead to unsafe retries.

Mitigation: Use a separate wallet with a small balance and conservative spending caps; avoid sending credentials through HEADERS until cross-origin handling is fixed; check the original payment hash before retrying; pin dependencies and send only intended content to the selected seller.

## Reference(s):

- [Pursekeeper](https://pursekeeper.dev)
- [ClawHub release](https://clawhub.ai/pursekeeper/skills/pursekeeper)
- [Wallet without a node](references/no-node.md)
- [Nano payment inference proxy](references/inference-proxy.md)
- [Seller directory and payment guidance](references/sellers.md)
- [Buying inference from NanoGPT](references/buy-from-nanogpt.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, API calls]

**Output Format:** [Markdown guidance with shell commands, JavaScript examples, and JSON or HTTP payment payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include payment amounts, wallet settings, service endpoints, and transaction hashes; payment actions can spend real Nano.]

## Skill Version(s):

0.3.11 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
