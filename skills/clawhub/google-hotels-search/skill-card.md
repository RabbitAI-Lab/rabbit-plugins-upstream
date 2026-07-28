## Description: <br>
Search live Google Hotels stays by location, dates and occupancy, returned in one unified schema alongside every other booking platform. Use when a user wants to find Google Hotels listings. Powered by the StayingAPI REST API / MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to search Google Hotels stays by location, dates, occupancy, and filters through StayingAPI's REST API or MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live API use requires a StayingAPI key, and mishandling a live key can expose account access. <br>
Mitigation: Use a sandbox key for testing, store live keys in a secure credential store or protected agent config, avoid committing keys, and rotate exposed keys. <br>
Risk: Live search, polling, and upstream platform coverage can return empty, partial, failed, or rate-limited results. <br>
Mitigation: Check job status, warnings, pagination metadata, endpoint support, and Retry-After headers before presenting results as complete. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/stayingapi/skills/google-hotels-search) <br>
- [StayingAPI homepage](https://stayingapi.com) <br>
- [StayingAPI documentation](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI contract](https://api.stayingapi.com/openapi.json) <br>
- [Authentication setup](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API Calls, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with REST or MCP request details and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires STAYINGAPI_KEY for live API requests; sandbox keys return deterministic fixtures.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
