## Description: <br>
Keap API integration with managed OAuth for managing contacts, companies, tags, tasks, orders, opportunities, campaigns, email, and related CRM and marketing automation resources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to access Keap through Maton-managed OAuth, inspect CRM data, and prepare approved changes to contacts, companies, tags, tasks, orders, opportunities, campaigns, and marketing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can mediate broad access to Keap CRM and marketing automation data through Maton. <br>
Mitigation: Install it only when Maton-mediated Keap access is intended, protect MATON_API_KEY, and keep the key out of logs and shared prompts. <br>
Risk: Requests may affect the wrong Keap account when multiple Maton connections exist. <br>
Mitigation: Specify the intended Maton connection before making account-specific requests. <br>
Risk: Write operations can send email or change contacts, tags, orders, products, opportunities, campaigns, and other CRM records. <br>
Mitigation: Review the target resource and intended effect with the user before approving any create, update, delete, email send, order/product change, or campaign sequence change. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/keap) <br>
- [Keap Developer Portal](https://developer.infusionsoft.com/) <br>
- [Keap REST API V2 Documentation](https://developer.infusionsoft.com/docs/restv2/) <br>
- [Keap Getting Started Guide](https://developer.infusionsoft.com/getting-started/) <br>
- [Keap OAuth 2.0 Authentication](https://developer.infusionsoft.com/authentication/) <br>
- [Maton](https://maton.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with REST endpoints and Python, JavaScript, and shell examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and a connected Keap OAuth account through Maton.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
