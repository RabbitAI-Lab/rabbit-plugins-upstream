## Description:

亚马逊-店铺FBA helps agents work with Amazon FBA eligibility, inventory, inbound shipment, and MCF fulfillment workflows through LinkFox SP-API gateway scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, operators, and developers use this skill to query and manage FBA eligibility, inventory summaries, inbound plan workflows, shipments, and multi-channel fulfillment orders through LinkFox-authenticated SP-API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform Amazon FBA write operations that may alter inventory, inbound plans, shipments, fulfillment orders, returns, or appointments.

Mitigation: Confirm every POST, PUT, DELETE, fulfillment, return, payment, or scheduling action with the user before execution.

Risk: The skill depends on LinkFox API keys, login, billing flows, and configurable LINKFOX_* endpoint variables.

Mitigation: Use the skill only with trusted LinkFox accounts, keep API keys out of shared output, and verify endpoint variables point to official LinkFox hosts before use.

Risk: Full API responses are saved to local linkfox data files and may contain sensitive Amazon seller business records.

Mitigation: Treat saved response files as sensitive, review them before sharing, and avoid uploading them to external systems unless approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-fba)
- [API and gateway reference](references/api.md)
- [Capability matrix](references/capabilities.md)
- [Operations registry](references/operations.json)
- [Amazon getItemEligibilityPreview](https://developer-docs.amazon.com/sp-api/reference/getitemeligibilitypreview)
- [Amazon FBA Inventory v1](https://developer-docs.amazon.com/sp-api/reference/fba-inventory-v1)
- [Amazon Fulfillment Inbound v2024-03-20](https://developer-docs.amazon.com/sp-api/reference/fulfillment-inbound-v2024-03-20)
- [Amazon Fulfillment Inbound v0](https://developer-docs.amazon.com/sp-api/reference/fulfillment-inbound-v0)
- [Amazon Fulfillment Outbound 2020-07-01](https://developer-docs.amazon.com/sp-api/reference/fulfillment-outbound-2020-07-01)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are saved under linkfox session data files; responses larger than 8KB are summarized unless inline output is requested.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
