## Description: <br>
调取全球人员资料库查询目标人员的履历与学术背景，获取完整教育经历清单，完善 B2B 销售客户画像，依托学历背景挖掘潜在人脉关联。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, human resources teams, hiring managers, and B2B sales teams use this skill to retrieve a person's education history from the Upkuajing global company database by person ID. The skill helps review schools, degrees, majors, minors, GPA, and education summaries for candidate screening, background verification, talent assessment, or customer profile enrichment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid third-party API and may create charges for each education-history query or paginated follow-up request. <br>
Mitigation: Confirm cost expectations before running paid requests and use the provider's pricing endpoint or published pricing page for current fees. <br>
Risk: UPKUAJING_API_KEY can be stored locally in plaintext and used by helper commands for account, recharge, and lookup operations. <br>
Mitigation: Install only in trusted environments, restrict file permissions for local credential files, and avoid shared workspaces unless credential handling has been reviewed. <br>
Risk: The security scan notes an under-disclosed background version check to openapi.upkuajing.com. <br>
Mitigation: Review outbound network behavior before enterprise deployment and ensure users understand the automatic version-check request. <br>


## Reference(s): <br>
- [教育经历列表 API 参考](references/person-education-list-api.md) <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/global-company-person-education-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; API calls are paid and may return paginated education records and fee information.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
