## Description:

A REST API calling assistant that helps agents make authenticated HTTP requests with retries, timeouts, rate-limit handling, pagination, JSON parsing, and error classification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to prepare and run authenticated REST API calls, retrieve paginated API data, and handle common HTTP failure modes with retries and structured outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API tokens, PII, private endpoint details, or sensitive response data could be exposed through saved outputs or learner notes/preferences.

Mitigation: Provide credentials through named environment variables, avoid saving sensitive responses unless needed, and keep secrets, PII, tokens, and private endpoint details out of learner records.

Risk: The skill can help an agent send requests to arbitrary API endpoints with user-provided methods, headers, and payloads.

Mitigation: Review the destination URL, request method, payload, authorization scope, and service rate limits before execution.

## Reference(s):


## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and optional JSON or file outputs from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API credentials should be supplied through environment variables; helper output may be written to local files when an output path is provided.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
