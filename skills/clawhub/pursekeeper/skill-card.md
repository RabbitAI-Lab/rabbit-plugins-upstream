## Description:

Helps agents earn and spend Nano (XNO) through a no-node wallet, a directory of HTTP 402 services, and payment guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pursekeeper](https://clawhub.ai/user/pursekeeper)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use the skill to find Nano-paid services, manage a no-node wallet, and make or accept HTTP 402 payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A disclosed wallet seed can expose all funds in that wallet.

Mitigation: Use a low-value seed and keep NANO_SEED out of logs, shell history, and shared requests.

Risk: Invoked payment commands can spend wallet funds at an unexpected price.

Mitigation: Review each quoted price and keep NANO_MAX_PAY low unless deliberately raised for a payment.

Risk: Untrusted seller URLs may receive sensitive request headers.

Mitigation: Do not send Authorization or other secret headers to seller URLs you do not fully trust.

## Reference(s):

- [pursekeeper homepage](https://pursekeeper.dev)
- [No-node wallet and payment guide](references/no-node.md)
- [Nano seller directory](references/sellers.md)
- [NanoGPT purchase guide](references/buy-from-nanogpt.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with shell and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.12 (source: frontmatter, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
