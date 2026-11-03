## Description:

Unofficial Go client for the Twelve Data market data API, generated with oapi-codegen. Package twelvedata (github.com/psyb0t/go-twelvedata) provides typed REST methods for prices, quotes, time series, technical indicators, fundamentals, instrument metadata and batch queries. Use when Go code needs Twelve Data market data or already imports go-twelvedata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using Go use this skill to install and call the unofficial, typed Twelve Data client for market data, fundamentals, technical indicators, instrument metadata, and batch queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API key could be exposed through source code, logs, or URL query strings.

Mitigation: Read TWELVEDATA_API_KEY from the environment and send it in the Authorization header; do not hardcode, commit, or log credentials or authenticated requests.

Risk: API requests consume plan credits and may be limited by account permissions or rate limits.

Mitigation: Check plan and data permissions, track usage, set request limits, and use bounded backoff for rate limits.

Risk: The client is unofficial and depends on a downloaded Go module.

Mitigation: Review and pin the dependency version before use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-twelvedata)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-twelvedata)

## Skill Output:

**Output Type(s):** [Go code, Shell commands, Configuration guidance, API usage guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for adding the client and making typed API calls; no files are produced automatically.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
