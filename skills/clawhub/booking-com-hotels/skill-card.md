## Description: <br>
Search Booking.com hotels by location, dates, and occupancy in a unified schema with cross-OTA price comparison powered by StayingAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-planning agents use this skill to discover Booking.com hotel options by location, dates, occupancy, and price, then compare available offers across supported travel platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys can be exposed if pasted into prompts, version-controlled files, or shared dotfiles. <br>
Mitigation: Use a sandbox key for testing when possible, keep live keys in an agent secret store or OS keychain, and rotate any key that may have been exposed. <br>
Risk: Live hotel search results can be partial, empty, delayed by asynchronous jobs, or limited by platform coverage. <br>
Mitigation: Check job status, warnings, pagination, and offer counts before presenting results, honor Retry-After, and avoid claiming multi-platform coverage when the response does not support it. <br>


## Reference(s): <br>
- [StayingAPI homepage](https://stayingapi.com) <br>
- [StayingAPI docs](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI contract](https://api.stayingapi.com/openapi.json) <br>
- [StayingAPI pricing](https://stayingapi.com/pricing) <br>
- [StayingAPI MCP server](https://mcp.stayingapi.com/mcp) <br>
- [Auth setup](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with API endpoint details and inline bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires STAYINGAPI_KEY and internet access to api.stayingapi.com; live calls may return asynchronous job results.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
