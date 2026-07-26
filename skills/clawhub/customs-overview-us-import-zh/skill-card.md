## Description: <br>
查询美国进口交易统计，按州或城市返回进口记录数、集装箱数和近90天活动数据，并支持游标分页。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade teams, logistics analysts, and U.S. market operators use this skill to monitor U.S. import activity by state or city, compare container flow patterns, and evaluate market-entry signals from customs import data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid third-party API and each query can incur charges. <br>
Mitigation: Confirm each paid query in a separate user message before running the query or account action. <br>
Risk: The skill can read or write the UPKUAJING_API_KEY value in ~/.upkuajing/.env. <br>
Mitigation: Avoid displaying the .env contents in chat or logs and use a safer secret store when the runtime supports one. <br>
Risk: The skill can create API keys and recharge or payment order URLs. <br>
Mitigation: Review account and payment actions before execution and require explicit user confirmation. <br>
Risk: The skill sends requests to openapi.upkuajing.com, including a version check path. <br>
Mitigation: Review outbound network behavior before installation in restricted environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-overview-us-import-zh) <br>
- [国家贸易概览-美国进口交易 API 参考](references/customs-overview-us-import-api.md) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [API results include U.S. state or city rows, import record counts, container counts, recent 90-day counts, cursor pagination, and fee information.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
