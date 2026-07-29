## Description: <br>
Find the cheapest available rate for one hotel via the Google Hotels backbone, using exposed offers plus computed minimum and median rates from StayingAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-focused agents use this skill to compare available booking offers for a specific hotel, identify the lowest exposed rate, and explain coverage limits before presenting a result as cross-platform. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hotel/property, location, date, and occupancy queries are sent to StayingAPI during use. <br>
Mitigation: Use the skill only when that external lookup is appropriate, and avoid sending unnecessary personal or sensitive travel details. <br>
Risk: The skill requires a STAYINGAPI_KEY that could expose live API access if stored insecurely. <br>
Mitigation: Store the key in a trusted secret manager or runtime environment setting, and use a stay_test_ sandbox key for evaluation. <br>
Risk: Some properties may return only a single aggregated-lowest offer rather than multiple OTA offers. <br>
Mitigation: Check offers.length and clearly state when the result is not a multi-platform comparison. <br>
Risk: Async jobs can complete with empty results or fail with errors nested in the job payload. <br>
Mitigation: Poll with backoff, honor Retry-After, check data.status, and handle completed-empty and failed states before summarizing results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/stayingapi/skills/google-hotels-compare) <br>
- [StayingAPI homepage](https://stayingapi.com) <br>
- [StayingAPI docs](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI contract](https://api.stayingapi.com/openapi.json) <br>
- [Authentication setup](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text guidance with API request details and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe API responses, async polling status, offer counts, computed minimum and median rates, and setup steps for STAYINGAPI_KEY.] <br>

## Skill Version(s): <br>
1.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
