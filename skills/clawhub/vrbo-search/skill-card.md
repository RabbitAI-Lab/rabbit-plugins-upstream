## Description: <br>
Searches live Vrbo stays by location, dates, and occupancy through StayingAPI, returning results in a unified accommodation schema. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travel search agents, travel planners, and developers use this skill to find Vrbo listings for a user's destination, dates, occupancy, and filters when a StayingAPI key is available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: StayingAPI credentials can be exposed if STAYINGAPI_KEY is pasted into shared or version-controlled files. <br>
Mitigation: Use a sandbox stay_test_ key for evaluation and store live keys in a secure secret store or local environment config that is not shared. <br>
Risk: Live searches require network access and may return partial, empty, failed, or rate-limited results. <br>
Mitigation: Review response status and warnings, honor Retry-After or backoff guidance, and describe partial or empty results without overstating coverage. <br>


## Reference(s): <br>
- [StayingAPI homepage](https://stayingapi.com) <br>
- [StayingAPI documentation](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI contract](https://api.stayingapi.com/openapi.json) <br>
- [Authentication setup](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with REST and MCP request details plus shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires STAYINGAPI_KEY and network access to api.stayingapi.com or mcp.stayingapi.com.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
