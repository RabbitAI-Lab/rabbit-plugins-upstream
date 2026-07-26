## Description: <br>
查询分页的国家贸易列表数据，获取国家级别的贸易分解，包含年度、季度和月度贸易量，用于市场分析。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade teams, market researchers, and trade analysts use this skill to query paginated country-level import and export breakdowns from Upkuajing for country comparison, market penetration analysis, and growth opportunity discovery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses paid Upkuajing API calls and each page query may incur a charge. <br>
Mitigation: Tell the user a charge will occur, obtain explicit confirmation in a separate message before each charged query, and use the pricing command or pricing page for current costs. <br>
Risk: The skill stores and reads the UPKUAJING_API_KEY from ~/.upkuajing/.env when an environment variable is not set. <br>
Mitigation: Keep the local key file permission-restricted, avoid sharing the key, and rotate it if it may have been exposed. <br>
Risk: Trade search parameters and account or recharge requests are sent to Upkuajing services. <br>
Mitigation: Use the skill only when the user is comfortable sharing the requested trade parameters with Upkuajing and review account or payment links before opening them. <br>


## Reference(s): <br>
- [国家贸易列表 API 参考](references/customs-overview-trade-list-api.md) <br>
- [ClawHub skill listing](https://clawhub.ai/upkuajing/skills/customs-overview-trade-list-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Queries return paginated country trade records and fee information when the API call succeeds.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
