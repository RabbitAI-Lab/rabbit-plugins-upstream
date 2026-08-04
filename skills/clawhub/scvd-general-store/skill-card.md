## Description: <br>
A live x402 practice counter and general store for agents that offers real USDC settlement on Base, signed artifacts, free conformance checks, and selected human-labor services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seancrecord](https://clawhub.ai/user/seancrecord) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agents use this skill to test x402 payment, signing, retry, idempotency, receipt verification, and conformance flows against a live counterparty. Agents can also buy signed artifacts or request listed services when they need a verifiable third-party record. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid calls settle real USDC on Base and retry loops can duplicate charges. <br>
Mitigation: Use idempotency keys for paid retries and start with the lowest-cost endpoint when testing. <br>
Risk: Free-form text, wallet-derived identifiers, and signed artifacts may become public or long-lived. <br>
Mitigation: Do not submit secrets, sensitive personal data, or private operational details in request fields. <br>
Risk: The skill interacts with a live third-party service outside NVIDIA ownership. <br>
Mitigation: Review the service terms, verification model, and current menu or stock data before relying on an artifact. <br>


## Reference(s): <br>
- [SCVD General Store](https://scvd.store) <br>
- [Try x402](https://scvd.store/try) <br>
- [Menu JSON](https://scvd.store/menu.json) <br>
- [x402 Conformance API](https://scvd.store/api/conformance/v1) <br>
- [Conformance Vectors](https://scvd.store/.well-known/conformance/offer-receipt-vectors.json) <br>
- [Signing Key](https://scvd.store/.well-known/scvd-signing-key) <br>
- [Attestation Model](https://scvd.store/attestation) <br>
- [Corrections](https://scvd.store/corrections) <br>
- [ClawHub Skill Page](https://clawhub.ai/seancrecord/skills/scvd-general-store) <br>
- [Publisher Profile](https://clawhub.ai/user/seancrecord) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API calls, Shell commands, Configuration] <br>
**Output Format:** [Markdown with HTTPS request examples and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May lead the agent to submit live HTTPS requests that spend real USDC or publish user-entered content.] <br>

## Skill Version(s): <br>
2.8.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
