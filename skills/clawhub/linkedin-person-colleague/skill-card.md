## Description: <br>
Find colleagues for a LinkedIn person using a company ID and personnel ID, then return colleague identifiers and job titles for recruiting, sales outreach, and account intelligence workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, sales teams, B2B lead-generation specialists, and account-intelligence researchers use this skill to discover colleagues and team relationships from UpKuaJing LinkedIn data when they already have the required company and person identifiers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: UpKuaJing API calls can incur fees. <br>
Mitigation: Tell the user a query or top-up can cost money, check current pricing through the provided pricing command or link, and wait for explicit confirmation before executing paid actions. <br>
Risk: Company and person identifiers are sent to UpKuaJing for LinkedIn colleague lookup. <br>
Mitigation: Submit only identifiers needed for the user's approved recruiting, sales, or account-intelligence task, and avoid unnecessary personal data. <br>
Risk: The API key may be stored in plaintext at ~/.upkuajing/.env. <br>
Mitigation: Protect the local environment file, avoid sharing the key, and prefer secure environment management where available. <br>


## Reference(s): <br>
- [Colleague List API Reference](references/linkedin-person-colleague-list-api.md) <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/linkedin-person-colleague) <br>
- [UpKuaJing homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; colleague queries can return paginated results and fee information.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
