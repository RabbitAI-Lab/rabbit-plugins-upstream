## Description: <br>
B2B lead generation skill that combines customs trade intelligence, global company due diligence, and LinkedIn professional-network data to help agents analyze markets, investigate companies, identify decision makers, and support cross-border buyer or supplier discovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sales, sourcing, export, and B2B lead-generation teams use this skill to inspect customs trade patterns, assess companies and suppliers, identify buyers and decision makers, and map professional relationships before outreach. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid API credentials may be stored in a local ~/.upkuajing/.env file. <br>
Mitigation: Use a managed secret mechanism where possible, restrict permissions on the local credential file, and rotate the API key if it may have been exposed. <br>
Risk: The skill can retrieve and store bulk personal, contact, and professional-network data. <br>
Mitigation: Use the skill only for lawful B2B due diligence or lead generation with a valid basis, minimize collection, and treat all returned task_data as sensitive. <br>
Risk: Result files may persist locally under task_data after searches or long-running jobs. <br>
Mitigation: Periodically delete stored result files that are no longer needed and avoid sharing task_data outside approved workflows. <br>
Risk: All API calls are paid, and broad searches may consume multiple billable calls. <br>
Mitigation: Require explicit user confirmation before chargeable operations and use the platform pricing command or pricing page for current costs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/b2b-lead-generation-zh) <br>
- [UpKuaJing homepage](https://www.upkuajing.com) <br>
- [UpKuaJing developer platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Company employee list API](references/company-employee-list-api.md) <br>
- [Company shareholder list API](references/company-shareholder-list-api.md) <br>
- [Customs HS code market distribution API](references/customs-analysis-area-api.md) <br>
- [Customs HS code detail API](references/customs-analysis-hscode-detail-api.md) <br>
- [Customs HS code search API](references/customs-analysis-hscode-search-api.md) <br>
- [Customs market overview API](references/customs-analysis-overview-api.md) <br>
- [Customs trade share API](references/customs-analysis-trade-percent-api.md) <br>
- [Customs trend analysis API](references/customs-analysis-trends-api.md) <br>
- [Customs company partner statistics API](references/customs-company-partner-stats-api.md) <br>
- [Customs company trade statistics API](references/customs-company-stats-api.md) <br>
- [Customs overview top buyers and suppliers API](references/customs-overview-top-n-api.md) <br>
- [Customs US import statistics API](references/customs-overview-us-import-api.md) <br>
- [Global company search API](references/global-company-list-api.md) <br>
- [Global company person search API](references/global-company-person-list-api.md) <br>
- [LinkedIn company search API](references/linkedin-company-list-api.md) <br>
- [LinkedIn company employee list API](references/linkedin-company-employee-list-api.md) <br>
- [LinkedIn person search API](references/linkedin-person-list-api.md) <br>
- [LinkedIn person colleague list API](references/linkedin-person-colleague-list-api.md) <br>
- [LinkedIn person alumni list API](references/linkedin-person-alumni-list-api.md) <br>
- [LinkedIn person experience list API](references/linkedin-person-experience-list-api.md) <br>
- [LinkedIn person education list API](references/linkedin-person-education-list-api.md) <br>
- [LinkedIn school detail API](references/linkedin-school-detail-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and API-result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct agents to run paid API scripts, read API reference files, and store task results locally under task_data/.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
