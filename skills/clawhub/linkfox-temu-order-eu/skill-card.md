## Description:

Provides agent guidance and scripts for querying and managing Temu EU order data through the LinkFox gateway, including order lists, details, shipping information, order amounts, combined shipment groups, customization data, and SN/IMEI verification upload.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to work with Temu EU order-management APIs through LinkFox, retrieve order and shipping data, perform order amount checks, inspect customization details, and upload verification information for eligible orders.

### Deployment Geography for Use:

Europe

## Known Risks and Mitigations:

Risk: The security evidence reports that full order responses and optional Temu tokens may be written locally.

Mitigation: Use the skill only in a trusted workspace, protect or delete generated LinkFox data and token-store files after use, and avoid storing tokens unless the workflow requires a reusable store key.

Risk: The security evidence reports broader gateway, onboarding, and payment-related capabilities that need review before installation.

Mitigation: Review requested operations before execution and use least-privilege LinkFox and Temu credentials scoped to the intended order-management task.

Risk: The security verdict is suspicious despite no enumerated risk findings.

Mitigation: Review the skill before installing or running it, and avoid the generic proxy or raw token-listing capabilities unless they are deliberately needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-order-eu)
- [API reference](references/api.md)
- [Temu accessToken authorization and retrieval](references/access-token.md)
- [Partner EU order catalog](references/partner-eu-catalog.md)
- [Per-interface API documents](references/apis/README.md)
- [Temu Partner EU documentation](https://partner-eu.temu.com/documentation?menu_code=dbd3d395963a408984b8ae7dbc5f64f9)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, API calls, JSON, configuration]

**Output Format:** [Markdown guidance with shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full API responses locally and may print either full JSON or a summarized response depending on response size and inline mode.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
