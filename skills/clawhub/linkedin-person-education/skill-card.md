## Description: <br>
Retrieves LinkedIn-sourced education history by person ID, including schools, degrees, majors, minors, GPAs, and pagination data for candidate background review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, HR teams, hiring managers, and authorized screening workflows use this skill to retrieve education records for a LinkedIn person ID when assessing candidate qualifications or verifying academic background. Review is recommended before installation because the security evidence flags candidate-data handling, paid API calls, plaintext API key storage, account top-up helpers, and version-check persistence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Candidate and employee education data may be sensitive and may require authorization before querying. <br>
Mitigation: Use only for authorized screening or verification workflows and avoid exposing returned records beyond the intended hiring review process. <br>
Risk: API calls may incur fees and the skill includes account top-up helpers. <br>
Mitigation: Inform users about paid calls and obtain explicit confirmation before execution; verify pricing through the provider before running paginated lookups. <br>
Risk: The skill stores API keys in plaintext under ~/.upkuajing and may write version-check cache data. <br>
Mitigation: Protect local credential files, avoid printing .env contents in chat or logs, and disable or remove version-check or persistence behavior where telemetry retention is restricted. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/upkuajing/skills/linkedin-person-education) <br>
- [UpKuaJing homepage](https://www.upkuajing.com) <br>
- [UpKuaJing developer platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [LinkedIn person education list API reference](references/linkedin-person-education-list-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Text, Shell commands, Configuration guidance] <br>
**Output Format:** [JSON API responses and concise Markdown guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; calls may incur fees and may return fee metadata with account balance and call cost.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
