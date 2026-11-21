## Description:

Unofficial Go client for the Twelve Data market data API, with typed REST methods for prices, quotes, time series, technical indicators, fundamentals, instrument metadata, and batch queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add and call the unofficial typed Twelve Data client from Go code for market prices, quotes, time series, indicators, fundamentals, instrument metadata, and batch queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials can be exposed if sent as query parameters or included in logs.

Mitigation: Read the key from TWELVEDATA_API_KEY, send it in the Authorization header, and do not log authenticated requests.

Risk: Requests consume API credits, and endpoint access depends on the user's plan and data permissions.

Mitigation: Check plan and data permissions and respect the user's request budget.

Risk: The security scan reported no findings in reviewed material, but coverage was partial because two local references could not be resolved.

Mitigation: Review the referenced materials if greater assurance is needed before installation.

## Reference(s):

- [Setup and reference](references/setup.md)
- [GitHub repository](https://github.com/psyb0t/go-twelvedata)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-twelvedata)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typed client calls; requires a Twelve Data API key and provider access for requested endpoints.]

## Skill Version(s):

0.6.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
