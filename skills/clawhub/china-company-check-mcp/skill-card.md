## Description: <br>
China Check helps agents look up and verify mainland-China companies using official GSXT/SAMR registration data through the China-Check MCP tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ballcheung](https://clawhub.ai/user/ballcheung) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to find, vet, or verify mainland-China companies, suppliers, factories, manufacturers, brands, and business partners. It returns registry facts such as legal name, registration status, legal representative, USCC, registered capital, address, business scope, and industry. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Company names, domains, phone numbers, or registration identifiers are sent to the disclosed China-Check MCP service for lookup. <br>
Mitigation: Confirm the user is comfortable sharing those lookup terms with the service before use. <br>
Risk: Returned registration data is informational and may be insufficient for mission-critical supplier, legal, or financial decisions. <br>
Mitigation: Verify mission-critical decisions against official sources and avoid implying that the free snapshot includes risk, litigation, ownership, or IP data. <br>


## Reference(s): <br>
- [Source repository](https://github.com/ballcheung/china-company-check-mcp) <br>
- [ClawHub listing](https://clawhub.ai/ballcheung/skills/china-company-check-mcp) <br>
- [China-Check MCP server](https://www.china-check.com/api/mcp/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown summaries with registry fields returned from MCP tool calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only lookups; search queries are limited to 100 characters and company identifiers to 64 characters.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
