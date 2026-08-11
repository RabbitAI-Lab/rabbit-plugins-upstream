## Description:

Helps agents work with Shopee FirstMile logistics for authorized stores, including finding unbound orders, generating or binding first-mile tracking numbers, retrieving waybills, and checking channels or transit warehouses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, logistics operators, and support agents use this skill to manage Shopee cross-border FirstMile shipment workflows for already-authorized stores. It is intended for order-level logistics operations such as generating tracking numbers, binding or unbinding first-mile shipments, and retrieving waybill or channel information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox account credentials and Shopee store logistics data.

Mitigation: Install and run it only when the publisher and LinkFox service are trusted for the stores and data involved.

Risk: Generated API keys, payment QR flows, and account onboarding outputs are sensitive.

Mitigation: Treat keys, QR codes, payment URLs, phone numbers, and login codes as secrets and avoid sharing them in prompts, logs, or public workspaces.

Risk: Bind, unbind, and tracking-number generation actions can change shipment state.

Mitigation: Confirm the target store, order identifiers, and intended operation before running any mutating FirstMile command.

Risk: Endpoint override environment variables can redirect calls away from the default LinkFox gateway.

Mitigation: Use endpoint overrides only for destinations controlled by the operator.

Risk: Local response archives may contain order or shipment data.

Mitigation: Plan retention and deletion of generated linkfox response files according to the user's data-handling requirements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-first-mile)
- [Shopee FirstMile API Overview](references/api.md)
- [Shopee FirstMile Official Documentation](https://open.shopee.com/documents/v2/v2.first_mile.get_unbind_order_list?module=96&type=1)
- [Authentication and Billing Onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, shell commands, and JSON API responses saved to local files or printed as summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Shopee order, shipment, waybill, channel, warehouse, billing, or authentication details; large responses are summarized while full JSON is written to a local linkfox archive.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
