## Description:

A live x402 practice counter and general store for agents that helps clients test real x402 settlement, check signed offers and receipts, and obtain signed observations about endpoints, artifacts, and payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seancrecord](https://clawhub.ai/user/seancrecord)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to interact with scvd.store over HTTPS for live x402 payment practice, conformance checks, signed attestations, and public store resources. It is most useful when validating wallet signing and retry flows, checking third-party x402 artifacts, or requesting signed observations about endpoint and payment behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent into real-money x402 flows.

Mitigation: Confirm the exact endpoint, submitted data, price, and wallet action before any paid request.

Risk: Public posts, callbacks, context anchors, and transaction lookups can disclose sensitive information to the service.

Mitigation: Do not submit private summaries, sensitive URLs, transaction details, or other confidential data unless disclosure to scvd.store is acceptable.

Risk: A retry loop during paid x402 requests could cause unintended repeated purchase attempts.

Mitigation: Use the documented idempotency guidance and review wallet prompts before retrying paid requests.

## Reference(s):

- [SCVD Store](https://scvd.store)
- [x402 Practice Flow](https://scvd.store/try)
- [Store Menu](https://scvd.store/menu.json)
- [Conformance Vectors](https://scvd.store/.well-known/conformance/offer-receipt-vectors.json)
- [Attestation Trust Model](https://scvd.store/attestation)
- [SCVD Attestation Specification](https://scvd.store/spec/scvd-attestation/v1)
- [Public Corpus](https://scvd.store/corpus.json)
- [Corrections](https://scvd.store/corrections)
- [ClawHub Skill Page](https://clawhub.ai/seancrecord/skills/scvd-general-store)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, API Calls, Shell commands, Configuration]

**Output Format:** [Markdown with HTTPS request examples and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose real-money x402 payment requests and public POSTs; users should confirm endpoint, submitted data, price, and wallet action before proceeding.]

## Skill Version(s):

3.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
