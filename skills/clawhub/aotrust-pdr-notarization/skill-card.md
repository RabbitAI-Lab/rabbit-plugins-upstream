## Description:

Creates and verifies cryptographic proof-of-existence receipts for digital artifacts when a user explicitly requests notarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gitserge-crypto](https://clawhub.ai/user/gitserge-crypto)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers use this skill to request a timestamped proof for a specific artifact hash and later verify the resulting receipt. Paid notarization requires explicit user consent and a wallet-approved payment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact hash is sent to AOTrust and may be publicly visible in the proof.

Mitigation: Only submit the hash when the user explicitly requests proof for that specific artifact; do not upload the artifact itself.

Risk: Paid notarization incurs an irreversible $0.01 USDC charge.

Mitigation: Before each payment, confirm the exact hash, destination, chain and charge with the user; require manual wallet approval and never authorize unattended signing.

## Reference(s):

- [AOTrust MCP endpoint](https://api.aotrust.link/mcp)
- [AOTrust HTTP notarization endpoint](https://api.aotrust.link/notarize)
- [AOTrust PDR verification endpoint](https://api.aotrust.link/v1/pdr/verify)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Text summary with a proof receipt and verification result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Receipt includes a public artifact hash; paid proofs cost $0.01 USDC.]

## Skill Version(s):

3.9.1 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
