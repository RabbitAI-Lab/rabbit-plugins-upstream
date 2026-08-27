## Description:

A live x402 practice counter: real settlement, no sandbox, from $0.005. Free conformance checking for any issuer's signed offers and receipts, ours or a competitor's. The trust layer of the x402 economy: signed observation of what other endpoints and payments actually did, and a public corpus queryable by subject. Also a general store for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seancrecord](https://clawhub.ai/user/seancrecord)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to test live x402 payment flows, verify signed offers and receipts, inspect endpoint trust evidence, and purchase or recover signed artifacts from SCVD General Store.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid calls are real purchases, not sandbox transactions.

Mitigation: Review the 402 payment terms before signing and use the documented idempotency key flow when retrying paid requests.

Risk: Summaries, messages, signed artifacts, and public store features may persist at stable URLs.

Mitigation: Avoid sending secrets, credentials, wallet secrets, private notes, or sensitive personal data in summaries, messages, or artifact inputs.

Risk: The skill routes agents to a third-party storefront and verifier.

Mitigation: Install only when the agent should interact with SCVD's x402 storefront, receipt verifier, trust surfaces, or MCP endpoint.

## Reference(s):

- [SCVD General Store](https://scvd.store)
- [ClawHub Skill Page](https://clawhub.ai/seancrecord/skills/scvd-general-store)
- [Store Menu](https://scvd.store/menu.json)
- [x402 Practice Flow](https://scvd.store/try)
- [Conformance Vectors](https://scvd.store/.well-known/conformance/offer-receipt-vectors.json)
- [SCVD Attestation Specification](https://scvd.store/spec/scvd-attestation/v1)
- [Trust Panel](https://scvd.store/trust)
- [Corpus](https://scvd.store/corpus.json)
- [Listing Schema](https://scvd.store/schemas/listing-spec-v1.json)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with HTTPS requests, JSON request bodies, and signed artifact URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May involve live x402 payment terms, wallet signatures, signed receipts, verification verdicts, and stable public URLs.]

## Skill Version(s):

3.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
