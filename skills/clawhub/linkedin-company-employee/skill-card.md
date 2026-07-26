## Description: <br>
Pull LinkedIn employee lists and job titles by company ID for talent mapping, organizational analysis, and B2B lead qualification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, sales teams, and B2B lead-generation specialists use this skill to retrieve employee records and job titles for a known LinkedIn company ID, supporting talent mapping, organization review, and lead qualification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid UpKuaJing API client and can perform account or top-up actions. <br>
Mitigation: Inform the user before any paid query or account action, use the pricing reference for current costs, and wait for explicit confirmation in a separate message before proceeding. <br>
Risk: The skill reads and may write an API key in plaintext under ~/.upkuajing/.env. <br>
Mitigation: Use a dedicated API key, avoid printing the key value, restrict access to the local environment file, and prefer environment-managed secrets in shared environments. <br>
Risk: Queries contact UpKuaJing over the network and send company identifiers to the service. <br>
Mitigation: Review organizational data-sharing requirements before use and submit only company identifiers that are appropriate for the user's compliance context. <br>


## Reference(s): <br>
- [LinkedIn Employee List API Reference](references/linkedin-company-employee-list-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing API Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; paid queries require explicit confirmation and may return paginated results.] <br>

## Skill Version(s): <br>
1.0.2 (source: server evidence and frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
