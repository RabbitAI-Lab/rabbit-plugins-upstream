## Description: <br>
Query date reference information that returns last year, last month, and same-month-last-year values for customs trade queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Export teams, trade analysts, and import-export professionals use this skill to retrieve accurate fiscal reference dates before constructing customs overview, trend, trade-list, and market intelligence queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid UpKuaJing API and query or top-up operations can incur charges. <br>
Mitigation: Confirm pricing and get explicit user approval before any paid query or account top-up flow. <br>
Risk: The UPKUAJING_API_KEY may be stored in a plaintext ~/.upkuajing/.env file. <br>
Mitigation: Use a dedicated API key, restrict local file permissions, avoid sharing the file, and rotate the key if exposure is suspected. <br>
Risk: The skill contacts UpKuaJing services for queries, pricing or account support, and a limited version check. <br>
Mitigation: Install and run it only in environments where outbound requests to UpKuaJing are acceptable. <br>


## Reference(s): <br>
- [Date Reference API](references/customs-overview-date-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing API Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns one set of date reference values per query and includes fee information when returned by the API.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
