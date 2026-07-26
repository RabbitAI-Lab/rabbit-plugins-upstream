## Description: <br>
Provides agent-facing guidance and scripts for authorized Shopee stores to manage logistics workflows through LinkFox, including shipping orders, tracking numbers, shipping documents, addresses, channels, booking, and operating-hour actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, store operators, and developers use this skill to run authorized Shopee logistics actions such as preparing shipments, obtaining tracking numbers, generating shipping documents, and managing logistics settings for a shop. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change live Shopee shop logistics data, including shipping orders, addresses, channels, pause status, and tracking state. <br>
Mitigation: Confirm each state-changing action and its target shop, order, address, or channel before execution. <br>
Risk: Saved LinkFox response files may contain sensitive business, customer, order, or logistics data. <br>
Mitigation: Store response files only in protected workspaces and delete or retain them according to the user's data handling requirements. <br>
Risk: The skill requires access to authorized Shopee store credentials through the LinkFox authentication dependency. <br>
Mitigation: Use only authorized shop access, keep API keys out of shared logs, and resolve missing authentication through the documented dependency flow. <br>


## Reference(s): <br>
- [Skill API reference](references/api.md) <br>
- [Shopee Open Platform Logistics documentation](https://open.shopee.com/documents/v2/v2.logistics.get_shipping_parameter?module=95&type=1) <br>
- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-logistics) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON, files] <br>
**Output Format:** [Markdown guidance with shell commands and JSON inputs; script runs return JSON responses and save full response files locally.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses up to 8 KB are printed in full after being saved; larger responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
