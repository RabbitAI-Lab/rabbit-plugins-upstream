## Description: <br>
Read an Airbnb listing calendar as day-by-day availability over a date window when a user asks whether an Airbnb is open on specific dates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel operators use this skill to check day-by-day Airbnb listing availability for known listing IDs or URLs over a requested date window through StayingAPI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: STAYINGAPI_KEY is a credential required for all API requests. <br>
Mitigation: Use a sandbox stay_test_ key for evaluation, store live keys in a secure agent or runtime secret store, avoid committing keys, and rotate any key that may have been exposed. <br>
Risk: Live availability checks depend on external StayingAPI responses and may return asynchronous, partial, empty, or failed results. <br>
Mitigation: Inspect job status, warnings, and errors before presenting results, pace polling with backoff, and distinguish sandbox fixtures from live data. <br>


## Reference(s): <br>
- [StayingAPI](https://stayingapi.com) <br>
- [StayingAPI docs](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI contract](https://api.stayingapi.com/openapi.json) <br>
- [Authentication setup](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API request details and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires STAYINGAPI_KEY and internet access to api.stayingapi.com; sandbox keys return fixtures for evaluation.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
