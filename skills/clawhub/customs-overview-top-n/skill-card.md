## Description: <br>
Query ranked suppliers or buyers by trade volume for a country pair and year, returning cursor-paginated company lists from the UpKuaJing customs database. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sourcing agents, export teams, and trade analysts use this skill to identify leading suppliers or buyers, assess trading-counterpart concentration, and browse ranked company results for strategic procurement or sales planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid UpKuaJing account and API calls may incur charges. <br>
Mitigation: Tell the user that the query incurs a fee and wait for explicit confirmation before running a paid query or creating a top-up order. <br>
Risk: The skill reads and may store an API key in a local plaintext file. <br>
Mitigation: Use the UPKUAJING_API_KEY environment variable when possible, restrict access to the local credential file, and avoid sharing terminal output that reveals credential paths or key material. <br>
Risk: The skill performs an automatic version-check request during API use and writes a local version cache. <br>
Mitigation: Review this network behavior before deployment in restricted environments and account for the local cache under the user's home directory. <br>
Risk: Incorrect query parameters can produce failed or misleading trade-data results. <br>
Mitigation: Consult the bundled API reference for required fields, company type values, and cursor handling before executing a query. <br>


## Reference(s): <br>
- [Customs Overview Top N API Reference](references/customs-overview-top-n-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results are paginated by cursor and include fee information returned by the API.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
