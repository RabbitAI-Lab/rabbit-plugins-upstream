## Description: <br>
Queries Upkuajing customs analysis overview data by country, returning supplier and buyer counts with cursor pagination. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Trade analysts, market researchers, and import-export operators use this skill to compare supplier and buyer activity across countries for a customs product analysis overview. Agents can use it to guide paid API queries, inspect fee-bearing JSON results, and continue through cursor-paginated country rows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill calls a paid third-party customs data API and each query can incur charges. <br>
Mitigation: Confirm each paid query in a separate user message before running the query or account action. <br>
Risk: The skill may read, use, or create an API key stored in plaintext under ~/.upkuajing/.env. <br>
Mitigation: Avoid displaying the credential file contents in chat or logs, and use a safer secret store when the runtime supports one. <br>
Risk: The skill can create API keys and recharge payment URLs for the Upkuajing account flow. <br>
Mitigation: Review account and billing actions before execution and require explicit user confirmation. <br>
Risk: The skill sends requests to openapi.upkuajing.com, including a daily version-check request during API use. <br>
Mitigation: Review outbound network behavior before installation in restricted or compliance-sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-analysis-overview-zh) <br>
- [分析报告-概览 API 参考](references/customs-analysis-overview-api.md) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [API results include country rows, supplier counts, buyer counts, latest trade date fields, cursor pagination, and fee information.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
