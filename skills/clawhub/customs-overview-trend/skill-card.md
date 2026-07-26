## Description: <br>
Query import/export trade trend data by retrieving monthly trade volume trends within a specified time range with cursor-based pagination. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Trade analysts, supply chain managers, and market researchers use this skill to retrieve monthly customs trade totals, inspect seasonal trade-flow patterns, and continue through paginated results for a selected date range. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid trade-data API and query calls may incur account charges. <br>
Mitigation: Confirm pricing and obtain explicit user approval before running any paid query or top-up action. <br>
Risk: The skill can read or store an UpKuaJing API key in a plaintext home-directory file. <br>
Mitigation: Avoid sharing .env contents in chat or logs, and consider managing the API key manually instead of letting the helper create and persist one. <br>
Risk: Security evidence flags sensitive account, billing, credential-storage, and version-check behavior for review before installation. <br>
Mitigation: Install only after reviewing the security summary and only in environments where API-key access, account helpers, and version checks are acceptable. <br>


## Reference(s): <br>
- [Trend API Reference](references/customs-overview-trend-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing Open API Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; successful trend queries return monthly trade records plus fee information.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
