## Description:

Enables agents to inspect a self-custody Ethereum wallet, preview transactions, and submit payments subject to wallet permissions and user-selected approval mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rustok](https://clawhub.ai/user/rustok)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers use this skill to review wallet balances and DeFi positions, preview Ethereum transactions, and request on-chain payments from a locally hosted wallet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous mode can spend the full wallet balance without per-payment approval.

Mitigation: Keep new connections read-only unless transaction access is needed; avoid autonomous mode for funds you cannot afford to lose and review previews before sending.

Risk: A leaked approval PIN or recovery phrase can compromise wallet control or recovery.

Mitigation: Enter the PIN and recovery phrase only in your own terminal; never paste either into agent chat, and store the recovery phrase offline.

Risk: On-chain transfers are irreversible, and a broadcast transaction may still fail while incurring fees.

Mitigation: Confirm the recipient, chain, amount and simulation before execution; verify the transaction receipt before reporting success and do not blindly retry unknown outcomes.

Risk: Installing an unverified release could expose wallet funds.

Mitigation: Review the installer and verify its signed release using an independently installed, trusted cosign verifier; refuse installation if verification fails.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/rustok/skills/wallet)
- [Rustok wallet documentation](https://github.com/rustok-org/mcp)
- [Rustok wallet caveats](https://github.com/rustok-org/mcp/blob/main/docs/CAVEATS.md)
- [Sigstore verifier installation](https://docs.sigstore.dev/cosign/system_config/installation/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance and structured wallet tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Balance and position summaries, transaction previews, and payment status; on-chain success requires independent receipt verification.]

## Skill Version(s):

0.12.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
