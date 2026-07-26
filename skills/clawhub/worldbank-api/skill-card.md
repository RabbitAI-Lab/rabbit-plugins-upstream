## Description: <br>
Fetch country-level economic and development data with the free World Bank Indicators API, including GDP, population, inflation, unemployment, life expectancy, CO2, poverty, trade, country comparisons, development indicators, and historical country data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nanookai](https://clawhub.ai/user/nanookai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to retrieve and interpret public World Bank country-level economic and development indicators for comparisons, historical analysis, and data-backed answers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Macroeconomic or development-data queries may be sent to the public World Bank API. <br>
Mitigation: Use the skill only for tasks where live World Bank data is desired and public API disclosure is acceptable. <br>
Risk: Broad trigger wording may cause an agent to use the World Bank API even when the user did not explicitly ask for World Bank data. <br>
Mitigation: Constrain activation to requests that need live World Bank indicators or ask the user before making public API calls for ambiguous data requests. <br>


## Reference(s): <br>
- [World Bank API skill page](https://clawhub.ai/nanookai/skills/worldbank-api) <br>
- [World Bank Indicators API](https://api.worldbank.org/v2) <br>
- [World Bank API endpoint reference](references/endpoints.md) <br>
- [Verified World Bank indicator codes](references/indicators.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API URLs, shell commands, code examples, and optional JSON data rows from the bundled script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include live public World Bank API responses and source update timestamps.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
