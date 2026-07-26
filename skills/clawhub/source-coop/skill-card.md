## Description: <br>
A geospatial data access skill that helps agents discover Source Cooperative accounts and datasets, inspect product metadata, list files, and retrieve file metadata through a Xiaobenyang API proxy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, data analysts, and GIS users use this skill to find Source Cooperative accounts and datasets, retrieve product metadata, list files, and prepare dataset URLs for downstream analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores a Xiaobenyang API key in a local .env file. <br>
Mitigation: Use an environment variable or secret manager where possible, restrict the key's scope, and remove local .env entries before sharing the workspace. <br>
Risk: Tool calls are proxied through a third-party Xiaobenyang API rather than direct local Source Cooperative access. <br>
Mitigation: Confirm users are comfortable sending requests and API credentials to that service before enabling the skill. <br>
Risk: The artifact contains inconsistent reused documentation references, including stale gaokao or school wording. <br>
Mitigation: Review tool descriptions and returned data for consistency before relying on outputs in production workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/source-coop) <br>
- [Xiaobenyang API key site](https://xiaobenyang.com) <br>
- [Xiaobenyang MCP API endpoint](https://mcp.xiaobenyang.com) <br>
- [Source Cooperative data endpoint example](https://data.source.coop/harvard-lil/gov-data/metadata/metadata.jsonl.zip) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, guidance] <br>
**Output Format:** [Markdown summaries with JSON-like tool results from API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Xiaobenyang API key; returned data should be reviewed before use because requests are proxied through a third-party service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
