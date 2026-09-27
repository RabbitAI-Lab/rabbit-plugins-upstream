## Description:

Guides agents through earning, holding, spending, and accepting Nano (XNO), including HTTP 402 payments and a wallet that does not require a local node.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pursekeeper](https://clawhub.ai/user/pursekeeper)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find Nano-accepting services, make small payments, manage a Nano wallet without a local node, and accept payments for their own services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Transactions are irreversible, and scripts may sign using unverified third-party ledger state.

Mitigation: Fund the wallet only with small amounts, verify each recipient and amount, and prefer a trusted local node or independently verified account state before signing.

Risk: Exposure of the Nano wallet seed could compromise funds.

Mitigation: Keep NANO_SEED out of logs and shared shells; store it securely and never send it to services.

Risk: Paid external services may receive confidential prompts or request data.

Mitigation: Avoid submitting confidential prompts or sensitive data to paid external services.

## Reference(s):

- [pursekeeper homepage](https://pursekeeper.dev)
- [ClawHub skill listing](https://clawhub.ai/pursekeeper/skills/pursekeeper)
- [No-node wallet and payment guide](artifact/references/no-node.md)
- [NanoGPT payment guide](artifact/references/buy-from-nanogpt.md)
- [Nano-accepting services](https://pursekeeper.dev/sellers.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Wallet commands can return addresses, balances, and transaction hashes.]

## Skill Version(s):

0.1.2 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
