## Description:

依托全球企业数据库检索目标公司对应的校友以及离职前员工名单，梳理企业历史人员脉络，挖掘潜在商务联系人并拓展业务合作机会。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, sales teams, B2B lead builders, and relationship researchers use this skill to query alumni-style people lists from Upkuajing's global company data by person ID and school ID. It supports talent sourcing, background research, contact-list expansion, and professional network analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts Upkuajing services and may trigger billable API calls.

Mitigation: Confirm the user's intent and billing awareness before running paid lookup or pagination commands, and use the pricing endpoint or published pricing page for current cost information.

Risk: The API key may be stored in a local plaintext file under the user's home directory.

Mitigation: Prefer environment-variable injection where possible, avoid displaying or pasting the key, and restrict local file permissions for any saved credential file.

Risk: Optional error reporting can send request context and failure details to the provider.

Mitigation: Review the error report content with the user and send it only after explicit confirmation.

Risk: The scan summary notes under-disclosed support and version-check network calls.

Mitigation: Review network behavior before deployment and account for provider version-check and support endpoints in security approvals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/global-company-person-alumni-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer platform](https://developer.upkuajing.com/)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Person alumni list API reference](artifact/references/person-alumni-list-api.md)
- [Skill error report API reference](artifact/references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Alumni-list responses include data, fee information, and request identifiers; paginated results use a cursor for follow-up calls.]

## Skill Version(s):

1.0.5 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
