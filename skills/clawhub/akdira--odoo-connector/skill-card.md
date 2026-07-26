## Description: <br>
AI Agent skill for Odoo 17/18/19 XML-RPC API integration, including authentication, CRUD operations, and search operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[akdira](https://clawhub.ai/user/akdira) <br>

### License/Terms of Use: <br>
MIT No Attribution (MIT-0) <br>


## Use Case: <br>
Developers, engineers, and operations teams use this skill to help agents connect to authorized Odoo 17, 18, or 19 systems through XML-RPC, generate API usage patterns, and perform ERP data operations such as authentication, search, read, create, update, and delete. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill recommends bypassing CAPTCHA or Cloudflare protections during Odoo web UI login. <br>
Mitigation: Use API keys, service accounts, allowlisted network paths, or administrator-approved security configuration instead of following bypass advice. <br>
Risk: Generated examples can perform live write, delete, order confirmation, replenishment, and external synchronization operations in Odoo. <br>
Mitigation: Test in staging first, use least-privilege credentials, keep backups, and require human review before production execution. <br>
Risk: Odoo API credentials can expose ERP data and business workflows if mishandled. <br>
Mitigation: Store credentials in environment variables or a secrets manager, prefer API keys over passwords, rotate keys, and avoid logging or committing secrets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/akdira/skills/odoo-connector) <br>
- [Publisher profile](https://clawhub.ai/user/akdira) <br>
- [Authentication Guide](docs/authentication.md) <br>
- [Quick Start Guide](docs/quickstart.md) <br>
- [API Reference](docs/api-reference.md) <br>
- [Troubleshooting Guide](docs/troubleshooting.md) <br>
- [Odoo External API documentation](https://www.odoo.com/documentation/17.0/developer/reference/external_api.html) <br>
- [Odoo ORM API documentation](https://www.odoo.com/documentation/17.0/developer/reference/backend/orm.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python XML-RPC code examples, shell commands, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may propose live Odoo read, write, delete, order, replenishment, and synchronization operations that require authorized credentials and review before execution.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter, changelog, and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
