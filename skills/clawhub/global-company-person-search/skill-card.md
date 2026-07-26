## Description: <br>
Search global corporate personnel by name, company, industry, and profile URL, and enrich contact data for recruiting, sales, and B2B lead generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, sales teams, and B2B lead-generation specialists use this skill to find global corporate personnel and enrich contact data for talent search, headhunting, lead development, and cross-border customer acquisition. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queries and returned contact data are sent to and received from the UpKuaJing API, and results may include personal or business contact information. <br>
Mitigation: Review privacy, consent, retention, and lawful-use requirements before running searches or storing returned records. <br>
Risk: The skill uses paid API calls and may incur fees, especially for query_count values above one page of results. <br>
Mitigation: Check current pricing with the provided pricing helper or pricing page, inform the user of expected call volume, and get explicit confirmation before paid operations. <br>
Risk: The API key is stored in ~/.upkuajing/.env when generated or configured locally. <br>
Mitigation: Protect the local env file, avoid sharing the key, and rotate or replace the key if it is exposed. <br>
Risk: Search results are stored locally as task JSONL files and can contain contact-enrichment data. <br>
Mitigation: Apply local access controls and delete task result files when they are no longer needed. <br>


## Reference(s): <br>
- [Global Company Person List API](references/global-company-person-list-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/global-company-person-search) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/upkuajing) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [JSON responses, local JSONL result files, and concise Markdown guidance with shell commands when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results are stored as per-task JSONL files; task metadata supports continuation by task_id.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
