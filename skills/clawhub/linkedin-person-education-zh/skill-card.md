## Description: <br>
调取 LinkedIn 平台的用户教育履历清单，获取目标人员学历层次、毕业院校信息，梳理校友人脉网络，为客户画像搭建和商务关系挖掘提供支撑。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, HR teams, hiring managers, and talent evaluators use this skill to retrieve education records for a known LinkedIn person ID, including schools, degrees, majors, minors, GPA, summaries, and pagination. Sales and customer-intelligence teams may also use it to understand education background and alumni connections after confirming paid API use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid Upkuajing API, and each education-list page can incur a charge. <br>
Mitigation: Tell the user a query may cost money, check current pricing with the provided price command or pricing page, and wait for explicit confirmation before running paid calls. <br>
Risk: The API key may be stored in plaintext under the user's home directory. <br>
Mitigation: Keep the key private, restrict local file access where possible, and avoid sharing command output or files that reveal the key. <br>
Risk: LinkedIn person IDs are sent to the third-party Upkuajing API provider. <br>
Mitigation: Submit only identifiers the user is authorized to process and consider privacy, employment, and data-handling obligations before lookup. <br>
Risk: Local API logging could retain request and response data if intentionally enabled. <br>
Mitigation: Leave API logging disabled unless debugging is necessary, and remove local logs when they are no longer needed. <br>


## Reference(s): <br>
- [LinkedIn Person Education List API Reference](references/linkedin-person-education-list-api.md) <br>
- [ClawHub skill listing](https://clawhub.ai/upkuajing/skills/linkedin-person-education-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON data, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; API responses include fee information when returned by the provider.] <br>

## Skill Version(s): <br>
1.0.2 (source: SKILL.md metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
