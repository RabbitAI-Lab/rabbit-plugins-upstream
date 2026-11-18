## Description:

Earn and spend Nano (XNO) with other agents. A directory of services that take Nano over HTTP 402, each verified by a real payment; a wallet that needs only a seed and HTTPS, no node; a public x402 facilitator for selling; and the ways an agent gets its first Nano. Use when an API answers 402 with a nano_ address, when you want to sell a service for Nano, when you need a Nano wallet without running a node, or when asked where Nano can be spent or earned.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pursekeeper](https://clawhub.ai/user/pursekeeper)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find services that accept Nano, make or receive Nano payments, sell services through HTTP 402, and configure a Nano-funded inference proxy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment rates this release suspicious, citing a network redirection weakness and a payment-lock race. The inspection is incomplete, so the findings do not establish malicious intent.

Mitigation: Before installing, review which external services the skill contacts and its data-sharing guidance. Check payment outcomes before retrying, and account for the scan's 44.4% full component coverage.

## Reference(s):

- [Pursekeeper website](https://pursekeeper.dev)
- [Nano wallet guide](references/no-node.md)
- [Seller directory guide](references/sellers.md)
- [x402 inference proxy guide](references/inference-proxy.md)
- [NanoGPT purchase guide](references/buy-from-nanogpt.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown guidance with shell command examples and JavaScript scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes payment and wallet guidance; actions may sign and broadcast irreversible Nano payments.]

## Skill Version(s):

0.3.15 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
