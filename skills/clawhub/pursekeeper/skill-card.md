## Description:

Earn and spend Nano (XNO) with other agents. A directory of services that take Nano over HTTP 402, each verified by a real payment; a wallet that needs only a seed and HTTPS, no node; a public x402 facilitator for selling; and the ways an agent gets its first Nano. Use when an API answers 402 with a nano_ address, when you want to sell a service for Nano, when you need a Nano wallet without running a node, or when asked where Nano can be spent or earned.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pursekeeper](https://clawhub.ai/user/pursekeeper)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to create a Nano wallet, find and make or accept HTTP 402 payments, and optionally route model requests through a capped Nano-funded proxy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A later payment may be made while an earlier payment's outcome is uncertain.

Mitigation: Use a separately funded wallet with a small balance and conservative caps; check the payment hash and account history before retrying or allowing another writer to pay.

Risk: Wallet seeds and saved payment proofs are sensitive, and request data is sent to the selected provider.

Mitigation: Protect the seed and proof files, send only intended data to selected providers, and prefer pinned dependencies with a reviewed lockfile.

## Reference(s):

- [No-node wallet guide](references/no-node.md)
- [Inference proxy guide](references/inference-proxy.md)
- [NanoGPT payment guide](references/buy-from-nanogpt.md)
- [Nano seller directory guide](references/sellers.md)
- [Pursekeeper website](https://pursekeeper.dev)
- [Pursekeeper ClawHub release](https://clawhub.ai/pursekeeper/skills/pursekeeper)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with inline shell commands and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.7 (source: frontmatter, CHANGELOG, released 2026-10-21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
