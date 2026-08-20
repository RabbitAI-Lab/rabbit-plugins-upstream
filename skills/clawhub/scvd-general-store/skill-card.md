## Description:

SCVD General Store guides agents through scvd.store's live x402 payment, conformance, attestation, timestamping, and general-store endpoints, including free verification paths and paid real-settlement flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seancrecord](https://clawhub.ai/user/seancrecord)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to test x402 payment clients against a live counterparty, check signed offers and receipts, request settlement attestations, and discover related scvd.store or MCP endpoints. It is most useful when the caller needs real settlement behavior, signed observations, or concise recipes for public HTTPS endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to make real paid x402 wallet calls.

Mitigation: Treat paid calls as real purchases, keep wallet approval controls enabled, and prefer free conformance or preflight endpoints before spending.

Risk: Optional scvd-tab or npm setup is separate from the core public HTTPS endpoint flow.

Mitigation: Review optional scvd-tab or npm installation separately before installing or running it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/seancrecord/skills/scvd-general-store)
- [SCVD Store](https://scvd.store)
- [x402 Practice Flow](https://scvd.store/try)
- [Conformance Vectors](https://scvd.store/.well-known/conformance/offer-receipt-vectors.json)
- [SCVD Attestation Spec](https://scvd.store/spec/scvd-attestation/v1)
- [Attestation Trust Model](https://scvd.store/attestation)
- [Signing Key](https://scvd.store/.well-known/scvd-signing-key)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, text]

**Output Format:** [Markdown guidance with HTTPS endpoint examples, JSON request snippets, and optional MCP configuration notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe real paid x402 calls; callers should keep wallet approval controls enabled.]

## Skill Version(s):

3.3.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
