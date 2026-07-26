## Description: <br>
Helps agents query official Taiwan Stock Exchange OpenAPI data for listed-stock prices, fundamentals, financial statements, governance disclosures, broker data, warrants, indices, and trading calendars. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nanookai](https://clawhub.ai/user/nanookai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to select TWSE OpenAPI endpoints, fetch public datasets, and filter or parse Taiwan listed-company data. It is useful for stock quote, fundamentals, TAIEX, financial statement, ESG, broker, warrant, and market calendar questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may make external requests to TWSE OpenAPI endpoints when answering Taiwan stock questions. <br>
Mitigation: Use it only where outbound requests to public TWSE data sources are acceptable. <br>
Risk: TWSE endpoints often return full public datasets before filtering, which can be large. <br>
Mitigation: Filter results with code or shell pipelines and avoid pasting large raw responses into agent context. <br>
Risk: Public market data and derived analysis can be mistaken for investment advice. <br>
Mitigation: Treat outputs as informational and verify conclusions independently before making financial decisions. <br>
Risk: TWSE responses include mixed English and Traditional Chinese field names plus numeric strings with commas, blanks, or dash placeholders. <br>
Mitigation: Use the reference files for exact field names and normalize numeric strings before analysis. <br>


## Reference(s): <br>
- [TWSE OpenAPI documentation](https://openapi.twse.com.tw/) <br>
- [TWSE OpenAPI Swagger specification](https://openapi.twse.com.tw/v1/swagger.json) <br>
- [TWSE API - Securities Trading](references/securities-trading.md) <br>
- [TWSE API - Corporate Governance](references/corporate-governance.md) <br>
- [TWSE API - Financial Statements](references/financial-statements.md) <br>
- [TWSE API - Indices](references/indices.md) <br>
- [TWSE API - Warrants](references/warrants.md) <br>
- [TWSE API - Broker Data](references/brokers.md) <br>
- [TWSE API - Miscellaneous](references/misc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell and Python snippets; fetched TWSE API responses are JSON arrays.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides agents to fetch full public datasets and filter client-side by stock code or criteria.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
