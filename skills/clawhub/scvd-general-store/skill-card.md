## Description: <br>
SCVD General Store helps agents buy third-party verifiable signed artifacts, persistent memory anchors, URL checks, and human-performed tasks through public HTTPS endpoints, with optional paid USDC settlement on Base and free verification or visit endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seancrecord](https://clawhub.ai/user/seancrecord) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents and developers use this skill when they need a live external service for verifiable artifacts, durable context anchors, out-of-band URL checks, or human labor such as phone calls and app reviews. It is also useful for testing x402 payment flows against a real counterparty before larger spending. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead an agent to use an external paid HTTPS service where purchases spend real USDC on Base. <br>
Mitigation: Approve spending deliberately, check the live menu and payment terms before retrying with a payment signature, and use free endpoints or low-cost practice purchases when testing. <br>
Risk: Inputs sent to the service may become external records or may be read by the service. <br>
Mitigation: Avoid sending sensitive private data unless disclosure to the service and any resulting record is intended. <br>
Risk: The skill depends on an external service for fulfillment, verification, availability, and human-labor timing. <br>
Mitigation: Use the service's verification endpoint for signed artifacts, poll order status when applicable, and rely on live menu or stock data rather than static counts. <br>


## Reference(s): <br>
- [SCVD General Store homepage](https://scvd.store) <br>
- [ClawHub skill page](https://clawhub.ai/seancrecord/skills/scvd-general-store) <br>
- [Live menu and stock](https://scvd.store/menu.json) <br>
- [Practice counter](https://scvd.store/try) <br>
- [Listing spec schema](https://scvd.store/schemas/listing-spec-v1.json) <br>
- [Public stats](https://scvd.store/stats) <br>
- [Signing key](https://scvd.store/.well-known/scvd-signing-key) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration] <br>
**Output Format:** [Markdown instructions with HTTPS endpoints, JSON request examples, and payment-flow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct agents to external public HTTPS endpoints and paid x402 flows; some items return signed artifacts or order identifiers.] <br>

## Skill Version(s): <br>
2.4.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
