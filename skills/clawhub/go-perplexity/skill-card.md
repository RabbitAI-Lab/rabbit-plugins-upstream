## Description:

Unofficial Go client for the Perplexity REST API at https://api.perplexity.ai. Package perplexity (github.com/psyb0t/go-perplexity), generated with oapi-codegen from Perplexity's OpenAPI document, has one typed method per endpoint on the client from perplexity.NewClientWithResponses, covering Sonar chat completions (sync and async), web search, embeddings and contextualized embeddings, agents and their files, skills, decisions, models and usage analytics, with JSON bodies decoded into Go structs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add typed calls to the Perplexity REST API from a Go project. It provides setup, authentication, request and response examples, endpoint references, and error-handling guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review covers the skill instructions, not the downloaded Go library implementation.

Mitigation: Review and pin the third-party dependency before use.

Risk: The client sends an API key with requests, and exposed credentials could be misused.

Mitigation: Read the key from an environment variable; do not hardcode, commit, log it, or print request headers.

Risk: Perplexity API calls can incur charges, and some endpoints change account state.

Mitigation: Expect API charges and make account-changing calls only when requested, limited to resources the user created or named.

Risk: Requests can be sent to the configured base URL.

Mitigation: Use the documented base URL, https://api.perplexity.ai.

## Reference(s):

- [Setup and API reference](artifact/references/setup.md)
- [Source repository](https://github.com/psyb0t/go-perplexity)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-perplexity)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-perplexity)

## Skill Output:

**Output Type(s):** [Go code, Shell commands, Configuration guidance, Technical guidance]

**Output Format:** [Markdown with Go code blocks, shell commands, and endpoint tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use a bearer API key and the Perplexity API base URL; generated response helpers do not parse server-sent event streams.]

## Skill Version(s):

0.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
