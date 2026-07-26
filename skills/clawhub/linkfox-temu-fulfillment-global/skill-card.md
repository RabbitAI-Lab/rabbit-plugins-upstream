## Description: <br>
Temu Global fulfillment API helper for Buy-Shipping labels, co-warehouse fulfillment, seller self-fulfilled shipments, logistics tracking, and related shipment workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Temu sellers and commerce operations agents use this skill to run Global, non-US/EU fulfillment tasks through LinkFox: buying shipping labels, submitting or canceling co-warehouse fulfillment, confirming or updating seller-fulfilled shipments, scheduling pickups, downloading labels, and checking tracking. <br>

### Deployment Geography for Use: <br>
Global, excluding US and EU fulfillment flows documented as separate related skills. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform live fulfillment actions such as creating, confirming, updating, or canceling shipments. <br>
Mitigation: Require explicit user confirmation before any create, confirm, update, cancel, or pickup-reservation action. <br>
Risk: The skill handles LinkFox and Temu credentials and can store Temu access tokens locally. <br>
Mitigation: Use a dedicated least-privilege token, avoid sharing tokens in shell history or transcripts, and review local token storage before use. <br>
Risk: API responses are saved to local JSON files that may contain fulfillment or customer-operation data. <br>
Mitigation: Keep generated response files out of version control and clean up session data after the fulfillment task is complete. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-fulfillment-global) <br>
- [API reference](references/api.md) <br>
- [Partner Global fulfillment catalog](references/partner-global-catalog.md) <br>
- [Temu access token guide](references/access-token.md) <br>
- [API document index](references/apis/README.md) <br>
- [Temu Partner Global documentation](https://partner-global.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON request examples, shell commands, and saved JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts write complete responses under a local linkfox session data directory and print either full JSON or a summary depending on response size.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
