## Description: <br>
Checks LinkedIn work history by personnel ID and returns employers, job titles, employment dates, and current or former status for background verification and candidate screening. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, hiring managers, sales teams, and talent-acquisition staff use this skill to review a professional's work-history timeline, past employers, and roles when screening candidates or validating background information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes employment-screening and professional background data. <br>
Mitigation: Use it only with a lawful basis and required consent, and review results before making hiring or screening decisions. <br>
Risk: The skill can create API keys, manage account top-up flows, and make paid API calls. <br>
Mitigation: Require explicit user confirmation before fee-incurring calls or account-management actions, and verify current pricing before use. <br>
Risk: The skill stores the UpKuaJing API key in a plaintext file under ~/.upkuajing/.env. <br>
Mitigation: Restrict local file access, avoid sharing the environment file, and rotate the key if it may have been exposed. <br>
Risk: The skill performs a remote version check and may create local cache or log files. <br>
Mitigation: Review version-check, logging, and persistence behavior before using the skill in sensitive environments. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/linkedin-person-experience) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [Detailed Price Description](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Work Experience List API](references/linkedin-person-experience-list-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY; API calls may incur fees and support cursor pagination.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
