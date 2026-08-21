## Description:

Decision Gate Verifier lets agents request independent checks that an action matched a previously committed claim, returning a signed PASS, REFUSE, or IN_DOUBT receipt anchored on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vaahl-dev](https://clawhub.ai/user/vaahl-dev)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this paid verifier to obtain third-party receipts for policy conformance around actions such as donations, payouts, autonomous spending, and irreversible releases. The skill is intended for workflows where a self-authored audit log is not enough evidence for a reviewer or counterparty.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to handle wallet private keys and sign live USDC payment authorizations.

Mitigation: Use a limited wallet, avoid high-value private keys, and verify payment amount, token, chain, and recipient before signing.

Risk: Broad trigger language and paid verification calls could lead to unintended spending.

Mitigation: Require explicit user confirmation or a spending budget before invoking paid checks.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/vaahl-dev/skills/decision-gate-verifier)
- [Decision Gate product page](https://soulscore.xyz/decision-gate?src=clawhub)
- [Soulscore methodology](https://soulscore.xyz/methodology?src=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown instructions, Python code examples, shell command snippets, configuration details, and JSON receipt objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Receipts include verdict data intended to be independently reproduced or anchored on Base.]

## Skill Version(s):

0.4.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
