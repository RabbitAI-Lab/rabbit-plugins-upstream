## Description:

Unofficial Go client for the Twelve Data market data API, generated with oapi-codegen. Package twelvedata (github.com/psyb0t/go-twelvedata) provides typed REST methods for prices, quotes, time series, technical indicators, fundamentals, instrument metadata and batch queries. Use when Go code needs Twelve Data market data or already imports go-twelvedata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add typed Twelve Data market-data requests to a Go project, including prices, historical data, indicators, fundamentals and batch queries. It guides installation, authentication, response handling and request-limit awareness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API key placed in source code, logs or a query string could be exposed.

Mitigation: Read the key from TWELVEDATA_API_KEY and send it in the Authorization header; do not hardcode, commit or log authenticated requests.

Risk: API calls consume plan credits, and endpoint access depends on the subscription and data permissions.

Mitigation: Set request limits for the user's Twelve Data plan and data permissions, and handle rate limits with bounded backoff.

Risk: The client is unofficial, and the security review covers the bundled instructions rather than a full audit of downloaded library code.

Mitigation: Review and pin the dependency version.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-twelvedata package documentation](https://pkg.go.dev/github.com/psyb0t/go-twelvedata)
- [Declared project homepage](https://github.com/psyb0t/go-twelvedata)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-twelvedata)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and concise Markdown guidance with inline shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API authentication and request examples; secrets should be supplied through environment configuration.]

## Skill Version(s):

0.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
