## Description: <br>
SCVD General Store helps agents test live x402 payments, verify signed offers and receipts, and buy signed artifacts or human-assisted services using USDC on Base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seancrecord](https://clawhub.ai/user/seancrecord) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and autonomous-agent builders use this skill to exercise real x402 payment flows, verify signed x402 artifacts, and reach store endpoints for paid or free agent-oriented services. It is also useful when an agent needs signed third-party evidence, a memory anchor, a public record, or human-assisted fulfillment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid flows settle real USDC on Base. <br>
Mitigation: Read the live item terms before signing and treat every payment request as real money. <br>
Risk: Retries can duplicate paid requests when clients do not preserve idempotency. <br>
Mitigation: Use the documented idempotency key behavior for paid requests to avoid duplicate charges. <br>
Risk: Public or human-read endpoints may expose submitted content. <br>
Mitigation: Avoid sending sensitive content unless that disclosure is intended. <br>
Risk: External bridge code is outside the scanned artifact. <br>
Mitigation: Inspect any external bridge repository separately before running it. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/seancrecord/skills/scvd-general-store) <br>
- [SCVD Store](https://scvd.store) <br>
- [x402 practice flow](https://scvd.store/try) <br>
- [Menu source of truth](https://scvd.store/menu.json) <br>
- [x402 conformance API](https://scvd.store/api/conformance/v1) <br>
- [x402 conformance vectors](https://scvd.store/.well-known/conformance/offer-receipt-vectors.json) <br>
- [SCVD signing key](https://scvd.store/.well-known/scvd-signing-key) <br>
- [Attestation model](https://scvd.store/attestation) <br>
- [Corrections log](https://scvd.store/corrections) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with HTTPS request examples, JSON payloads, endpoint references, and integration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may direct agents to live paid endpoints; payment flows settle real USDC on Base.] <br>

## Skill Version(s): <br>
2.9.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
