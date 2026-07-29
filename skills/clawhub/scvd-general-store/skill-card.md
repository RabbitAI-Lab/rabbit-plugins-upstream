## Description: <br>
SCVD General Store helps agents use free or paid HTTPS services at scvd.store for signed artifacts, context anchors, URL checks, x402 payment tests, and optional human-labor requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seancrecord](https://clawhub.ai/user/seancrecord) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents and developers use this skill to discover scvd.store services and make free or paid HTTPS or MCP requests for signed artifacts, live x402 payment testing, persistent context anchors, URL checks, and human-assisted tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide an agent to spend real USDC through wallet-signed x402 payments. <br>
Mitigation: Require explicit approval before any paid purchase and confirm the item, amount, network, and recipient before signing. <br>
Risk: Requests may send summaries, URLs, messages, or callback URLs to scvd.store. <br>
Mitigation: Review request payloads before sending them and do not submit secrets or sensitive personal or business information. <br>
Risk: Prices, stock, fulfillment state, and service availability can change on the external store. <br>
Mitigation: Fetch the current menu or relevant endpoint response before relying on price, availability, or fulfillment expectations. <br>


## Reference(s): <br>
- [SCVD General Store](https://scvd.store) <br>
- [SCVD menu](https://scvd.store/menu.json) <br>
- [SCVD practice counter](https://scvd.store/try) <br>
- [SCVD listing spec schema](https://scvd.store/schemas/listing-spec-v1.json) <br>
- [SCVD public stats](https://scvd.store/stats) <br>
- [SCVD signing key](https://scvd.store/.well-known/scvd-signing-key) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls] <br>
**Output Format:** [Markdown guidance with HTTPS endpoint examples and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May involve external HTTPS requests, wallet-signed x402 payments, and optional callback URLs.] <br>

## Skill Version(s): <br>
2.4.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
