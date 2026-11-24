## Description:

Bloom lets agents read financial state and stage payments, trades, and other digital asset actions, with transactions requiring the user's passkey or a signed Sealed Approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bloom-directory](https://clawhub.ai/user/bloom-directory)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use Bloom to inspect balances and positions, manage wallets, and stage payments, swaps, trades, lending, or prediction market actions across EVM chains and Solana. Transactions require approval through the user's passkey or a signed Sealed Approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payments, trades, and other financial actions can move digital assets.

Mitigation: Review each proposed action and approve transactions with the user's passkey or a signed Sealed Approval; never request or handle private keys, seed phrases, passwords, or passkey secrets.

## Reference(s):

- [Bloom](https://bloom.directory)
- [Bloom on ClawHub](https://clawhub.ai/bloom-directory/skills/bloom)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Financial action proposals]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Financial actions are staged for user approval.]

## Skill Version(s):

0.5.1 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
