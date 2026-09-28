## Description:

Helps agents earn, hold, and spend Nano (XNO) with a no-node wallet, HTTP 402 payment instructions, and a directory of sellers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pursekeeper](https://clawhub.ai/user/pursekeeper)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to find ways to earn Nano, make or accept small Nano payments, and access paid services without running a Nano node.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the wallet or payment client with a funded seed can spend real cryptocurrency.

Mitigation: Use a small funded wallet; keep NANO_SEED out of logs and shell history, and keep NANO_MAX_PAY low unless deliberately raising it for one run.

Risk: A mistaken seller, recipient, amount, or HTTP 402 quote can result in an irreversible payment.

Mitigation: Independently verify the seller URL, payment address, amount, and 402 quote before signing or broadcasting.

## Reference(s):

- [pursekeeper homepage](https://pursekeeper.dev)
- [No-node wallet guide](references/no-node.md)
- [NanoGPT payment walkthrough](references/buy-from-nanogpt.md)
- [Seller directory and payment examples](references/sellers.md)
- [Live Nano seller directory](https://pursekeeper.dev/sellers.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.6 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
