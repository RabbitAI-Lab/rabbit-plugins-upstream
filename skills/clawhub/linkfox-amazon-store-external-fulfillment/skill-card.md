## Description:

Helps agents use LinkFox's Amazon External Fulfillment workflow to call SP-API inventory, shipment, package, invoice, label, and return operations for Seller Flex, Easy Ship, Self Ship, and related fulfillment channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and commerce automation agents use this skill to manage Amazon External Fulfillment inventory, shipments, packages, invoices, shipping labels, and returns through LinkFox-authenticated SP-API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Amazon fulfillment data, reusable LinkFox API keys, and account onboarding flows.

Mitigation: Install and use it only when the user trusts LinkFox with that data, keep endpoint environment variables pointed at trusted LinkFox HTTPS hosts, and treat stdout plus saved response files as sensitive.

Risk: Inventory, shipment, package, invoice, label, return, and payment-order actions can affect merchant operations or billing.

Mitigation: Require explicit user confirmation before write, label, invoice, package, shipment, return, or payment-order actions.

Risk: Phone-based onboarding can create or access a LinkFox account and issue an API key.

Mitigation: Ask for SMS codes only when the user intends to create or access that account, and provide the resulting API key as a secret configuration value.

## Reference(s):

- [Bundled API and gateway guide](artifact/references/api.md)
- [Bundled onboarding guide](artifact/references/onboarding.md)
- [Amazon SP-API batchInventory reference](https://developer-docs.amazon.com/sp-api/reference/batchinventory)
- [Amazon SP-API getShipments reference](https://developer-docs.amazon.com/sp-api/reference/getshipments-1)
- [Amazon SP-API getShipment reference](https://developer-docs.amazon.com/sp-api/reference/getshipment-1)
- [Amazon SP-API processShipment reference](https://developer-docs.amazon.com/sp-api/reference/processshipment)
- [Amazon SP-API createPackages reference](https://developer-docs.amazon.com/sp-api/reference/createpackages)
- [Amazon SP-API updatePackage reference](https://developer-docs.amazon.com/sp-api/reference/updatepackage)
- [Amazon SP-API updatePackageStatus reference](https://developer-docs.amazon.com/sp-api/reference/updatepackagestatus)
- [Amazon SP-API retrieveShippingOptions reference](https://developer-docs.amazon.com/sp-api/reference/retrieveshippingoptions)
- [Amazon SP-API generateInvoice reference](https://developer-docs.amazon.com/sp-api/reference/generateinvoice)
- [Amazon SP-API retrieveInvoice reference](https://developer-docs.amazon.com/sp-api/reference/retrieveinvoice)
- [Amazon SP-API generateShipLabels reference](https://developer-docs.amazon.com/sp-api/reference/generateshiplabels)
- [Amazon SP-API listReturns reference](https://developer-docs.amazon.com/sp-api/reference/listreturns)
- [Amazon SP-API getReturn reference](https://developer-docs.amazon.com/sp-api/reference/getreturn)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON request/response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save complete responses under a linkfox session data directory and print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
