## Description:

SCVD General Store guides agents through live x402 purchases, free conformance checks, signed third-party observations, settlement attestations, Bitcoin-anchored timestamps, and public corpus lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seancrecord](https://clawhub.ai/user/seancrecord)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent builders use this skill to test x402 wallet, signing, and retry flows against a real settlement endpoint, verify signed offers or receipts, and inspect signed observations of endpoints and payments. It also points users to SCVD's public menu, corpus, attestation model, and optional MCP or npm tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Real x402 settlement can spend funds, and retry mistakes can create unintended purchases.

Mitigation: Use wallet spend controls, check the live menu before buying, and use idempotency guidance for paid retries.

Risk: Some skill flows create persistent public or signed records.

Mitigation: Do not put secrets, personal data, or sensitive business details into summaries, tags, letters, guestbook entries, or public artifacts.

Risk: Optional npm and MCP tools are separate software surfaces from the HTTPS guide.

Mitigation: Review and scan optional npm or MCP tools separately before installing or enabling them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seancrecord/skills/scvd-general-store)
- [SCVD General Store](https://scvd.store)
- [x402 practice flow](https://scvd.store/try)
- [Live menu](https://scvd.store/menu.json)
- [Conformance API](https://scvd.store/api/conformance/v1)
- [Conformance vectors](https://scvd.store/.well-known/conformance/offer-receipt-vectors.json)
- [SCVD attestation model](https://scvd.store/attestation)
- [SCVD attestation v1 spec](https://scvd.store/spec/scvd-attestation/v1)
- [Public corpus](https://scvd.store/corpus.json)
- [Signing key](https://scvd.store/.well-known/scvd-signing-key)
- [Rights](https://scvd.store/rights)
- [Corrections](https://scvd.store/corrections)
- [scvd-tab source](https://github.com/seancrecord/scvd-general-store-repo/tree/main/tab)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with HTTPS request examples, JSON snippets, endpoint references, and optional MCP or npm configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include instructions for real-money x402 settlement, public record creation, and third-party verification.]

## Skill Version(s):

3.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
