## Description: <br>
Check day-by-day Booking.com availability for a known listing over a date window, powered by StayingAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent developers use this skill to check whether a known Booking.com listing is available across requested dates. It guides agents to call StayingAPI availability endpoints, handle asynchronous jobs, and report calendar availability without treating price lookup as part of this skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live StayingAPI keys can authorize billable or sensitive API access if exposed. <br>
Mitigation: Use a sandbox key for testing, store live keys only in secure runtime secret storage, and revoke exposed keys promptly. <br>
Risk: Availability calls depend on external network access and upstream platform coverage, so results may be delayed, partial, empty, or failed. <br>
Mitigation: Respect Retry-After headers, cap polling attempts, inspect job status and warnings, and present empty or failed results explicitly. <br>


## Reference(s): <br>
- [StayingAPI homepage](https://stayingapi.com) <br>
- [StayingAPI documentation](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI contract](https://api.stayingapi.com/openapi.json) <br>
- [Authentication setup](references/auth-setup.md) <br>
- [ClawHub skill page](https://clawhub.ai/stayingapi/skills/booking-com-availability) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with API request guidance and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires STAYINGAPI_KEY and internet access to api.stayingapi.com.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
