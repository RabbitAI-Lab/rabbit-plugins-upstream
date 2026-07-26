## Description: <br>
Search award flight availability across 24 mileage programs, including business and first class, with detailed route and booking information via the seats.aero API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jarrodjs](https://clawhub.ai/user/jarrodjs) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Travelers, points users, and agents use this skill to search award flight availability, inspect route and program coverage, and retrieve trip details from the seats.aero API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles a user-provided seats.aero API key in chat context. <br>
Mitigation: Treat the key as sensitive, avoid exposing it in transcripts or logs, prefer a revocable key, and rotate it if it may have been exposed. <br>
Risk: Award availability data can become stale or rate limited. <br>
Mitigation: Check returned freshness timestamps, keep date ranges focused, use pagination deliberately, and retry later after rate-limit responses. <br>


## Reference(s): <br>
- [Seats.aero partner API access](https://seats.aero/partner) <br>
- [Seats.aero partner API base URL](https://seats.aero/partnerapi/) <br>
- [ClawHub skill page](https://clawhub.ai/jarrodjs/skills/seats-aero) <br>


## Skill Output: <br>
**Output Type(s):** [text, API calls, guidance] <br>
**Output Format:** [Markdown guidance with API request details and summarized flight award availability] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include route, cabin, date, mileage program, availability, mileage cost, freshness, pagination, and booking-link details returned by the seats.aero API.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
