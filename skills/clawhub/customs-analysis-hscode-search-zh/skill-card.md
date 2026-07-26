## Description: <br>
按产品名称和HS编码关键词从海关贸易数据中搜索匹配的HS编码，并返回可用于后续贸易分析的HS编码列表。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Trade analysts, exporters, importers, and agents use this skill to identify likely customs HS classifications before running deeper customs trade-data analyses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses paid third-party API calls and can create recharge payment URLs. <br>
Mitigation: Tell the user a query or recharge flow may incur charges and wait for explicit confirmation before running it. <br>
Risk: The skill may store an API key in plaintext at ~/.upkuajing/.env. <br>
Mitigation: Limit access to the local credential file, avoid sharing its contents, and rotate the API key if exposure is suspected. <br>
Risk: API calls may read account balance details and perform automatic version-check requests with a local cache write. <br>
Mitigation: Run the skill only in environments where these account-information and network side effects are acceptable. <br>


## Reference(s): <br>
- [HS编码搜索 API 参考](references/customs-analysis-hscode-search-api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-analysis-hscode-search-zh) <br>
- [跨境魔方](https://www.upkuajing.com) <br>
- [跨境魔方开放平台](https://developer.upkuajing.com/) <br>
- [OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON results from the API scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; paid API calls require explicit user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
