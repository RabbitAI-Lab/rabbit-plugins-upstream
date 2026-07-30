## Description: <br>
Check day-by-day Google Hotels availability (the booking calendar) for a known listing over a date window. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel or lodging agents use this skill to check whether a known Google Hotels listing is available across a requested date window. It is best used after a listing ID or listing URL is already known. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A StayingAPI key could be exposed if pasted into prompts, committed to repositories, or stored in unprotected dotfiles. <br>
Mitigation: Use a sandbox key for evaluation where possible and store live keys in the agent runtime's secret storage or another protected secret manager. <br>
Risk: Live availability checks may return asynchronous jobs, empty results, or nested failed statuses that can be misread as successful availability data. <br>
Mitigation: Poll jobs with backoff, honor Retry-After, cap attempts, and treat data.status of completed or failed as the terminal source of truth. <br>


## Reference(s): <br>
- [StayingAPI](https://stayingapi.com) <br>
- [StayingAPI Docs](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI Contract](https://api.stayingapi.com/openapi.json) <br>
- [Authentication Setup](references/auth-setup.md) <br>
- [StayingAPI MCP Server](https://mcp.stayingapi.com/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Text] <br>
**Output Format:** [Markdown with inline shell commands and API response interpretation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires STAYINGAPI_KEY for REST API requests; sandbox keys can be used for evaluation.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
