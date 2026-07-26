## Description: <br>
Verifies overseas candidates' education history, including schools attended, degrees, majors, minors, GPA, and summaries, through the UpKuaJing API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, HR teams, and hiring managers use this skill to validate applicant education histories during pre-employment screening, credential checks, and talent assessment workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Candidate or person identifiers are sent to UpKuaJing's paid API. <br>
Mitigation: Use the skill only when the organization is authorized to submit those identifiers to UpKuaJing and the user has confirmed the paid query. <br>
Risk: The API key is stored locally in ~/.upkuajing/.env. <br>
Mitigation: Avoid displaying the file contents in chat or logs and use organizational secret-management controls for production deployments. <br>
Risk: Each query and pagination request may incur fees or require account top-up. <br>
Mitigation: Confirm paid API calls and top-up actions explicitly before execution, and check current pricing through the documented UpKuaJing pricing flow. <br>
Risk: Runtime dependency versions are not pinned beyond a lower bound. <br>
Mitigation: Pin dependencies in managed production environments if reproducible installs or stricter supply-chain controls are required. <br>


## Reference(s): <br>
- [Education History List API Reference](references/person-education-list-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Developer Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [ClawHub Skill Listing](https://clawhub.ai/upkuajing/skills/global-company-person-education) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include paginated education records and fee information returned by the UpKuaJing API.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
