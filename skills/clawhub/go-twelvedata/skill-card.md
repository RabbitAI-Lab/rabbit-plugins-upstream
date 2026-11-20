## Description:

Unofficial Go client for the Twelve Data market data API, generated with oapi-codegen. Package twelvedata (github.com/psyb0t/go-twelvedata) provides typed REST methods for prices, quotes, time series, technical indicators, fundamentals, instrument metadata and batch queries. Use when Go code needs Twelve Data market data or already imports go-twelvedata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to add typed calls to the Twelve Data API for prices, quotes, time series, technical indicators, fundamentals, instrument metadata, and batch queries. It is suited to projects using the go-twelvedata module.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial because two local references in SKILL.md did not resolve.

Mitigation: Check that referenced files are present and review their contents before installing.

Risk: An API key placed in a query string or logged request could be exposed, and API calls consume account credits.

Mitigation: Read the key from TWELVEDATA_API_KEY, send it in the Authorization header, keep it out of code and logs, and respect the plan's permissions and request budget.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [Project homepage](https://github.com/psyb0t/go-twelvedata)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-twelvedata)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typed API calls depend on the selected endpoint, instruments, and request parameters.]

## Skill Version(s):

0.5.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
