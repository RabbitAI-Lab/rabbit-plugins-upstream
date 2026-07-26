## Description: <br>
调取 LinkedIn 用户的完整任职履历清单，梳理目标人员职业发展轨迹、就职企业变动情况以及专业从业背景，为商务尽调、客户背景分析提供参考依据。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
招聘人员、用人经理、销售和尽调团队可用该技能按人员 ID 查询 LinkedIn 工作经历，核验候选人履历、评估专业经验并了解目标人员曾任职公司。使用前应确认会产生 API 调用费用，并在处理个人职业数据时遵守适用的数据使用和隐私要求。 <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads and writes ~/.upkuajing files and may store an API key in plaintext. <br>
Mitigation: Install only in trusted environments, protect the API key file with local access controls, and rotate the key if it may have been exposed. <br>
Risk: API calls can incur account charges, including paginated follow-up requests. <br>
Mitigation: Require explicit user confirmation before billable calls and check current pricing or account balance before high-volume use. <br>
Risk: The skill can create recharge orders and surface payment URLs when directed. <br>
Mitigation: Treat billing actions as user-approved account operations and verify payment links before opening them. <br>
Risk: The security summary notes an under-disclosed automatic version-check request. <br>
Mitigation: Review outbound network behavior before deployment and ensure users are comfortable with periodic version checks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/linkedin-person-experience-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [领英工作经历列表 API 参考](references/linkedin-person-experience-list-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Configuration guidance] <br>
**Output Format:** [Markdown guidance with command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; calls the Upkuajing OpenAPI and may return paginated work-experience records with fee information.] <br>

## Skill Version(s): <br>
1.0.1 (source: SKILL.md metadata and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
