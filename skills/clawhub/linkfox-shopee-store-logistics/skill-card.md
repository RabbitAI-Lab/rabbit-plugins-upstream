## Description:

Provides agent guidance and scripts for Shopee store logistics tasks, including shipping parameters, shipment creation, tracking numbers, shipping documents, pickup addresses, and logistics channels through LinkFox gateway calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to manage authorized Shopee store logistics workflows such as preparing shipments, retrieving tracking details, creating shipping documents, and checking store logistics settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform live Shopee logistics actions, including shipment, address, tracking, and document operations.

Mitigation: Install only if you trust LinkFox and confirm shipment, address, and tracking changes before running scripts.

Risk: The skill depends on API keys and configurable gateway URLs.

Mitigation: Configure API keys and gateway URLs carefully, keep credentials out of prompts and shared logs, and rotate keys if exposure is suspected.

Risk: The onboarding helpers include phone-login and payment flows.

Mitigation: Use those helpers only when you explicitly want the agent to handle account setup or purchases.

Risk: Saved response files may contain customer, order, or logistics data.

Mitigation: Review local linkfox response files for sensitive content and periodically delete them when they are no longer needed.

## Reference(s):

- [Shopee Open Platform Logistics Documentation](https://open.shopee.com/documents/v2/v2.logistics.get_shipping_parameter?module=95&type=1)
- [Logistics API Reference](references/api.md)
- [Onboarding and Authentication Guidance](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Files, Configuration]

**Output Format:** [Markdown guidance with shell commands, JSON inputs and responses, and saved response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full API responses under a local linkfox session data directory and may print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
