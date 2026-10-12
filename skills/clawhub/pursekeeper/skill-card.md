## Description:

Helps agents earn and spend Nano (XNO) through a no-node wallet, HTTP 402 payment workflows, a seller directory, and guidance for paid services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pursekeeper](https://clawhub.ai/user/pursekeeper)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find Nano-paid services, make capped HTTP 402 payments, operate a no-node wallet, or accept Nano for their own services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment actions can spend real funds, and exposure of the wallet seed grants control of the wallet.

Mitigation: Use a dedicated low-balance wallet and protect NANO_SEED as a secret.

Risk: Unintended or excessive payments may deplete the wallet.

Mitigation: Set NANO_MAX_PAY and NANO_CAP deliberately before paying.

Risk: Unknown paid services may receive funds and sensitive request data.

Mitigation: Verify UPSTREAM and seller endpoints before paying; avoid sending sensitive prompts or data to unknown services.

## Reference(s):

- [Pursekeeper website](https://pursekeeper.dev)
- [Pursekeeper on ClawHub](https://clawhub.ai/pursekeeper/skills/pursekeeper)
- [Seller directory and payment methods](references/sellers.md)
- [No-node wallet guide](references/no-node.md)
- [Inference proxy guide](references/inference-proxy.md)
- [NanoGPT purchase guide](references/buy-from-nanogpt.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Payments can transfer real Nano; users set spending limits before execution.]

## Skill Version(s):

0.3.0 (source: frontmatter, CHANGELOG, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
