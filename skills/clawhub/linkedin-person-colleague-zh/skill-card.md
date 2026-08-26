## Description:

依托 LinkedIn 数据，结合人员与企业信息检索同事和团队成员清单，梳理企业内部人际关联与组织架构，发掘可对接的潜在商务联系人。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, sales teams, B2B lead builders, and business researchers use this skill to retrieve LinkedIn colleague lists by company ID and person ID, map team relationships, and expand contact research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read or create an API key and store it under ~/.upkuajing.

Mitigation: Review this behavior before installing, protect the key as a secret, and verify key presence without printing .env contents in chat or logs.

Risk: The skill can access account balance details and create recharge payment URLs.

Mitigation: Require explicit user confirmation before paid queries or recharge actions, and direct users to verify pricing and payment pages before proceeding.

Risk: The skill can send confirmed error reports to the provider.

Mitigation: Send diagnostics only after user confirmation and avoid including sensitive or unnecessary context in error reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/linkedin-person-colleague-zh)
- [Publisher profile](https://clawhub.ai/user/upkuajing)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer portal](https://developer.upkuajing.com/)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [LinkedIn colleague list API reference](artifact/references/linkedin-person-colleague-list-api.md)
- [Skill error report API reference](artifact/references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses and concise Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY; colleague lookup calls may incur fees and support cursor pagination.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
