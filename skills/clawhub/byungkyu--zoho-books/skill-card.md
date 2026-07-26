## Description: <br>
Zoho Books API integration with managed OAuth for reading, creating, updating, and deleting invoices, contacts, bills, expenses, sales orders, purchase orders, and other accounting records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to access Zoho Books through Maton's managed OAuth proxy and manage contacts, invoices, bills, expenses, orders, and other accounting records. It is intended for workflows that need authenticated Zoho Books API calls with explicit approval before write or delete actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, or delete accounting records in Zoho Books. <br>
Mitigation: Require explicit user approval for each write or delete action after confirming the target account, resource ID, and business effect. <br>
Risk: MATON_API_KEY grants access through Maton's OAuth proxy. <br>
Mitigation: Keep the key secret, avoid logging it, and revoke unused or compromised credentials promptly. <br>
Risk: Requests may affect the wrong Zoho Books account when multiple connections exist. <br>
Mitigation: Use the Maton-Connection header to select the intended connection and verify it before acting. <br>


## Reference(s): <br>
- [Zoho Books API v3 Introduction](https://www.zoho.com/books/api/v3/introduction/) <br>
- [Zoho Books Invoices API](https://www.zoho.com/books/api/v3/invoices/) <br>
- [Zoho Books Contacts API](https://www.zoho.com/books/api/v3/contacts/) <br>
- [Zoho Books Bills API](https://www.zoho.com/books/api/v3/bills/) <br>
- [Zoho Books Expenses API](https://www.zoho.com/books/api/v3/expenses/) <br>
- [Maton](https://maton.ai) <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-books) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API endpoints, Python and JavaScript examples, shell commands, and JSON response examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and explicit user approval before create, update, or delete operations.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
