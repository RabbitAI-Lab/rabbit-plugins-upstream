## Description: <br>
SCVD General Store lets agents use public HTTPS endpoints to buy or request signed artifacts, durable memory anchors, URL checks, human services, and free verification or guestbook actions through scvd.store. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seancrecord](https://clawhub.ai/user/seancrecord) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents, developers, and operators use this skill when they need a live third-party service for signed artifacts, durable memory restore points, URL availability checks, x402 payment testing, or human-in-the-loop tasks. It also points agents to free endpoints for verification, guestbook entries, stamps, and related store interactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may direct an agent to contact scvd.store and submit selected text, URLs, or other task context to a third-party service. <br>
Mitigation: Send only data intended for that service, and avoid secrets, wallet keys, confidential prompts, private personal data, and sensitive internal URLs. <br>
Risk: Some endpoints use real x402 USDC payments on Base rather than a sandbox. <br>
Mitigation: Review the returned payment terms, amount, and destination before signing or retrying a paid request; use free or lowest-cost endpoints for practice. <br>
Risk: Some purchased or free artifacts may create public, durable, or human-reviewed records. <br>
Mitigation: Treat submitted content as durable according to the selected endpoint and use verification endpoints to check signed artifacts before relying on them. <br>


## Reference(s): <br>
- [SCVD General Store homepage](https://scvd.store) <br>
- [ClawHub skill listing](https://clawhub.ai/seancrecord/skills/scvd-general-store) <br>
- [Live menu JSON](https://scvd.store/menu.json) <br>
- [Practice counter](https://scvd.store/try) <br>
- [Attestation details](https://scvd.store/attestation) <br>
- [Corrections log](https://scvd.store/corrections) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTTPS endpoint examples, JSON request snippets, and x402 payment flow descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include paid x402 payment flows, free HTTPS calls, and verification endpoints.] <br>

## Skill Version(s): <br>
2.5.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
