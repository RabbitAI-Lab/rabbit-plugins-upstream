## Description: <br>
Zoho Bigin API integration with managed OAuth for managing contacts, companies, pipelines, and products in Bigin CRM. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to read, search, create, update, and delete Zoho Bigin CRM records through Maton-managed OAuth when working with contacts, companies, products, and sales pipelines. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access connected Zoho Bigin CRM data through Maton-managed OAuth. <br>
Mitigation: Review the Zoho and Maton OAuth scopes before use and install only for accounts whose CRM data the agent is allowed to access. <br>
Risk: Create, update, and delete operations can mutate business CRM records. <br>
Mitigation: Require explicit user approval before executing write operations, including confirmation of the target resource and intended effect. <br>
Risk: Using the wrong connection when multiple Zoho Bigin accounts are configured could affect unintended CRM data. <br>
Mitigation: Use the Maton-Connection header to select the intended active connection when more than one account is available. <br>


## Reference(s): <br>
- [Zoho Bigin Skill on ClawHub](https://clawhub.ai/byungkyu/skills/zoho-bigin) <br>
- [Publisher Profile](https://clawhub.ai/user/byungkyu) <br>
- [Bigin API Overview](https://www.bigin.com/developer/docs/apis/v2/) <br>
- [Bigin REST API Documentation](https://www.bigin.com/developer/docs/apis/) <br>
- [Modules API](https://www.bigin.com/developer/docs/apis/modules-api.html) <br>
- [Maton](https://maton.ai) <br>
- [Maton Community](https://discord.com/invite/dBfFAcefs2) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with API endpoint descriptions and Python, JavaScript, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and the MATON_API_KEY environment variable for authenticated requests.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
