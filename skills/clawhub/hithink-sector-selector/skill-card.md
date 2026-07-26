## Description: <br>
Screens market sectors using valuation, fund-flow, gain/loss, sector-type, volume, and combined natural-language filters, returning matching sector data from iWenCai. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chen6896qqwee](https://clawhub.ai/user/chen6896qqwee) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to translate natural-language sector-screening requests into iWenCai sector queries, retrieve matching market-sector data, and present concise results with the final query and data source. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sector-screening queries are sent to iWenCai using an IWENCAI_API_KEY. <br>
Mitigation: Avoid confidential trading strategies, account identifiers, and other sensitive information in queries; rotate or revoke API keys if exposed. <br>
Risk: Market-sector data may be incomplete, paginated, stale, or unavailable. <br>
Mitigation: Check total result counts against returned rows, paginate when needed, cite iWenCai as the data source, and have users verify market decisions independently. <br>
Risk: Optional use of other finance or search tools can disclose related query context to additional services. <br>
Mitigation: Use fallback tools only when necessary and keep sensitive strategy details out of follow-up searches or tool calls. <br>


## Reference(s): <br>
- [iWenCai web service](https://www.iwencai.com/unifiedwap/chat) <br>
- [iWenCai SkillHub](https://www.iwencai.com/skillhub) <br>
- [iWenCai OpenAPI query endpoint](https://openapi.iwencai.com/v1/query2data) <br>
- [ClawHub skill page](https://clawhub.ai/chen6896qqwee/skills/hithink-sector-selector) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown response with optional tables and inline shell commands; CLI output may include JSON or text returned from iWenCai.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses IWENCAI_API_KEY; iWenCai results are paginated with a default limit of 10 and may require retrying relaxed queries or fetching additional pages.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release metadata, artifact clawhub.json, SKILL.md, and scripts/cli.py) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
