## Description:

An unofficial Go client for the Perplexity REST API that provides typed methods for Sonar chat, search, embeddings, agents, skills, decisions, models, and usage analytics, with bearer-key authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this client to call Perplexity endpoints for Sonar chat, search, embeddings, agents, skills, decisions, models, and usage analytics. It returns typed Go response values or raw HTTP responses for endpoints that need custom handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is benign with medium confidence, and scan evidence is incomplete because a local reference was reported missing.

Mitigation: Review the skill and its referenced setup documentation before installation; treat the scan verdict as partial evidence.

Risk: Some API calls can incur charges or change account state, including creating, updating, and deleting skills and creating or cancelling agent runs.

Mitigation: Make state-changing or paid calls only when requested, and only for resources the user created or named; review deletion operations before use.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-perplexity)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-perplexity)
- [Perplexity API](https://api.perplexity.ai)

## Skill Output:

**Output Type(s):** [API Calls, Code, JSON, Text]

**Output Format:** [Go client calls with typed response structs, JSON-decoded bodies, or raw HTTP responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are decoded as a whole; use the plain client to handle streaming responses.]

## Skill Version(s):

0.6.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
