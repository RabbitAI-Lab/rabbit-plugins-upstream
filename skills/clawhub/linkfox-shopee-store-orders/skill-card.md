## Description: <br>
Helps agents query and manage Shopee store orders through LinkFox wrappers for the Shopee Open Platform Order module, including order lists, details, shipment/package views, cancellations, notes, split/unsplit actions, booking, invoices, and related FBS workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and agent workflows use this skill to inspect Shopee order state, retrieve order and package details, and perform supported order-management actions after store authorization is available. <br>

### Deployment Geography for Use: <br>
Global, subject to Shopee account, marketplace, and endpoint-specific regional eligibility for invoice, FBS, and prescription-check APIs. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform high-impact Shopee order mutations such as cancellation, split/unsplit, buyer-cancellation handling, prescription-check handling, and note updates. <br>
Mitigation: Require explicit confirmation of shop ID, order or package identifier, target API, and operation before running any mutating script. <br>
Risk: Order responses may contain sensitive buyer, recipient, item, shipment, or invoice data and are saved to workspace files. <br>
Mitigation: Use a controlled workspace, review saved LinkFox response files, restrict access to generated data, and avoid inline full-response output for sensitive data. <br>
Risk: Some APIs are region or eligibility restricted, including invoice, FBS, and prescription-check functions. <br>
Mitigation: Check the referenced API documentation and store eligibility before invoking region-limited endpoints. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-orders) <br>
- [Local API parameter reference](references/api.md) <br>
- [Shopee Open Platform Order module](https://open.shopee.com/documents/v2/v2.order.get_order_list?module=94&type=1) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API calls, JSON, Files, Guidance] <br>
**Output Format:** [JSON responses saved to workspace files, with stdout containing either full JSON or a concise summary depending on response size] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LinkFox API credentials and an authorized Shopee store; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
