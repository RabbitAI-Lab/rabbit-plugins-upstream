## Description: <br>
Helps agents use LinkFox Temu EU fulfillment APIs for buy-shipping labels, cooperative warehouse fulfillment, seller self-fulfillment, logistics tracking, and self-delivery POD workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, sellers, and fulfillment operators use this skill to prepare and execute Temu EU order-shipping workflows through LinkFox gateway calls. It supports label purchase, shipment confirmation, scan forms, pickup reservations, cooperative warehouse fulfillment, tracking, and POD upload workflows. <br>

### Deployment Geography for Use: <br>
Europe (Temu EU fulfillment workflows) <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Temu seller fulfillment tokens and LinkFox gateway credentials, which can expose sensitive account access if mishandled. <br>
Mitigation: Use limited-scope Temu tokens where possible and avoid pasting production secrets into shared chats, logs, or saved transcripts. <br>
Risk: The skill can change live fulfillment state, including shipment creation, confirmation, cancellation, and POD upload. <br>
Mitigation: Require human review before executing state-changing fulfillment actions or arbitrary proxy calls. <br>
Risk: The skill may retain Temu tokens and API response data in local files. <br>
Mitigation: Review and protect local files under linkfox data directories and ~/.linkfox, and remove retained sensitive data when it is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-fulfillment-eu) <br>
- [API reference](artifact/references/api.md) <br>
- [Access token guide](artifact/references/access-token.md) <br>
- [Authorization flow](artifact/references/authorization-flow.md) <br>
- [Partner EU fulfillment catalog](artifact/references/partner-eu-catalog.md) <br>
- [EU fulfillment API index](artifact/references/apis/README.md) <br>
- [Temu Partner EU documentation](https://partner-eu.temu.com/documentation) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON files, API calls] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON request or response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts may write full API responses under a local linkfox data directory and print either full JSON or a summary depending on response size.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
