## Description: <br>
Fetch exchange rates and convert currencies with the free Frankfurter API (no API key). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nanookai](https://clawhub.ai/user/nanookai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to fetch exchange rates, convert currencies, inspect provider data, and retrieve historical foreign-exchange reference data through the Frankfurter public API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Frankfurter returns daily reference-rate data, not live trading data, so stale or blended rates may be unsuitable for compliance-sensitive or financial-decision use. <br>
Mitigation: Check returned dates and provider details, and pin an appropriate provider when official source attribution is required. <br>


## Reference(s): <br>
- [Frankfurter API](https://api.frankfurter.dev) <br>
- [Frankfurter API v2 Endpoint Reference](references/endpoints.md) <br>
- [Frankfurter v1 API Legacy Reference](references/v1-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON, CSV, NDJSON, Python, JavaScript, and HTTP examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No API key required; responses are public daily reference-rate data from the Frankfurter API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
