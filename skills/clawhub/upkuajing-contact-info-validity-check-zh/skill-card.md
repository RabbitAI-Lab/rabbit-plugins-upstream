## Description: <br>
核验邮箱、手机号及其余联系方式的真实有效性，在开展客户触达前筛选无效数据，提升联系信息准确度，降低消息无效发送概率，服务外贸获客、CRM 数据清洗和销售线索核验工作。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales teams, recruiters, traders, and CRM operators use this skill to validate phone numbers, email addresses, and domains before outreach, list cleaning, supplier checks, candidate screening, and contact-data enrichment. It helps identify invalid records, phone type, WhatsApp registration state, domain validity, and domain safety signals through Upkuajing API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an Upkuajing API key and sends phone numbers, email addresses, and domains to the provider's API. <br>
Mitigation: Use a platform secret store or restricted local file permissions for the API key, avoid sharing the key in chat, and only submit contact data that is approved for third-party validation. <br>
Risk: The package includes local credential storage plus account and recharge helpers. <br>
Mitigation: Review account actions before use, inspect any payment URL before opening it, and require explicit user confirmation before paid or billing-related operations. <br>
Risk: The security scan notes an under-disclosed version check in addition to the main contact-validation behavior. <br>
Mitigation: Review the version-check behavior before deployment and allow outbound network access only to provider endpoints that are acceptable for the environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/upkuajing-contact-info-validity-check-zh) <br>
- [Publisher profile](https://clawhub.ai/user/upkuajing) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Phone validity API](references/phone-api.md) <br>
- [Email validity API](references/email-api.md) <br>
- [Domain validity API](references/domain-api.md) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [JSON results and concise Markdown guidance for running validation scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python, httpx, and an UPKUAJING_API_KEY; validation API calls may incur provider fees.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
