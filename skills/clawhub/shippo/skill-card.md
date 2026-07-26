## Description: <br>
A shipping and logistics skill for Shippo that helps agents get multi-carrier rates, buy domestic and international labels, validate addresses, track packages, run batch shipping, and provide shipping integration guidance through Shippo's hosted MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shippo](https://clawhub.ai/user/shippo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and operations teams use this skill to connect agents to Shippo for rate shopping, address validation, label purchase, tracking, customs workflows, batch shipping, cost analysis, and shipping integration guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Label and batch purchases can charge the connected Shippo account. <br>
Mitigation: Require explicit user confirmation of carrier, service, cost, estimated delivery time, origin, and destination before any purchase action. <br>
Risk: Shipment CSVs, labels, tracking records, and support tickets may include customer shipping data. <br>
Mitigation: Minimize copied shipping data, avoid exposing unnecessary names or street lines, and keep persistence within Shippo's API and the user's authorized account. <br>
Risk: Incorrect shipment, customs, or parcel details can produce failed labels, delays, or wrong charges. <br>
Mitigation: Validate addresses before label purchase, ask for missing customs and parcel details, and use the operation schemas before executing Shippo MCP calls. <br>


## Reference(s): <br>
- [Shippo AI repository](https://github.com/goshippo/ai) <br>
- [Shippo hosted MCP server](https://mcp.shippo.com) <br>
- [Shippo API Concepts](https://docs.goshippo.com/docs/api_concepts/apiversioning) <br>
- [Shippo Address Validation Guide](https://docs.goshippo.com/docs/addresses/address_validation) <br>
- [Shippo Customs Reference](https://docs.goshippo.com/docs/exporting/internationalshipments) <br>
- [Shippo Carrier Accounts](https://docs.goshippo.com/docs/shipping/carrieraccounts) <br>
- [Shippo Webhooks](https://docs.goshippo.com/docs/tracking/webhooks) <br>
- [Carrier Guide](references/carrier-guide.md) <br>
- [CSV Batch Format Specification](references/csv-format.md) <br>
- [Customs Declaration Guide](references/customs-guide.md) <br>
- [Shippo MCP Operation Reference](references/tool-reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline JSON, code, and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include complete label URLs, tracking numbers, validation summaries, rate tables, purchase confirmation prompts, CSV validation reports, and integration guidance.] <br>

## Skill Version(s): <br>
1.4.4 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
