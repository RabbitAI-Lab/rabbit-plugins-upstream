## Description:

Helps agents earn and spend Nano (XNO) through a no-node wallet, HTTP 402 payment recipes, a seller directory, and x402 selling guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pursekeeper](https://clawhub.ai/user/pursekeeper)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to find Nano-accepting services, manage a Nano wallet without a local node, pay for HTTP 402 services, and offer paid services of their own.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A disclosed wallet seed can expose funds.

Mitigation: Keep NANO_SEED out of logs, CI, and shared machines; use a low-balance wallet.

Risk: Paid calls may spend more than intended or pay an untrusted seller.

Mitigation: Set NANO_MAX_PAY, NANO_CAP, and NANO_MAX_PER_CALL deliberately, and verify seller URLs and quotes before payment.

Risk: A saved payment signature can remain spendable until its block confirms.

Mitigation: Use NANO_SAVE_PAYLOAD only when needed and safeguard the saved file until confirmation.

Risk: Third-party npm dependencies can introduce supply-chain exposure.

Mitigation: Consider pinning and auditing dependencies before using meaningful funds.

## Reference(s):

- [Pursekeeper skill on ClawHub](https://clawhub.ai/pursekeeper/skills/pursekeeper)
- [Pursekeeper homepage](https://pursekeeper.dev)
- [Live seller directory](https://pursekeeper.dev/sellers.json)
- [No-node wallet guide](references/no-node.md)
- [Inference proxy guide](references/inference-proxy.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Wallet operations and paid requests require explicit operator setup and may spend XNO.]

## Skill Version(s):

0.3.1 (source: SKILL.md frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
