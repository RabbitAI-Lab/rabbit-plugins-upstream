## Description: <br>
Read normalized Booking.com reviews for a listing, with native rating scales preserved. Use when a user wants ratings or guest feedback for a listing on Booking.com. Powered by StayingAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent operators use this skill to retrieve normalized Booking.com guest reviews for a known listing through StayingAPI. It is appropriate when the user has a listing ID or URL and needs ratings, guest feedback, pagination-aware retrieval, or MCP-based review access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a StayingAPI key and outbound requests to StayingAPI. <br>
Mitigation: Use a sandbox key for evaluation when possible, and store live keys only in a trusted environment variable or agent-managed secret store. <br>
Risk: Live review retrieval can return asynchronous jobs, partial results, empty results, or failed job envelopes. <br>
Mitigation: Poll with backoff, honor Retry-After, cap attempts, and inspect job status, warnings, and pagination metadata before summarizing results. <br>
Risk: Platform support differs by endpoint, and Google is not enabled for listing detail or reviews. <br>
Mitigation: Use the documented support matrix and request reviews only for booking, airbnb, or vrbo platforms. <br>


## Reference(s): <br>
- [StayingAPI homepage](https://stayingapi.com) <br>
- [StayingAPI documentation](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI contract](https://api.stayingapi.com/openapi.json) <br>
- [StayingAPI API key setup](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Markdown, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with REST API request details and review summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires STAYINGAPI_KEY and outbound access to api.stayingapi.com; native rating scales are preserved.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
