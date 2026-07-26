## Description: <br>
Find alumni connections in LinkedIn data from a person ID and school ID for talent sourcing and B2B contact enrichment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External recruiters, sales teams, and B2B lead-generation specialists use this skill to identify alumni ties between a person and school in LinkedIn-derived data. It supports talent sourcing, institutional-network research, and contact-database expansion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid UpKuaJing API and each alumni-list page can incur a fee. <br>
Mitigation: Confirm pricing and get explicit user approval before running fee-incurring API calls; use the pricing command or pricing page for current costs. <br>
Risk: The API key may be stored in a plaintext ~/.upkuajing/.env file. <br>
Mitigation: Protect local credential files, avoid sharing the key, and remove or rotate the key if the environment is no longer trusted. <br>
Risk: Alumni lookup results may contain personal or contact-related data. <br>
Mitigation: Use the data only with a lawful and policy-compliant basis for recruiting, sales, or research workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/linkedin-person-alumni) <br>
- [UpKuaJing homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [LinkedIn person alumni list API reference](references/linkedin-person-alumni-list-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON responses with alumni records, pagination cursor, and fee information, plus concise guidance when credentials, balance, or parameters need attention.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python, httpx, and UPKUAJING_API_KEY; calls may incur per-page UpKuaJing API fees.] <br>

## Skill Version(s): <br>
1.0.4 (source: evidence.release.version and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
