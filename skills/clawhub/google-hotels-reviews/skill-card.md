## Description: <br>
Google Hotels review text is not available through StayingAPI; this skill tells an agent to use Google Hotels aggregate ratings from /v1/search or review text from Booking.com, Airbnb, or Vrbo instead. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill when asked for Google Hotels review text so they can explain that StayingAPI does not provide it, use aggregate rating fields from /v1/search, or switch to Booking.com, Airbnb, or Vrbo for review text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent could continue retrying the unsupported Google Hotels reviews endpoint or imply that review text is available. <br>
Mitigation: State that Google Hotels review text is unavailable through StayingAPI and route review-text requests to Booking.com, Airbnb, or Vrbo. <br>
Risk: A live StayingAPI key could be used during evaluation when sandbox behavior is sufficient. <br>
Mitigation: Use a stay_test_ sandbox key when evaluating and store STAYINGAPI_KEY securely before making API requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/stayingapi/skills/google-hotels-reviews) <br>
- [StayingAPI homepage](https://stayingapi.com) <br>
- [StayingAPI API contract](https://api.stayingapi.com/openapi.json) <br>
- [Authentication setup](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, shell commands, API calls, configuration] <br>
**Output Format:** [Markdown guidance with inline API endpoint and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires STAYINGAPI_KEY for API requests; Google Hotels review text is not supported.] <br>

## Skill Version(s): <br>
1.1.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
