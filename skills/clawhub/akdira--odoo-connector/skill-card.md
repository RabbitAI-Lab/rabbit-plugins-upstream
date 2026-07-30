## Description: <br>
AI Agent skill for Odoo 17/18/19 XML-RPC API integration for authentication, CRUD, and search operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[akdira](https://clawhub.ai/user/akdira) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and business automation teams use this skill to guide agents that connect to authorized Odoo ERP instances, verify XML-RPC credentials, and perform read, search, create, update, delete, bulk import, and workflow operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write-capable Odoo credentials can modify live ERP records and trigger business workflows. <br>
Mitigation: Use a dedicated least-privilege API user, test in staging first, and require explicit confirmation before create, write, unlink, action_confirm, replenishment, bulk import, or third-party sync operations. <br>
Risk: Credentials or API keys can expose an Odoo instance if stored or logged unsafely. <br>
Mitigation: Store Odoo credentials in environment variables or a secrets manager, rotate keys, avoid admin accounts, and do not commit or log secrets. <br>
Risk: Unauthorized automation or CAPTCHA-related access can violate system owner permissions or service terms. <br>
Mitigation: Use the skill only with explicit authorization for the target Odoo instance and verify hosting provider terms before automated access. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/akdira/skills/odoo-connector) <br>
- [Odoo External API Documentation](https://www.odoo.com/documentation/17.0/developer/reference/external_api.html) <br>
- [Odoo ORM API Reference](https://www.odoo.com/documentation/17.0/developer/reference/backend/orm.html) <br>
- [Python xmlrpc.client Documentation](https://docs.python.org/3/library/xmlrpc.client.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python code examples, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No external Python dependencies are required by the bundled scripts; generated guidance depends on the target Odoo instance, credentials, permissions, and selected model operations.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release evidence, _meta.json, and CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
