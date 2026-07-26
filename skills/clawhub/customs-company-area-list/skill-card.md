## Description: <br>
Query paginated trade-area data for a company to retrieve country and region breakdowns with trade counts, amounts, quantities, weights, and percentages for market analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External analysts and developers use this skill to query UpKuaJing customs data for a company's country or region trade breakdown, including paginated drill-downs by company role and optional filters such as date range, product, HS code, country code, or port. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid third-party API and can guide account top-up or payment order creation. <br>
Mitigation: Confirm pricing and obtain explicit user approval before fee-incurring queries or top-up actions. <br>
Risk: The API key may be stored locally in ~/.upkuajing/.env. <br>
Mitigation: Protect the local .env file and prefer an environment variable or secret manager where available. <br>
Risk: The skill sends company query parameters to UpKuaJing services and returns third-party customs data. <br>
Mitigation: Use the API reference for parameter selection and review returned data before using it for market decisions. <br>


## Reference(s): <br>
- [Company Area List API](references/customs-company-area-list-api.md) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, API calls, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and formatted JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Queries return paginated country or region records and fee information; users may need to provide a cursor to retrieve additional pages.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
