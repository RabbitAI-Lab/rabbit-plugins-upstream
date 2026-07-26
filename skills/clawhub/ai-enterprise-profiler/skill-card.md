## Description: <br>
AI 企业画像 helps AI practitioners research company profiles, competitors, financing, teams, products, and strategic positioning through Jiqizhixin's enterprise data service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiqizhixin](https://clawhub.ai/user/jiqizhixin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External AI industry researchers, business development teams, market analysts, and strategy teams use this skill to build enterprise profiles, compare competitors, summarize financing and team signals, and turn enterprise API results into structured conclusions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AI-company research queries and filters are sent to the Jiqizhixin service and may reveal research interests or strategy terms. <br>
Mitigation: Use the skill only for queries your organization has approved for that provider, and avoid confidential client names or non-public strategy terms unless approved. <br>
Risk: The skill requires JQZX_API_TOKEN to call the enterprise API. <br>
Mitigation: Keep the token out of chat, logs, screenshots, shell history, and repositories; provide it only through the expected environment variable. <br>
Risk: Enterprise search results may be incomplete or narrow when sample coverage is low. <br>
Mitigation: State coverage boundaries in outputs, retry with aliases or broader query terms, and use supplemental public data only when the skill's results are insufficient. <br>


## Reference(s): <br>
- [/api/v1 Enterprise API Strategy](references/api-v1-enterprises.md) <br>
- [Search Keyword Synonym Reference](references/keyword_reference.md) <br>
- [Jiqizhixin Data Service](https://www.jiqizhixin.com/data-service) <br>
- [ClawHub Skill Page](https://clawhub.ai/jiqizhixin/skills/ai-enterprise-profiler) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown summaries with structured tables, shell command examples, and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires JQZX_API_TOKEN and the curl and jq command-line tools to query a third-party enterprise API.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
