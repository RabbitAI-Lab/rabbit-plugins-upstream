## Description:

依托全球企业资料库查找目标人员或企业对应的同事及内部团队成员，梳理企业内部人脉网络，助力外贸销售和猎头人员拓展业务人脉，实现精准客户触达。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, sales teams, B2B lead builders, and business researchers use this skill to find colleagues and internal team members for a known company and person ID. It helps expand relationship maps after a key contact has been identified.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid Upkuajing API and paginated lookups can incur a charge per page.

Mitigation: Tell the user a query may incur fees and wait for explicit confirmation before running paid lookups; use the price information command or pricing page for current costs.

Risk: The API key may be stored in plaintext under ~/.upkuajing.

Mitigation: Protect local access to the API key file, avoid sharing it, and rotate the key if exposure is suspected.

Risk: The skill performs automatic network version-check requests and can send error reports that may include request or response context.

Mitigation: Review network behavior before installation and avoid including sensitive request or response details when reporting errors.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/global-company-person-colleague-zh)
- [Upkuajing Homepage](https://www.upkuajing.com)
- [Upkuajing Developer Platform](https://developer.upkuajing.com/)
- [Upkuajing API Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Person Colleague List API](references/person-colleague-list-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and an UPKUAJING_API_KEY; colleague lookup calls are paid and paginated.]

## Skill Version(s):

1.0.5 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
