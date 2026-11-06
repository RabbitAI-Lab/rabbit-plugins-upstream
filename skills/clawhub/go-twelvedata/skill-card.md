## Description:

Provides Go developers with an unofficial, typed client for the Twelve Data market data API, including methods for prices, quotes, time series, technical indicators, fundamentals, instrument metadata and batch queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to add the unofficial go-twelvedata client to a Go project and make typed requests for Twelve Data market information, including prices, historical series, indicators and fundamentals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API key can be exposed if it is hardcoded, committed, logged or sent in a URL.

Mitigation: Read TWELVEDATA_API_KEY from the environment and send it in the Authorization header; do not hardcode, commit or log credentials.

Risk: API requests consume plan credits and may be limited by subscription and data permissions.

Mitigation: Check endpoint access and plan limits, and set a request budget before making calls.

Risk: The Go dependency is unofficial and its source is not bundled with this skill.

Mitigation: Pin and review the dependency before use.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [go-twelvedata source repository](https://github.com/psyb0t/go-twelvedata)
- [go-twelvedata Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-twelvedata)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and instructions for configuring the API client and handling responses.]

## Skill Version(s):

0.3.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
