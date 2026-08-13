## Description:

A live x402 practice counter: real settlement, no sandbox, from $0.005. Free conformance checking for any issuer's signed offers and receipts, ours or a competitor's. The trust layer of the x402 economy: signed observation of what other endpoints and payments actually did, and a public corpus queryable by subject. Also a general store for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seancrecord](https://clawhub.ai/user/seancrecord)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agents use this skill to test x402 payment flows against live public HTTPS endpoints, check signed offer and receipt conformance, and request signed observations, attestations, or store artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid flows use real settlement rather than a sandbox.

Mitigation: Only sign payments the operator intends to make, and prefer the free checks or lowest-cost practice endpoint before higher-value purchases.

Risk: Wallet secrets or credentials could be exposed if an agent treats payment setup carelessly.

Mitigation: Do not provide wallet secrets, private keys, credentials, or recovery material; use normal wallet signing controls for each intended payment.

Risk: Some artifacts, observations, guestbook entries, certificates, or corpus records may be public or permanent.

Mitigation: Avoid submitting sensitive, private, or regulated information to public endpoints unless the operator has explicitly accepted that disclosure.

Risk: Automated retries can unintentionally repeat paid requests.

Mitigation: Use the documented idempotency key behavior for paid retries and inspect returned terms before signing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seancrecord/skills/scvd-general-store)
- [SCVD General Store](https://scvd.store)
- [x402 practice flow](https://scvd.store/try)
- [Live menu](https://scvd.store/menu.json)
- [Offer and receipt conformance vectors](https://scvd.store/.well-known/conformance/offer-receipt-vectors.json)
- [SCVD attestation specification](https://scvd.store/spec/scvd-attestation/v1)
- [Attestation trust model](https://scvd.store/attestation)
- [Signing key](https://scvd.store/.well-known/scvd-signing-key)
- [Public corpus](https://scvd.store/corpus.json)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration]

**Output Format:** [Markdown with HTTPS request examples and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may lead agents to call public scvd.store endpoints; paid flows require intentional wallet signing.]

## Skill Version(s):

3.1.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
