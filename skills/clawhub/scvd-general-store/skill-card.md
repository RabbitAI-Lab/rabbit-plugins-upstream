## Description:

SCVD General Store helps agents and developers test real x402 payments, verify signed offers and receipts, and use a live agent-commerce store and evidence observatory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seancrecord](https://clawhub.ai/user/seancrecord)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent builders use this skill to exercise x402 client behavior against a live service, inspect conformance checks, and obtain or verify signed observations about payments, endpoints, and store artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill points agents at live x402 payment flows that can transfer real USDC.

Mitigation: Require explicit human approval before any paid call, wallet signature, or submitted payment.

Risk: Persistent context or URL-based inputs may expose secrets or private conversation details to an external service.

Mitigation: Do not place credentials, private keys, seed phrases, or sensitive conversation details in context_anchor summaries, query strings, or request bodies.

Risk: The local `scvd-tab` MCP setup uses an unpinned `npx -y scvd-tab` install path.

Mitigation: Review and pin the package version first, or run it in a restricted environment.

Risk: A repeated paid request can create unintended duplicate payments if retries are not controlled.

Mitigation: Inspect the 402 terms before payment and use the documented idempotency key behavior for paid retries.

## Reference(s):

- [SCVD Store Homepage](https://scvd.store)
- [ClawHub Skill Page](https://clawhub.ai/seancrecord/skills/scvd-general-store)
- [OpenAPI Specification](https://scvd.store/openapi.json)
- [Current Store Menu](https://scvd.store/menu.json)
- [Conformance Vectors](https://scvd.store/.well-known/conformance/offer-receipt-vectors.json)
- [Attestation Format](https://scvd.store/spec/scvd-attestation/v1)
- [Trust and Signing Key](https://scvd.store/trust)
- [Attestation Scope](https://scvd.store/attestation)
- [Criteria](https://scvd.store/criteria)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, API calls, Shell commands, Configuration]

**Output Format:** [Markdown guidance with HTTPS examples, JSON request bodies, x402 payment flow steps, MCP setup notes, and shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to live external services and real-money x402 payment flows; paid actions require a buyer-authorized wallet signature.]

## Skill Version(s):

3.16.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
