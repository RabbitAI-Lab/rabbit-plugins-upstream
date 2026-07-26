## Description: <br>
依托全球企业数据库检索目标公司对应的校友以及离职前员工名单，梳理企业历史人员脉络，挖掘潜在商务联系人并拓展业务合作机会。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, sales teams, B2B lead builders, and relationship analysts use this skill to look up alumni or former colleague links for a person and organization context through the Upkuajing global company database. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API calls can incur vendor charges, including additional charges for paginated follow-up requests. <br>
Mitigation: Confirm the user understands the charge before each paid lookup and use the vendor pricing command or pricing page instead of estimating costs. <br>
Risk: The skill may store UPKUAJING_API_KEY in a plaintext file under the user's home directory. <br>
Mitigation: Use local file permissions or a separate secret-management process for the API key, and avoid sharing the file contents. <br>
Risk: Recharge workflows can create payment URLs for the vendor service. <br>
Mitigation: Review any payment URL before opening it or sending funds, and confirm the transaction with the account owner. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/global-company-person-alumni-zh) <br>
- [Publisher profile](https://clawhub.ai/user/upkuajing) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer portal](https://developer.upkuajing.com/) <br>
- [Upkuajing API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [全球企业库校友列表 API 参考](references/person-alumni-list-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns paginated alumni records and fee information when provided by the vendor API.] <br>

## Skill Version(s): <br>
1.0.3 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
