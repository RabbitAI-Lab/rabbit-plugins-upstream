## Description: <br>
This skill queries UpKuaJing's global company database for a person's work experience records by personnel ID, with optional filtering by company ID. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, HR staff, hiring managers, and analysts can use this skill to retrieve a person's work history from the UpKuaJing global company database. Server security evidence notes that the release advertises education verification, but the artifact behavior is work-experience lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release metadata advertises education verification, while the artifact queries work-experience records. <br>
Mitigation: Install and use the skill only when the intended task is work-experience lookup, and disclose the mismatch during review before relying on results. <br>
Risk: Queries and account top-up actions can incur costs. <br>
Mitigation: Require explicit user confirmation in a separate message before any billable query or top-up order. <br>
Risk: The skill can store the API key in plaintext under ~/.upkuajing/.env. <br>
Mitigation: Prefer a managed secret store or environment variable and avoid writing credentials to local plaintext files when possible. <br>
Risk: The skill performs a daily version-check call to the provider during API use. <br>
Mitigation: Review outbound network behavior and provider endpoints before deployment in restricted environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/global-company-person-experience) <br>
- [UpKuaJing homepage](https://www.upkuajing.com) <br>
- [UpKuaJing developer platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Work Experience List API reference](references/person-experience-list-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and an UPKUAJING_API_KEY; API calls are billable and may return paginated results.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release, artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
