## Description: <br>
Helps agents work with Temu US fulfillment workflows, including Buy-Shipping labels, cooperative warehouse fulfillment, self-fulfilled shipments, tracking, scan forms, shipment documents, and related Partner US API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and developers use this skill to prepare and execute Temu US fulfillment tasks such as buying labels, confirming shipments, managing pickup reservations, downloading labels or scan forms, coordinating cooperative warehouse fulfillment, and checking tracking data. <br>

### Deployment Geography for Use: <br>
United States <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform live fulfillment actions that affect Temu shipping and order records. <br>
Mitigation: Use only with authorized Temu accounts, prefer test data first, and require explicit user confirmation before shipment creation, confirmation, cancellation, pickup changes, warehouse authorization, or label purchase/download. <br>
Risk: Access tokens and saved API responses may contain sensitive account, order, address, tracking, or label data. <br>
Mitigation: Treat tokens like passwords, avoid pasting them into logs or chat, restrict local file access, and delete saved response files when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-fulfillment-us) <br>
- [API reference](references/api.md) <br>
- [Partner US fulfillment catalog](references/partner-us-catalog.md) <br>
- [Access token guide](references/access-token.md) <br>
- [Authorization flow](references/authorization-flow.md) <br>
- [Fulfillment API index](references/apis/README.md) <br>
- [Temu Partner US documentation](https://partner-us.temu.com/documentation) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Files, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance, shell commands, and JSON responses or saved JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are saved as local JSON files; small responses may also be printed to stdout, while larger responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
