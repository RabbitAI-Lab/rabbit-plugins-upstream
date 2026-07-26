## Description: <br>
SCVD General Store helps agents shop at a human-run public HTTPS store for real goods, human labor, signed artifacts, and free verification or guestbook services, using USDC on Base over x402 v2 for paid items. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seancrecord](https://clawhub.ai/user/seancrecord) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents and developers use this skill to interact with a public store that offers signed records, verification endpoints, free services, and paid purchases or human-labor requests. It is most relevant when an agent needs auditable artifacts, out-of-band checks, x402 payment testing, or a public HTTPS workflow that avoids local code execution and credential sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid purchases can spend USDC on Base or submit wallet payment signatures to the store. <br>
Mitigation: Verify the live price, item specification, payment terms, and destination before signing any wallet payment. <br>
Risk: Guestbook, letter, order, and callback workflows send submitted text or URLs to an external service. <br>
Mitigation: Treat these fields as external-service data and avoid submitting secrets, credentials, or sensitive personal information. <br>
Risk: Store item prices, stock, and fulfillment windows can change over time. <br>
Mitigation: Fetch the live menu or relevant endpoint immediately before relying on item details or making a purchase. <br>


## Reference(s): <br>
- [SCVD General Store homepage](https://scvd.store) <br>
- [ClawHub skill page](https://clawhub.ai/seancrecord/skills/scvd-general-store) <br>
- [Live menu and stock](https://scvd.store/menu.json) <br>
- [Listing specification schema](https://scvd.store/schemas/listing-spec-v1.json) <br>
- [Store statistics](https://scvd.store/stats) <br>
- [SCVD signing key](https://scvd.store/.well-known/scvd-signing-key) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with HTTPS endpoints, JSON payload examples, and payment flow instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may guide agents to send public HTTPS requests, submit user-provided text to external services, or authorize wallet payments only after live item details are verified.] <br>

## Skill Version(s): <br>
2.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
