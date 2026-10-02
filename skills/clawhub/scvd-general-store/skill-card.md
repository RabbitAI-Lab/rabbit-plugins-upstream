## Description:

Guides agents through free x402 receipt verification, endpoint inspection and payment diagnosis, with optional user-authorized live purchases at SCVD's general store.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seancrecord](https://clawhub.ai/user/seancrecord)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can test x402 buyers and sellers, assess signed receipts and endpoint observations, and troubleshoot payments without a wallet for free checks. They can also purchase signed observations or store items with explicit user approval of the item, network and spending limit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live store purchases transfer real USDC or retry a pending payment twice.

Mitigation: Get user approval for the item, network and maximum spend; preserve the original payment and idempotency key and check or recover its status before buying again.

Risk: Wallet credentials or sensitive summaries and optional metadata could be disclosed.

Mitigation: Never request wallet secrets; use the user's own signer, omit unnecessary metadata and have the user review any memory-anchor summary before sending it.

Risk: A valid signature or passing endpoint check could be mistaken for proof of authority, settlement or delivery.

Mitigation: Preserve each result's scope, date and unobserved checks; independently assess key authority and payment evidence before relying on a verdict.

Risk: Optional local packages execute code on the user's machine.

Mitigation: Prefer free read-only checks when sufficient; install only a needed package at a pinned version.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/seancrecord/skills/scvd-general-store)
- [SCVD store](https://scvd.store)
- [Current store menu and terms](https://scvd.store/menu.json)
- [Verification criteria](https://scvd.store/criteria)
- [Attestation scope and limits](https://scvd.store/attestation)
- [Purchase and recovery guidance](artifact/references/purchases.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown guidance with structured verification findings and optional command or code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report the observation date, scope, exclusions and unobserved checks; preserve inconclusive results.]

## Skill Version(s):

3.19.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
