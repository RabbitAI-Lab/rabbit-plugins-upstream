## Description: <br>
Helps agents search Amazon seller orders, retrieve order, buyer, address, item, and regulated-order details, and run shipment or verification status actions for Amazon SP-API Orders workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and developers use this skill to inspect Amazon store orders, retrieve buyer or order item details, and perform shipment or regulated-order status updates through guided agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read sensitive Amazon order, buyer, address, item, and regulated-order data. <br>
Mitigation: Use it only from a private workspace, request buyer or address details only when needed, and keep access limited to trusted users. <br>
Risk: The skill can change shipment or regulated-order verification state. <br>
Mitigation: Require explicit human confirmation before running shipment confirmation, shipment status, or verification update scripts. <br>
Risk: The skill saves complete API responses locally, which can retain sensitive order data. <br>
Mitigation: Review saved linkfox data files for retention and remove sensitive outputs when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-orders) <br>
- [Local API and Gateway Reference](references/api.md) <br>
- [Amazon SP-API searchOrders](https://developer-docs.amazon.com/sp-api/reference/searchorders) <br>
- [Amazon SP-API getOrder](https://developer-docs.amazon.com/sp-api/reference/getorder-3) <br>
- [Amazon SP-API Restricted Data Token](https://developer-docs.amazon.com/sp-api/reference/createrestricteddatatoken) <br>
- [Amazon SP-API confirmShipment](https://developer-docs.amazon.com/sp-api/reference/confirmshipment) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON script outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts save complete JSON responses locally and may print either full JSON or a summarized response depending on response size.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
