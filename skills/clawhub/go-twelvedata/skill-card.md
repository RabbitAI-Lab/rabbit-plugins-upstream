## Description:

Use the unofficial go-twelvedata client to write Go code for Twelve Data market prices, quotes, time series, technical indicators, fundamentals, instrument metadata and batch queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate the unofficial Go client into projects that need Twelve Data market data, indicators, fundamentals, and batch requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials can be exposed if embedded in code or URL query strings.

Mitigation: Load TWELVEDATA_API_KEY from the environment, send it in the Authorization header, and avoid logging authenticated requests.

Risk: Live requests can spend Twelve Data credits or exceed plan limits.

Mitigation: Check the plan and request budget; test against a local HTTP server instead of making live calls.

Risk: A request can return an HTTP error even when the Go call reports no error.

Mitigation: Check the HTTP status and decoded response before using market data.

## Reference(s):

- [Skill setup and reference](references/setup.md)
- [Go client homepage (skill metadata)](https://github.com/psyb0t/go-twelvedata)
- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/go-twelvedata)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go and a Twelve Data API key supplied through TWELVEDATA_API_KEY.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
