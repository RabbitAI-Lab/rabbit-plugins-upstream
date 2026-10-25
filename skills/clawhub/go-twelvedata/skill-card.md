## Description:

Guides Go developers in using the unofficial go-twelvedata client for Twelve Data market data, including setup, authentication, endpoint discovery, and response handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Twelve Data prices, quotes, historical data, indicators, and other market data into their applications through an unofficial typed client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using an unofficial client may not meet requirements for a provider-maintained integration.

Mitigation: Confirm that an unofficial Twelve Data Go client is acceptable before adopting it.

Risk: Live requests consume API credits and may exceed plan or data permissions.

Mitigation: Check the plan and request budget; test request handling against a local HTTP server.

Risk: API keys placed in code or query strings may be disclosed.

Mitigation: Read TWELVEDATA_API_KEY from the environment and send it in the Authorization header; never log or commit it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-twelvedata)
- [Client repository (linked in skill documentation; not verified release provenance)](https://github.com/psyb0t/go-twelvedata)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-twelvedata)
- [Setup and reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples require a Twelve Data API key and the requested instruments; live requests consume API credits.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
