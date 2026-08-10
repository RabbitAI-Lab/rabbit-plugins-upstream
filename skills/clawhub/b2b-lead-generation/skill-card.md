## Description: <br>
Aggregates customs trade intelligence, global company due diligence, and LinkedIn-style professional network data for B2B market analysis, supplier validation, and overseas lead generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Exporters, sourcing agents, sales teams, and B2B prospecting specialists use this skill to size product markets, profile buyers or suppliers, check company backgrounds, and identify professional contacts for cross-border customer acquisition. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables broad person-level, employee, LinkedIn-style, and contact-data searches. <br>
Mitigation: Use it only for a lawful business purpose and review privacy, employment, and outreach compliance requirements before running lookups. <br>
Risk: All API calls are paid and searches can require multiple billed calls. <br>
Mitigation: Inform the user of expected charges and obtain explicit confirmation before any paid lookup. <br>
Risk: The skill stores and reads the UpKuaJing API key from the user environment or ~/.upkuajing/.env. <br>
Mitigation: Protect the API key file, avoid sharing keys in chat or logs, and rotate keys if exposure is suspected. <br>
Risk: Lookup results may contain personal or business data and can be retained in task_data result files. <br>
Mitigation: Periodically delete task_data outputs that are no longer needed and handle exported results as sensitive business data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/b2b-lead-generation) <br>
- [UpKuaJing homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [Detailed Price Description](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Customs analysis API references](artifact/references/customs-analysis-overview-api.md) <br>
- [Customs company API references](artifact/references/customs-company-stats-api.md) <br>
- [Global company API references](artifact/references/global-company-list-api.md) <br>
- [LinkedIn people API references](artifact/references/linkedin-person-list-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API results, Guidance] <br>
**Output Format:** [Markdown guidance with Python command examples and JSON API result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; API calls are paid and may create task_data result files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
