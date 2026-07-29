## Description: <br>
Search Vrbo vacation rentals by location, dates and occupancy in one unified schema. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to search Vrbo vacation rentals by location, dates, occupancy, and filters through StayingAPI. It supports trip planning and travel research by returning normalized rental-search guidance and result handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires access to a StayingAPI key and sends rental-search requests to StayingAPI. <br>
Mitigation: Use a sandbox key for testing, and store live keys in protected agent secret storage rather than dotfiles, synced folders, logs, or shared environments. <br>
Risk: Live asynchronous search polling can trigger rate limits if retried too quickly. <br>
Mitigation: Honor Retry-After, back off between polling attempts, and cap the number of attempts. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/stayingapi/skills/vrbo-rentals) <br>
- [StayingAPI homepage](https://stayingapi.com) <br>
- [StayingAPI documentation](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI contract](https://api.stayingapi.com/openapi.json) <br>
- [Auth setup](references/auth-setup.md) <br>
- [StayingAPI MCP server](https://mcp.stayingapi.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with API request details and JSON response guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires STAYINGAPI_KEY and network access to api.stayingapi.com; sandbox keys can be used for evaluation.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
