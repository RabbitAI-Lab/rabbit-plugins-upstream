## Description: <br>
Official Supermetrics skill. Query marketing data from 100+ platforms including Google Analytics, Meta Ads, Google Ads, and LinkedIn. Requires API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bartschneider](https://clawhub.ai/user/bartschneider) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Marketing analysts, developers, and agent operators use this skill to discover Supermetrics data sources, accounts, metrics, and dimensions, then query connected marketing analytics data through Supermetrics with an API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access Supermetrics-connected marketing accounts when provided an API key. <br>
Mitigation: Use a scoped or revocable API key where possible, verify the publisher before adding credentials, and remove credentials when access is no longer needed. <br>
Risk: Queries may retrieve unintended account data if the account, fields, filters, or date range are incorrect. <br>
Mitigation: Confirm the target account, selected fields, filters, and date range before running data queries. <br>


## Reference(s): <br>
- [Supermetrics MCP API endpoint](https://mcp.supermetrics.com) <br>
- [ClawHub skill page](https://clawhub.ai/bartschneider/skills/supermetrics-openclawd) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Code, Configuration instructions, Guidance] <br>
**Output Format:** [Python helper functions returning dictionaries with success, data, or error fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SUPERMETRICS_API_KEY from the environment or the skill .env file.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
