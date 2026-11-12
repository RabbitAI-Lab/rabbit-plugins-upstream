## Description:

Provides an unofficial Go client for calling Perplexity's REST API with typed methods and JSON-decoded responses across Sonar, web search, embeddings, agents, skills, decisions, models, and usage analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the Go client to call Perplexity endpoints such as Sonar, web search, embeddings, and agent APIs, then work with typed Go request and response data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial and an artifact reference could not be resolved.

Mitigation: Review the unresolved reference and the scan limitation before installing.

Risk: Some API operations can create, update, or delete skills and start or cancel agent runs.

Mitigation: Make state-changing calls only when requested and only for resources the user named.

## Reference(s):

- [Setup and API method reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-perplexity)

## Skill Output:

**Output Type(s):** [Code, API Calls, JSON data]

**Output Format:** [Go client calls with JSON responses decoded into typed Go structs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API calls may incur charges or change account state; responses also expose status codes and raw bodies.]

## Skill Version(s):

0.3.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
