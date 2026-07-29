## Description: <br>
Searches live Booking.com stays by location, dates, and occupancy through StayingAPI, returning accommodation results in a unified schema. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when an agent needs to search Booking.com stays, compare matching properties, and handle StayingAPI REST or MCP search responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a StayingAPI key, and exposure of a live key could allow unauthorized API use. <br>
Mitigation: Use a sandbox key for evaluation, store live keys in a protected secret store or environment file, and avoid committing or logging the key. <br>
Risk: Live API searches may return async jobs, partial results, failed job envelopes, or rate-limit responses. <br>
Mitigation: Honor Retry-After, cap polling attempts, inspect job status and warning metadata, and treat pagination metadata as authoritative. <br>
Risk: Sandbox fixtures are deterministic examples and may not reflect the exact requested dates, occupancy, or property. <br>
Mitigation: Use sandbox responses for integration testing only, then switch to a live key when real Booking.com availability or pricing is needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/stayingapi/skills/booking-com-search) <br>
- [StayingAPI Homepage](https://stayingapi.com) <br>
- [StayingAPI Docs](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI Contract](https://api.stayingapi.com/openapi.json) <br>
- [MCP Server](https://mcp.stayingapi.com/mcp) <br>
- [Authentication Setup](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, JSON, Configuration instructions] <br>
**Output Format:** [Markdown guidance with REST and MCP request details; API responses are JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires STAYINGAPI_KEY and internet access; live search calls may return async jobs that need bounded polling.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
