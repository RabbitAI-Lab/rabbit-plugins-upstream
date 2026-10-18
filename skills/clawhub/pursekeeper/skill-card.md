## Description:

Helps agents earn, hold, spend, and accept Nano (XNO) through wallet commands, HTTP 402 payment flows, seller guidance, and a paid inference proxy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pursekeeper](https://clawhub.ai/user/pursekeeper)

### License/Terms of Use:

MIT-0

## Use Case:

Agents, developers, and operators use this skill to manage a Nano wallet, pay for Nano-enabled APIs and model calls, find services that accept Nano, or accept and verify payments for their own services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A wallet seed gives control over its funds if exposed or misused.

Mitigation: Use a dedicated wallet funded only with what you can afford to spend; keep NANO_SEED private and never print or transmit it.

Risk: Paid API calls can spend Nano or pay an unintended seller.

Mitigation: Set NANO_MAX_PAY or NANO_CAP deliberately and review seller and API endpoints before sending paid requests.

Risk: A saved payment payload can remain a spendable signed send until it confirms.

Mitigation: Leave NANO_SAVE_PAYLOAD unset unless needed, and protect any saved payload as a sensitive credential.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pursekeeper/skills/pursekeeper)
- [Pursekeeper homepage](https://pursekeeper.dev)
- [No-node Nano wallet guide](references/no-node.md)
- [Seller and payment guidance](references/sellers.md)
- [Paid inference proxy guide](references/inference-proxy.md)
- [NanoGPT payment walkthrough](references/buy-from-nanogpt.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples and payment instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Nano addresses, payment amounts, transaction hashes, and API response guidance.]

## Skill Version(s):

0.3.2 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
