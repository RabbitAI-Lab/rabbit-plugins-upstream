## Description:

依托 LinkedIn 数据，结合人员与企业信息调取校友及离职前员工清单，挖掘彼此共同求学背景和过往任职关联，发掘潜在商务合作机会。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, sales teams, B2B lead builders, and relationship researchers use this skill to look up LinkedIn alumni relationships for a specified person and school. It helps expand contact lists, trace education-based associations, and support talent sourcing or lead generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid lookup or recharge-related actions can incur external Upkuajing API costs.

Mitigation: Confirm any charged lookup, pagination request, price check, or recharge-related action with the user before execution.

Risk: The Upkuajing API key may be stored in a local plaintext .env file.

Mitigation: Keep the key out of chat and logs, restrict local file access where possible, and rotate the key if exposure is suspected.

Risk: Lookup and optional error-report data is sent to the external Upkuajing service.

Mitigation: Send only the minimum necessary lookup or diagnostic context and avoid including secrets or unrelated personal data in error reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/linkedin-person-alumni-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer platform](https://developer.upkuajing.com/)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [领英校友列表 API 参考](references/linkedin-person-alumni-list-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Alumni lookup responses include paginated list data, fee information, and request identifiers when returned by the Upkuajing API.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
