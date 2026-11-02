## Description:

Unofficial Go client for the Perplexity REST API at https://api.perplexity.ai. Package perplexity (github.com/psyb0t/go-perplexity), generated with oapi-codegen from Perplexity's OpenAPI document, has one typed method per endpoint on the client from perplexity.NewClientWithResponses, covering Sonar chat completions (sync and async), web search, embeddings and contextualized embeddings, agents and their files, skills, decisions, models and usage analytics, with JSON bodies decoded into Go structs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add and use the typed go-perplexity client in Go projects for Perplexity chat, search, embeddings, and other API endpoints. It provides installation, authentication, request, response, and error-handling guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unofficial dependency may change or introduce unexpected behavior.

Mitigation: Review and pin the dependency before adding it.

Risk: Requests can expose submitted data to Perplexity and may incur charges or change account state.

Mitigation: Send only intended data, keep the API key private, and authorize paid or account-changing calls only for specific resources.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [go-perplexity source repository](https://github.com/psyb0t/go-perplexity)
- [go-perplexity package documentation](https://pkg.go.dev/github.com/psyb0t/go-perplexity)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-perplexity)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go code examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typed Go examples, endpoint and type references, and API key configuration guidance.]

## Skill Version(s):

0.3.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
