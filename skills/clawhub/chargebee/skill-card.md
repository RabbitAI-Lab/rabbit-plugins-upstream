## Description: <br>
Chargebee API integration with managed OAuth for administering customers, subscriptions, invoices, hosted pages, and billing workflows through Maton. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to access Chargebee billing data and perform Chargebee administration through a managed Maton OAuth connection. It supports customer, subscription, invoice, hosted page, portal session, catalog, and billing workflow tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform billing administration actions that may affect customers, subscriptions, invoices, or revenue. <br>
Mitigation: Default to read-only checks, retrieve the target resource first, summarize the exact effect and financial impact, and require explicit user approval before any write, update, cancel, or delete action. <br>
Risk: Requests may target the wrong Chargebee account when multiple Maton connections exist or a default connection is used. <br>
Mitigation: Always specify and verify the intended Maton-Connection value before making requests, especially before write operations. <br>
Risk: MATON_API_KEY values and connection URLs can grant access to billing systems if exposed. <br>
Mitigation: Keep API keys and connection URLs private, use least-privilege Chargebee access, and revoke unused connections promptly. <br>


## Reference(s): <br>
- [ClawHub Chargebee Skill](https://clawhub.ai/byungkyu/skills/chargebee) <br>
- [Chargebee API Overview](https://apidocs.chargebee.com/docs/api) <br>
- [Chargebee Customers API](https://apidocs.chargebee.com/docs/api/customers) <br>
- [Chargebee Subscriptions API](https://apidocs.chargebee.com/docs/api/subscriptions) <br>
- [Chargebee Invoices API](https://apidocs.chargebee.com/docs/api/invoices) <br>
- [Chargebee Hosted Pages API](https://apidocs.chargebee.com/docs/api/hosted_pages) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline Python, JavaScript, shell, HTTP endpoint, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MATON_API_KEY and, when multiple Chargebee connections exist, an explicit Maton-Connection header.] <br>

## Skill Version(s): <br>
1.0.7 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
