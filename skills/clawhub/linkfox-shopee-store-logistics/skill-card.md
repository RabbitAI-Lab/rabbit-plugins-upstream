## Description:

Connects an agent to LinkFox's Shopee logistics gateway to ship orders, retrieve tracking numbers, create and download shipping documents, and manage logistics settings for authorized Shopee stores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee store operators and their agents use this skill to prepare shipments, create or download labels, retrieve tracking information, and manage logistics addresses, channels, operating hours, and related settings for authorized stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change live Shopee store logistics, including shipping orders, address or channel settings, and operating hours.

Mitigation: Require explicit human confirmation before mutating actions such as shipping, bulk shipping, deleting or updating addresses, changing channels, or changing operating hours.

Risk: API responses may contain store, customer, shipment, phone, credential, or payment-adjacent data and are stored locally.

Mitigation: Treat API keys, phone numbers, SMS codes, and saved responses as secrets; avoid sharing terminal output, avoid inline output unless needed, and periodically delete local LinkFox response directories.

Risk: The integration depends on LinkFox as the gateway for Shopee store data.

Mitigation: Install only if the operator trusts LinkFox for the connected store and has configured the required authorization skill and API key.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-logistics)
- [Shopee Open Platform Logistics reference](https://open.shopee.com/documents/v2/v2.logistics.get_shipping_parameter?module=95&type=1)
- [Logistics API reference](artifact/references/api.md)
- [Authorization and onboarding guide](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON responses saved to local files, with stdout JSON or summaries and occasional Markdown guidance with shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are stored in a local LinkFox session directory; large responses print summaries unless inline output is requested.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
