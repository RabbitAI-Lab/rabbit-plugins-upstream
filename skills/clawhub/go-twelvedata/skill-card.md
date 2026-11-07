## Description:

Unofficial Go client for the Twelve Data market data API, generated with oapi-codegen. Package twelvedata (github.com/psyb0t/go-twelvedata) provides typed REST methods for prices, quotes, time series, technical indicators, fundamentals, instrument metadata and batch queries. Use when Go code needs Twelve Data market data or already imports go-twelvedata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to integrate typed Twelve Data API calls into a Go project for prices, quotes, time series, fundamentals, instrument metadata, and batch requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reported no findings but has medium confidence because two local references could not be resolved.

Mitigation: Review the referenced setup materials before relying on the skill's guidance.

Risk: An API key could be exposed if placed in a URL or written to logs.

Mitigation: Read TWELVEDATA_API_KEY from the environment, send it in the Authorization header, and do not log authenticated requests.

Risk: API requests consume credits and may be limited by the user's plan or rate limits.

Mitigation: Check plan permissions and usage, respect the request budget, and handle rate limits with bounded backoff.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-twelvedata)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.4.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
