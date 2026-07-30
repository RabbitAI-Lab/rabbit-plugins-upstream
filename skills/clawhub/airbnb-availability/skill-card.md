## Description: <br>
Check day-by-day Airbnb availability for a known listing over a date window using StayingAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to check whether a known Airbnb listing is available across specific dates. It is suited for travel and accommodation workflows that already have a listing URL or platform listing ID. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The STAYINGAPI_KEY secret could be exposed through shared shell profiles, logs, command history, or version control. <br>
Mitigation: Use a sandbox key for testing, store live keys only in a trusted secret store or restricted-permission environment file, and avoid pasting keys into shared locations. <br>
Risk: Live availability calls may return asynchronous jobs, empty results, partial results, or failed job payloads that can be misread as complete availability data. <br>
Mitigation: Poll using Retry-After with bounded backoff, check terminal job status explicitly, and treat meta warnings and platform support limits as authoritative before summarizing results. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/stayingapi/skills/airbnb-availability) <br>
- [StayingAPI Homepage](https://stayingapi.com) <br>
- [StayingAPI Docs](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI Contract](https://api.stayingapi.com/openapi.json) <br>
- [Authentication Setup Reference](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with HTTP request details, setup commands, and expected JSON response handling] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires STAYINGAPI_KEY and internet access to api.stayingapi.com; MCP-capable runtimes may use the StayingAPI MCP server.] <br>

## Skill Version(s): <br>
1.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
