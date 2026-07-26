## Description: <br>
Manage Odoo contacts, business objects, and metadata through the official External XML-RPC API, including generic CRUD operations, res.partner flows, model introspection, and dynamic instance, database, and credential resolution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[willykinfoussia](https://clawhub.ai/user/willykinfoussia) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, administrators, and business operations teams use this skill to inspect and manage Odoo records through XML-RPC. It supports connection checks, contact management, generic model CRUD operations, model discovery, and controlled switching between Odoo instances or databases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can enable broad changes or deletions in live Odoo business data. <br>
Mitigation: Use a dedicated least-privilege API key, verify the active URL, database, and user before every write or delete, test in staging first, and avoid broad bulk operations. <br>
Risk: Session or temporary context can point operations at the wrong Odoo instance or database. <br>
Mitigation: Review the resolved connection context before sensitive operations and clear session context after sensitive work. <br>
Risk: Credentials and API keys grant the same access as the Odoo user account. <br>
Mitigation: Protect credentials as secrets, avoid exposing full secrets in outputs, and prefer scoped API keys over passwords. <br>


## Reference(s): <br>
- [Odoo Documentation](https://www.odoo.com/documentation/) <br>
- [Odoo External API documentation](https://www.odoo.com/documentation/18.0/fr/developer/reference/external_api.html) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline code blocks and structured command or API call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Odoo XML-RPC request examples, resolved connection context summaries without full secrets, and operational warnings for write or delete actions.] <br>

## Skill Version(s): <br>
0.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
