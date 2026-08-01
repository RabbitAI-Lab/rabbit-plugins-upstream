## Description: <br>
Search live Airbnb stays by location, dates and occupancy, returned in one unified schema alongside every other booking platform. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they want an agent to search Airbnb stays by location, dates, occupancy, and filters through StayingAPI. It is useful for travel accommodation discovery where results need to be normalized across booking platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Accommodation search parameters are sent to StayingAPI when live search is used. <br>
Mitigation: Use the skill only when the user intends to search stays, and avoid sending unnecessary sensitive trip details. <br>
Risk: The skill requires storing and using a StayingAPI key for API requests. <br>
Mitigation: Store STAYINGAPI_KEY in the agent runtime's secret or environment configuration, and use a stay_test_ sandbox key for evaluation when live results are not needed. <br>
Risk: Live calls may return asynchronous, partial, empty, or failed results depending on upstream availability. <br>
Mitigation: Follow the documented polling behavior, honor Retry-After, inspect job status and warnings, and present partial or empty results as such. <br>


## Reference(s): <br>
- [StayingAPI homepage](https://stayingapi.com) <br>
- [StayingAPI documentation](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI contract](https://api.stayingapi.com/openapi.json) <br>
- [StayingAPI MCP endpoint](https://mcp.stayingapi.com/mcp) <br>
- [Authentication setup](references/auth-setup.md) <br>
- [ClawHub skill page](https://clawhub.ai/stayingapi/skills/airbnb-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance, API calls] <br>
**Output Format:** [Markdown guidance with REST endpoint details, MCP guidance, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires STAYINGAPI_KEY and internet access to api.stayingapi.com; live requests send accommodation search parameters to StayingAPI.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
