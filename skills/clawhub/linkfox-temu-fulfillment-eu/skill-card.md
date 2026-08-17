## Description:

Provides an agent with Temu EU fulfillment and shipping workflows across Buy-Shipping labels, cooperative warehouse fulfillment, self-fulfilled shipments, tracking, and self-delivery POD upload and audit APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to prepare and manage Temu EU fulfillment actions, including creating shipping labels, confirming or updating shipments, managing cooperative warehouse fulfillment, checking tracking, and uploading POD evidence.

### Deployment Geography for Use:

Europe

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys, Temu access tokens, order and shipping data, onboarding, and payment-related flows.

Mitigation: Use trusted LinkFox credentials only, avoid passing real secrets in shell history, prefer environment variables or the local token store, and keep generated response files and token stores out of source control.

Risk: The skill can create, confirm, update, cancel, and upload evidence for live Temu EU shipping records.

Mitigation: Require explicit user confirmation before state-changing actions such as shipment creation, shipment confirmation, shipment updates, pickup cancellation, cooperative warehouse fulfillment changes, and POD uploads.

Risk: The security verdict requires review because the integration persists sensitive data and has broad order-shipping scope.

Mitigation: Limit use to the intended EU order-shipping workflows, review generated request payloads before execution, and inspect saved response files for sensitive content before sharing or committing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-fulfillment-eu)
- [Temu EU fulfillment API reference](references/api.md)
- [Temu access token authorization](references/access-token.md)
- [Partner EU fulfillment catalog](references/partner-eu-catalog.md)
- [Fulfillment API index](references/apis/README.md)
- [Temu Partner EU documentation](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON request or response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI scripts save complete API responses under a linkfox session data directory and print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
