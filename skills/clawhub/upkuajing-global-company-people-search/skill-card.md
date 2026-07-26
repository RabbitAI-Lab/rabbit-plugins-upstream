## Description: <br>
Search global companies and professional contacts for cross-border B2B lead generation, including company intelligence, business registration records, and verified contact details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External B2B sales, export, sourcing, and trade teams use this skill to search international companies and professional contacts, identify potential buyers or suppliers, and enrich selected entities with business details and contact information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill retrieves paid business and personal contact data, which can create privacy, compliance, and misuse risk. <br>
Mitigation: Use it only for a lawful business purpose, scope searches narrowly, and avoid broad contact harvesting. <br>
Risk: The UpKuaJing API key may be stored locally in ~/.upkuajing/.env. <br>
Mitigation: Use a dedicated API key, restrict local file permissions, and rotate or revoke the key if it may have been exposed. <br>
Risk: Search and enrichment results may be stored locally under task_data. <br>
Mitigation: Delete result files when they are no longer needed and avoid storing regulated or unnecessary personal data. <br>
Risk: List searches and enrichment interfaces can incur paid API charges. <br>
Mitigation: Confirm expected API call counts and fee impact before running large searches or batch enrichment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/upkuajing-global-company-people-search) <br>
- [UpKuaJing homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Company list API reference](references/company-list-api.md) <br>
- [People list API reference](references/human-list-api.md) <br>
- [Company detail API reference](references/company-detail-api.md) <br>
- [Human detail API reference](references/human-detail-api.md) <br>
- [Contact API reference](references/contact-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with Python command examples, JSON API responses, and local result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY; list searches and enrichment calls can incur fees and may write task_data results.] <br>

## Skill Version(s): <br>
1.0.9 (source: skill metadata and ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
