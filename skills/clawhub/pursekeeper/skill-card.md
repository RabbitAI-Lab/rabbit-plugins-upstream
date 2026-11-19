## Description:

Earn and spend Nano (XNO) with other agents. A directory of services that take Nano over HTTP 402, each verified by a real payment; a wallet that needs only a seed and HTTPS, no node; a public x402 facilitator for selling; and the ways an agent gets its first Nano. Use when an API answers 402 with a nano_ address, when you want to sell a service for Nano, when you need a Nano wallet without running a node, or when asked where Nano can be spent or earned.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pursekeeper](https://clawhub.ai/user/pursekeeper)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Pursekeeper to find services that accept Nano, use a wallet without running a node, pay HTTP 402 quotes, or accept Nano for their own services. Operators can also configure a capped Nano-funded inference proxy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports a possible payment-token disclosure, partial analysis of 11 of 21 components, and a suspicious verdict with medium confidence.

Mitigation: Review and scan the skill before installation, and avoid transactions that depend on another seller’s recovery entitlement.

Risk: A Nano seed controls wallet funds, and confirmed sends are final.

Mitigation: Keep the seed private and local, inspect each payment quote, and set an intentional spending cap before paying.

## Reference(s):

- [Pursekeeper website](https://pursekeeper.dev)
- [Verified Nano seller directory](https://pursekeeper.dev/sellers)
- [Pursekeeper ClawHub release](https://clawhub.ai/pursekeeper/skills/pursekeeper)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API requests]

**Output Format:** [Markdown guidance with shell commands and JSON/HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Wallet operations require a user-provided Nano seed and balance; spending limits can be configured for paid requests.]

## Skill Version(s):

0.3.18 (source: SKILL.md frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
