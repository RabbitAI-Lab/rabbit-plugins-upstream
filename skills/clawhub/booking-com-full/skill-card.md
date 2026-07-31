## Description: <br>
Complete Booking.com toolkit — search, availability, listing detail, price, cross-OTA price comparison and reviews, all in one unified schema. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when an agent needs broad Booking.com accommodation coverage through StayingAPI, including search, availability, listing detail, price quotes, cross-OTA price comparison, and reviews. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a StayingAPI key, and weak storage practices could expose a live credential. <br>
Mitigation: Store live keys in a credential manager or runtime secret store where possible; use a sandbox key for evaluation. <br>
Risk: Live API calls may consume account credits. <br>
Mitigation: Use sandbox keys for testing and review requests before switching to a live key. <br>


## Reference(s): <br>
- [StayingAPI homepage](https://stayingapi.com) <br>
- [StayingAPI docs](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI contract](https://api.stayingapi.com/openapi.json) <br>
- [Authentication setup](references/auth-setup.md) <br>
- [ClawHub skill page](https://clawhub.ai/stayingapi/skills/booking-com-full) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Configuration instructions, Shell commands, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with REST API requests and JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires STAYINGAPI_KEY and internet access to api.stayingapi.com; sandbox keys return deterministic fixtures.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
