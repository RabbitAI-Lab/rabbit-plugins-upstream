## Description:

核验邮箱、手机号及其余联系方式的真实有效性，在开展客户触达前筛选无效数据，提升联系信息准确度，降低消息无效发送概率，服务外贸获客、CRM 数据清洗和销售线索核验工作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams, recruiters, traders, and CRM operators use this skill to validate phone numbers, email addresses, and domains before outreach, list cleaning, candidate screening, or supplier verification. It helps reduce invalid sends and improves contact-data quality by returning validation status, phone type, WhatsApp status, domain safety status, and fee information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact records submitted for validation are sent to Upkuajing's API.

Mitigation: Use the skill only for contact data you are permitted to share with Upkuajing and avoid sending unnecessary personal or customer information.

Risk: Validation API calls are paid operations.

Mitigation: Confirm pricing and account balance before running billable checks, and review payment URLs before opening them.

Risk: The API key is stored locally in ~/.upkuajing/.env.

Mitigation: Protect the local key file, limit access permissions, and avoid exposing the key in logs, screenshots, or shared transcripts.

Risk: Error reports can include request context or payload details.

Mitigation: Do not include secrets or full customer payloads in error reports; send only the information needed for troubleshooting.

## Reference(s):

- [Phone Validity API Reference](references/phone-api.md)
- [Email Validity API Reference](references/email-api.md)
- [Domain Validity API Reference](references/domain-api.md)
- [Skill Error Report API Reference](references/skill-error-report-api.md)
- [Upkuajing Homepage](https://www.upkuajing.com)
- [Upkuajing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/upkuajing-contact-info-validity-check-zh)
- [Publisher Profile](https://clawhub.ai/user/upkuajing)

## Skill Output:

**Output Type(s):** [JSON, Guidance, Shell commands]

**Output Format:** [JSON validation results with concise Markdown guidance and direct script commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include total counts, per-contact validation records, fee information, and request identifiers.]

## Skill Version(s):

1.0.4 (source: server release and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
