## Description: <br>
Query paginated product trade data for a company, including product names, trade counts, amounts, quantities, weights, trade percentages, and associated HS codes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and trade analysts use this skill to retrieve a company's paginated customs product mix and inspect trade statistics and HS-code associations. It supports product portfolio analysis, import-export breakdowns, and drill-downs across supplier or buyer roles. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid UpKuaJing API and individual product-list queries may incur charges. <br>
Mitigation: Confirm pricing and obtain explicit user approval before each paid query. <br>
Risk: The skill reads and may store the UpKuaJing API key in plaintext at ~/.upkuajing/.env. <br>
Mitigation: Avoid printing the env file, restrict file permissions, and install only where access to the API key is acceptable. <br>
Risk: Incorrect query parameters can return errors or unintended paid queries. <br>
Mitigation: Check the bundled API reference for parameter names, required fields, pagination, and supported filters before execution. <br>


## Reference(s): <br>
- [Company Product List API Reference](references/customs-company-product-list-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Developer Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-company-product-list) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [JSON API responses with concise Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Paginated responses can include a cursor, fee information, product records, trade counts, amounts, quantities, weights, percentages, and HS-code arrays.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
