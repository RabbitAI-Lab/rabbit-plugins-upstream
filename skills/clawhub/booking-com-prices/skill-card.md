## Description: <br>
Gets a Booking.com price quote for a listing and dates, then compares the property against StayingAPI-resolved offers to identify the cheapest rate. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to quote Booking.com listing prices for specified dates and occupancy, then compare resolved offers when checking whether another OTA or supplier rate is cheaper. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: STAYINGAPI_KEY is a paid-service credential and may expose account access if committed or pasted into shared files. <br>
Mitigation: Store the key in a secret manager or agent-managed credential store, use a stay_test_ sandbox key for evaluation, avoid committing the key, and rotate it if exposed. <br>
Risk: Sandbox responses are fixtures and may not match the exact property, dates, or occupancy in the request. <br>
Mitigation: Use sandbox keys for wiring and parsing only, then switch to a live key before presenting results as real prices. <br>
Risk: Cross-OTA coverage varies by property and can return only one aggregated-lowest offer. <br>
Mitigation: Inspect offers.length and avoid describing a result as a multi-platform comparison unless multiple offers are present. <br>
Risk: Scrape-backed live calls may require asynchronous polling and can hit rate limits if polled too aggressively. <br>
Mitigation: Honor Retry-After, back off between polling attempts, cap retries, and detect failed jobs from data.status rather than only HTTP status. <br>


## Reference(s): <br>
- [StayingAPI authentication setup](references/auth-setup.md) <br>
- [StayingAPI homepage](https://stayingapi.com) <br>
- [StayingAPI documentation](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI contract](https://api.stayingapi.com/openapi.json) <br>
- [Booking.com prices ClawHub release page](https://clawhub.ai/stayingapi/skills/booking-com-prices) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with REST request details, response interpretation, and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires STAYINGAPI_KEY for API requests; outputs may include price quote summaries, cross-OTA comparison guidance, polling instructions, and endpoint caveats.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
