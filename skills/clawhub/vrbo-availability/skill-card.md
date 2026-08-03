## Description: <br>
Check day-by-day Vrbo availability (the booking calendar) for a known listing over a date window. Use when a user asks whether a listing on Vrbo is open on specific dates. Powered by StayingAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to check whether a known Vrbo listing is available across a requested date window and to interpret StayingAPI availability responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: STAYINGAPI_KEY is a sensitive API secret and can be exposed if stored in shell profiles, dotfiles, shared repositories, or logs. <br>
Mitigation: Store the key in a secure secret store or runtime-managed encrypted configuration, and avoid committing or printing it. <br>
Risk: Sandbox calls return deterministic fixtures that may not mirror the requested property, dates, or occupancy. <br>
Mitigation: Use sandbox keys for parsing and integration checks only, then switch to a live key when real availability data is required. <br>
Risk: Live API polling can hit rate limits if an agent loops too quickly while waiting for async jobs. <br>
Mitigation: Honor Retry-After, use backoff between polling attempts, and cap total retries. <br>


## Reference(s): <br>
- [StayingAPI homepage](https://stayingapi.com) <br>
- [StayingAPI docs](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI contract](https://api.stayingapi.com/openapi.json) <br>
- [StayingAPI key setup](references/auth-setup.md) <br>
- [ClawHub skill page](https://clawhub.ai/stayingapi/skills/vrbo-availability) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API calls, Shell commands, Configuration] <br>
**Output Format:** [Markdown with API request details and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires STAYINGAPI_KEY for REST API requests; MCP-capable runtimes can use the hosted StayingAPI MCP server.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
