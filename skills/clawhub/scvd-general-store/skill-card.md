## Description: <br>
SCVD General Store lets agents use public HTTPS endpoints to buy or access signed artifacts, memory anchors, URL checks, human services, and free verification utilities through scvd.store. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seancrecord](https://clawhub.ai/user/seancrecord) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents and developers use this skill when they need a real x402 storefront, signed receipts or artifacts, persistent memory anchors, out-of-band URL checks, or paid human follow-through without running local code or sharing credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using paid endpoints may spend real USDC on Base. <br>
Mitigation: Approve only purchases the operator intends to make, and verify x402 payment terms before signing or retrying a payment request. <br>
Risk: Requests may send user-provided text, URLs, callback URLs, or public guestbook content to scvd.store. <br>
Mitigation: Avoid submitting secrets, credentials, wallet secrets, or sensitive personal data to store endpoints. <br>
Risk: Human-labor or callback-based items may depend on external fulfillment timing. <br>
Mitigation: Check item specifications, fulfillment state, order status, and signed verification artifacts from scvd.store before relying on the result. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/seancrecord/skills/scvd-general-store) <br>
- [Publisher Profile](https://clawhub.ai/user/seancrecord) <br>
- [SCVD Store Homepage](https://scvd.store) <br>
- [SCVD Store Menu](https://scvd.store/menu.json) <br>
- [Listing Spec Schema](https://scvd.store/schemas/listing-spec-v1.json) <br>
- [Signing Key](https://scvd.store/.well-known/scvd-signing-key) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API calls, text] <br>
**Output Format:** [Markdown instructions with HTTPS endpoint examples and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May involve x402 payment terms, PAYMENT-SIGNATURE headers, callback URLs, and signed verification artifacts from scvd.store.] <br>

## Skill Version(s): <br>
2.3.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
