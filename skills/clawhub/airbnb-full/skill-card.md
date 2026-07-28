## Description: <br>
Complete Airbnb toolkit for search, availability, listing detail, price, cross-OTA price comparison, and reviews in a unified StayingAPI schema. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to query Airbnb and related lodging data through StayingAPI for property discovery, availability checks, listing details, prices, cross-OTA comparisons, and reviews. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys can be exposed if pasted into prompts, logs, or shared files. <br>
Mitigation: Store STAYINGAPI_KEY securely in the agent runtime or shell environment and use sandbox keys for evaluation. <br>
Risk: Live StayingAPI calls may consume credits or make paid data requests. <br>
Mitigation: Review StayingAPI pricing before live use and start with stay_test_ sandbox keys when validating workflows. <br>
Risk: Sandbox fixtures may not reflect the requested property, dates, or occupancy. <br>
Mitigation: Use sandbox responses for parsing and error-handling tests only, then switch to a live key when accurate lodging data is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/stayingapi/skills/airbnb-full) <br>
- [StayingAPI homepage](https://stayingapi.com) <br>
- [StayingAPI documentation](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI contract](https://api.stayingapi.com/openapi.json) <br>
- [StayingAPI authentication setup](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown guidance with inline shell commands and REST API details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires STAYINGAPI_KEY for API requests; supports sandbox keys for evaluation and live keys for real lodging data.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
